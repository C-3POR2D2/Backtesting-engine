
from models.events import FillEvent

class ExecutionHandler():
    def __init__(self, queue, slippage_factor): 
        self.queue = queue  
        self.slippage_factor = slippage_factor
   
    def fill(self, order_event):
        fill_price= 0
        direction = 0
        if (order_event.orderside == "buy"):
            direction = 1
        else:
            direction = -1

        fill_price = order_event.price + (self.slippage_factor * direction)
        fill_event = FillEvent(order_event.timestamp, fill_price, order_event.ticker, order_event.num_of_shares, order_event.orderside)
        self.queue.put(fill_event)