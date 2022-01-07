from time import sleep
from service.order import maintain_order
from datetime import datetime
from database.db_handler import init_db
from service.trading_hours import is_trading_hour


def maintain_loop(symbol):
    init_db()
    debugger_count = 0
    print('STARTED! LOOPING...')
    while True:
        if not is_trading_hour():
            sleep(30)
            continue
        maintain_order(symbol)
        sleep(10)
        debugger_count += 1
        if debugger_count > 1440:
            print(datetime.isoformat(datetime.now()), 'LOOPING...')
            debugger_count = 0
