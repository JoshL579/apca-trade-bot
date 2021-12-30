from api.trade.position import get_open_position
from api.account.profile import get_account
from database.db_handler import get_transactions, add_transaction
from config import price_range, max_orders


def calculate_price(symbol, bias):
    position = get_open_position(symbol)

    # order_not_exist
    if position.get('code') == 40410000 or position.get('code') == 40010001:
        return False

    # no preset orders
    if len(get_transactions()) == 0:
        preset_orders(position)

    # todo: check price in db

    diff = float(position.get('market_value')) - float(position.get('cost_basis'))

    # case: raised
    if diff > 0:
        if diff > bias:
            return 'S'

    # case: decreased
    if diff < 0:
        if diff < -bias:
            return 'B'

    return False


def preset_orders(position):
    # create orders
    amount = get_account().get('buying_power') / max_orders

    size = (price_range[1] - price_range[0]) / max_orders
    market_price = position.get('current_price')
    prices = []
    up_price = down_price = market_price

    # down price
    for i in range(int(max_orders / 2)):
        prices.append(down_price)
        down_price -= size

    # up price
    for i in range(int(max_orders / 2)):
        prices.append(up_price)
        up_price += size

    for price in prices:
        add_transaction(price)
