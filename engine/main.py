from engine.events_queue import EventQueue
from data.data_handler import DataHandler
from models.events import MarketDataEvent, OrderEvent, FillEvent
from strategy.strategy import Strategy
from engine.execution_handler import ExecutionHandler
from portfolio.portfolio_tracker import PortfolioTracker




class Engine():
    def __init__(self, data_handler, queue, strategy, execution_hander, portfolio_tracker):
        self.data_handler = data_handler
        self.queue = queue
        self.strategy = strategy
        self.execution_handler = execution_hander
        self.portfolio_tracker = portfolio_tracker
 

    def run(self):


        while self.data_handler.check_data() or self.queue.is_empty() == False:
            event = None
            if self.queue.is_empty() == False:

                event = self.queue.get()

                if isinstance(event, MarketDataEvent): 
                    market_event = self.strategy.on_market_data_event(event)
                if isinstance(event, OrderEvent):
                    market_event = self.execution_handler.fill(event)
                if isinstance(event, FillEvent):
                    market_event = self.portfolio_tracker.on_fill_event(event)
            else:
                new_candle = self.data_handler.send_market_data()

        # while data has candles OR queue is not empty:
        #     if queue is not empty:
        #         get event
        #         if MarketDataEvent → Strategy
        #         if OrderEvent → ExecutionHandler
        #         if FillEvent → PortfolioTracker
        #     else:
        #         ask DataHandler for next candle
