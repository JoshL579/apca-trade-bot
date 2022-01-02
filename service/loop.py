from time import sleep
from service.order import maintain_order
from datetime import datetime
from database.db_handler import init_db


def maintain_loop(symbol):
    init_db()
    debugger_count = 0
    print('STARTED! LOOPING...')
    while True:
        maintain_order(symbol)
        sleep(30)
        debugger_count += 1
        if debugger_count > 1440:
            print(datetime.isoformat(datetime.now()), 'LOOPING...')
            debugger_count = 0
