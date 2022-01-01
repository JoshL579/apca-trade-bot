from service.price import calculate_price
from api.trade.order import place_one_order, get_orders
from api.trade.position import close_one_position, get_open_position
from config import bias_to_place_new_order
from datetime import datetime
from database.db_handler import update_entry


def maintain_order(symbol):
    # already have unfulfilled order waiting for process
    if len(get_orders()) > 0:
        print(get_orders())
        return True

    calculation = calculate_price(symbol, bias_to_place_new_order)

    if not calculation:
        return True

    if calculation['direction'] == 'L':
        print(datetime.isoformat(datetime.now()), 'Increase One:', calculation['amount'])
        res = place_one_order(symbol, calculation['amount'])
        print(res)
        return update_entry(calculation['price'])

    if calculation['direction'] == 'S':
        print(datetime.isoformat(datetime.now()), 'Reduced One:', calculation['shares'])
        res = close_one_position(symbol, calculation['shares'])
        print(res)
        return update_entry(calculation['price'])

    return False
