from abc import ABC, abstractmethod
from models.events import MarketDataEvent, OrderEvent
import uuid
class Strategy(ABC):
    def __init__(self, order_queue):
        self.order_queue = order_queue
        self.current_candle = None

    @abstractmethod
    def on_market_data_event(self, event):
        pass



class MovingAverageStratgey(Strategy):
   
    def __init__(self, order_queue, ticker, num_of_shares):
        super().__init__(order_queue)
        self.closing_price = []
        self.order_queue = order_queue    
        self.ticker = ticker
        self.quantity = num_of_shares

    def on_market_data_event(self, event):
        self.current_candle = event
        self.closing_price.append(event.close)

        
        if len(self.closing_price) >= 20:
            average_price = sum(self.closing_price)/ 20
            
            if(event.close > average_price):
                 order = OrderEvent(event.timestamp, event.close, uuid.uuid4(),"MarketOrder", "buy", self.ticker, self.quantity)
                 self.order_queue.put(order)
            else:
                order = OrderEvent(event.timestamp, event.close, uuid.uuid4(), "MarketOrder", "sell", self.ticker, self.quantity)
                self.order_queue.put(order)