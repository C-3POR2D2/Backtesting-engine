from events_queue import EventQueue
from data.data_handler import DataHandler
from models.events import MarketDataEvent, OrderEvent, FillEvent
from strategy.strategy import Strategy
from engine.execution_handler import ExecutionHandler

import importlib
portfolios = importlib.import_module("portfolio tracker.portfolio_tracker")
pt = portfolios.PortfolioTracker

while DataHandler or EventQueue.is_empty()== False:
    event = None
    if EventQueue.is_empty == False:

        event = EventQueue.get()

        if event == MarketDataEvent: 
            market_event = Strategy(event)
        if event ==  OrderEvent:
           market_event = ExecutionHandler(event)
        if event == FillEvent(event)

    else:
        new_candle = DataHandler.send_market_data()
# while data has candles OR queue is not empty:
#     if queue is not empty:
#         get event
#         if MarketDataEvent → Strategy
#         if OrderEvent → ExecutionHandler
#         if FillEvent → PortfolioTracker
#     else:
#         ask DataHandler for next candle