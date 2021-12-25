from service.price import calculate_price
from api.trade.order import place_one_order, get_orders
from api.trade.position import close_one_position, get_open_position
from config import bias_to_place_new_order


def maintain_order(symbol):
    # already have unfulfilled order waiting for process
    if len(get_orders()) > 0:
        return True

    direction = calculate_price(symbol, bias_to_place_new_order)

    if not direction:
        return True

    if direction == 'B':
        current_position = get_open_position(symbol)
        current_value = current_position.get("market_value")
        entry_value = current_position.get("cost_basis")
        amount_to_buy = float(entry_value) - float(current_value)
        return place_one_order(symbol, amount_to_buy)

    if direction == 'S':
        current_position = get_open_position(symbol)
        current_value = current_position.get("market_value")
        entry_value = current_position.get("cost_basis")
        percentage = str((float(current_value) - float(entry_value)) / float(current_value) * 100)

        return close_one_position(symbol, percentage)
