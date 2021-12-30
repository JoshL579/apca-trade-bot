import os

apca_action_url = 'https://paper-api.alpaca.markets'
apca_data_url = 'https://data.alpaca.markets'
apca_api_key = os.getenv('APCA_API_KEY')
apca_api_secret = os.getenv('APCA_API_KEY_SECRET')

bias_to_place_new_order = 2
price_range = (380, 450)
max_orders = 35

watching_symbol = 'QQQ'

database_uri = "sqlite:///price.sqlite"
