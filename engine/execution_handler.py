
from models.events import FillEvent

class ExecutionHandler():
    def __init__(self, order_event, queue):
        self.order_event = order_event   
        self.queue = queue  

    
    def fill(self, order_event):
        fill_price, signal_price, direction = 0
        fill_price = signal_price + (self.slippage_factor * direction)
        fill_event = FillEvent(order_event.timestamp, fill_price, order_event.Ticker, order_event.numofshares, order_event.side)