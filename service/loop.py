from time import sleep
from service.order import maintain_order


def maintain_loop(symbol):
    while True:
        maintain_order(symbol)
        sleep(60)