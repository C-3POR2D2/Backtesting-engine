import time 

class Event():
    def __init__(self, timestamp):
        self.timestamp = timestamp


class MarketDataEvent(Event):
    def __init__(self, timestamp, volume, open, high, low, close):
        super().__init__(timestamp)
        self.volume = volume 
        self.open = open 
        self.close = close
        self.high = high 
        self.low = low

class OrderEvent(Event):
    def __init__(self, timestamp, price, id, order_type, orderside, ticker, num_of_shares):
        super().__init__(timestamp)
        self.id = id
        self.price = price
        self.ordertype = order_type
        self.orderside = orderside
        self.ticker = ticker
        self.num_of_shares = num_of_shares
    
class FillEvent(Event):
    def __init__(self, timestamp, fill_price, Ticker, num_of_shares, order_side):
        super().__init__(timestamp)
        self.Ticker = Ticker
        self.fillprice = fill_price
        self.numOfShares = num_of_shares
        self.orderside= order_side
        
