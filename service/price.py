from api.data.market import get_current_price
from api.trade.position import get_open_position

# todo: compare price every x mins

# todo: if price lower than bias place new order, if higher close certain order


# def get_entry_price():
#     with open('entry_price.txt', 'r') as f:
#         price = f.read().strip()
#     return price


def calculate_price(symbol, bias):
    position = get_open_position(symbol)
    diff = position.get('current_price') - position.get('avg_entry_price')

    # case: raised
    if diff > 0:
        if diff > bias:
            return 'B'

    # case: decreased
    if diff < 0:
        if diff < -bias:
            return 'S'

    return False


