import requests
from config import apca_action_url
from api.util.http import get_headers


def place_one_order(symbol):
    payload = {
        'symbol': symbol,
        'notional': 10,
        'side': 'buy',
        'type': 'market',
        'time_in_force': 'day',
    }
    res = requests.post(f'{apca_action_url}/v2/orders', json=payload, headers=get_headers())
    return res.json()


def get_open_position(symbol):
    res = requests.get(f'{apca_action_url}/v2/positions/{symbol}')
    return res.json()


def close_one_position(symbol, percentage):
    res = requests.delete(f'{apca_action_url}/v2/positions/{symbol}?percentage={percentage}')
    return res.json()
