from datetime import datetime
from config import tradingPeriod


def is_trading_hour():
    start = datetime.strptime(tradingPeriod[0], '%H:%M').time()
    end = datetime.strptime(tradingPeriod[1], '%H:%M').time()
    now = datetime.now().time()
    return start < now < end
