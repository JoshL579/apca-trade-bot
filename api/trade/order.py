import requests
from config import apca_action_url
from api.util.http import get_headers


def place_one_order(symbol, amount):
    payload = {
        'symbol': symbol,
        'notional': amount,
        'side': 'buy',
        'type': 'market',
        'time_in_force': 'day',
    }
    res = requests.post(f'{apca_action_url}/v2/orders', json=payload, headers=get_headers())
    return res.json()


def close_one_order(order_id):
    res = requests.delete(f'{apca_action_url}/v2/orders/{order_id}', headers=get_headers())
    return res.json()


def get_orders():
    res = requests.get(f'{apca_action_url}/v2/orders', headers=get_headers())
    return res.json()
