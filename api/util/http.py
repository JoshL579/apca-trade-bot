from config import apca_api_key
from config import apca_api_secret


def get_headers():
    return {
        'APCA-API-KEY-ID': apca_api_key,
        'APCA-API-SECRET-KEY': apca_api_secret
    }
