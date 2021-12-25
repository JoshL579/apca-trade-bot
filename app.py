from service.loop import maintain_loop
from config import watching_symbol

if __name__ == '__main__':
    maintain_loop(watching_symbol)
