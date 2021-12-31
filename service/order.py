from service.price import calculate_price
from api.trade.order import place_one_order, get_orders
from api.trade.position import close_one_position, get_open_position
from config import bias_to_place_new_order


def maintain_order(symbol):
    # already have unfulfilled order waiting for process
    if len(get_orders()) > 0:
        print(get_orders())
        return True

    calculation = calculate_price(symbol, bias_to_place_new_order)

    if not calculation:
        return True

    if calculation.direction == 'L':
        print('Increase One:', calculation.amount)
        return place_one_order(symbol, calculation.amount)

    if calculation.direction == 'S':
        # todo: change amount to percentage or quantity
        print('Reduced One:', calculation.amount)
        return close_one_position(symbol, calculation.amount)

    return False
