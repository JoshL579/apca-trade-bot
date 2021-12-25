from service.price import calculate_price
from api.trade.order import place_one_order
from api.trade.position import close_one_position, get_open_position


def maintain_order(symbol):
    bias = 1
    direction = calculate_price(symbol, bias)

    if not direction:
        return True

    if direction == 'B':
        return place_one_order(symbol)

    if direction == 'S':
        current_position = get_open_position(symbol)
        current_value = current_position.get("market_value")
        entry_value = current_position.get("cost_basis")
        percentage = str((int(current_value) - int(entry_value)) / int(current_value) * 100)

        return close_one_position(symbol, percentage)
