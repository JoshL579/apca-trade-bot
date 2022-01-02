from api.trade.position import get_open_position
from api.account.profile import get_account
from database.db_handler import get_transactions, add_transaction, get_entry, add_entry, delete_entry, update_entry, get_lot_size
from config import price_range, max_orders, liquidation_limit


def calculate_price(symbol, bias):
    position = get_open_position(symbol)

    # order_not_exist
    if position.get('code') == 40410000 or position.get('code') == 40010001:
        return False

    # no preset orders
    if len(get_transactions()) == 0:
        preset_orders(position)

    # get Long/Short & Lot Size per order & order quantity
    current_price = float(position.get('current_price'))
    direction, price, quantity = get_amounts(current_price)

    if not direction or not price or not quantity:
        return False

    if direction == 'L':
        amount = get_lot_size() * quantity
        return {'direction': direction, 'amount': amount, 'price': price}

    total = len(get_transactions())
    shares = float(position.get('qty')) / total * quantity
    return {'direction': direction, 'shares': shares, 'price': price}


def preset_orders(position):
    # clear entry db table
    if get_entry() is not None:
        delete_entry()

    # create orders
    size = float(get_account().get('buying_power') * liquidation_limit) / (max_orders + 1)
    add_entry(float(position.get('avg_entry_price')), size)

    gap = (price_range[1] - price_range[0]) / max_orders
    price = price_range[0]

    for i in range(int(max_orders) + 1):
        add_transaction(price)
        price += gap


def get_amounts(current_price):
    transactions = get_transactions()
    last_entry = get_entry()
    up_prices = down_prices = []

    # case price increased
    if current_price > last_entry:
        for transaction in transactions:
            if current_price > transaction.price > last_entry:
                up_prices.append(transaction.price)
        if len(up_prices) == 0:
            return False, False, False
        return 'S', max(up_prices), len(up_prices)

    # case price decreased
    if current_price < last_entry:
        for transaction in transactions:
            if last_entry > transaction.price > current_price:
                down_prices.append(transaction.price)
        if len(up_prices) == 0:
            return False, False, False
        return 'L', min(down_prices), len(down_prices)

    return False, False, False
