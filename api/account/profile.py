import requests
from config import apca_action_url
from api.util.http import get_headers


def get_portfolio_history():
    res = requests.get(f'{apca_action_url}/v2/account/portfolio/history', headers=get_headers())
    return res.json()
