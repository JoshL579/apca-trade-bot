from time import sleep
from service.order import maintain_order
from datetime import datetime


def maintain_loop(symbol):
    debugger_count = 0
    print('STARTED! LOOPING...')
    while True:
        maintain_order(symbol)
        sleep(60)
        debugger_count += 1
        if debugger_count > 1440:
            print(datetime.isoformat(datetime.now()), 'LOOPING...')
            debugger_count = 0
