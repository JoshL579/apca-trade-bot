import requests
from config import apca_action_url
from api.util.http import get_headers


def get_open_position(symbol):
    res = requests.get(f'{apca_action_url}/v2/positions/{symbol}', headers=get_headers())
    return res.json()


def close_one_position(symbol, qty):
    res = requests.delete(f'{apca_action_url}/v2/positions/{symbol}?qty={qty}', headers=get_headers())
    return res.json()
