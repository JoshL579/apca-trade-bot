import requests
from api.util.http import get_headers
from config import apca_data_url, apca_action_url


def get_last_trade(symbol):
    res = requests.get(f'{apca_data_url}/v2/stocks/{symbol}/trades/latest', headers=get_headers())
    return res.json()


def get_current_price(symbol):
    return get_last_trade(symbol).get('trade').get('p')


def get_positions():
    res = requests.get(f'{apca_action_url}/v2/positions', headers=get_headers())
    return res.json()


def get_assets():
    assets = requests.get(f'{apca_action_url}/v2/assets', headers=get_headers())
    return assets.json()

