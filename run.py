from engine.events_queue import EventQueue
from data.data_handler import DataHandler
from models.events import MarketDataEvent, OrderEvent, FillEvent
from strategy.strategy import Strategy
from engine.execution_handler import ExecutionHandler
from portfolio.portfolio_tracker import PortfolioTracker



data = [
    {"timestamp": "2024-01-01 09:30:00", "open": 150.0, "high": 152.0, "low": 149.0, "close": 151.0, "volume": 1000},
    {"timestamp": "2024-01-01 09:31:00", "open": 151.0, "high": 153.0, "low": 150.0, "close": 152.0, "volume": 1200},
    {"timestamp": "2024-01-01 09:32:00", "open": 152.0, "high": 154.0, "low": 151.0, "close": 153.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 153.0, "high": 120.0, "low": 151.0, "close": 154.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 154.0, "high": 110.0, "low": 151.0, "close": 155.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 155.0, "high": 150.0, "low": 151.0, "close": 156.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 156.0, "high": 160.0, "low": 151.0, "close": 155.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 157.0, "high": 163.0, "low": 151.0, "close": 153.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 158.0, "high": 163.0, "low": 151.0, "close": 157.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 157.0, "high": 167.0, "low": 151.0, "close": 156.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 156.0, "high": 131.0, "low": 151.0, "close": 158.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 156.0, "high": 135.0, "low": 151.0, "close": 161.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 157.0, "high": 163.0, "low": 151.0, "close": 166.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 157.0, "high": 158.0, "low": 151.0, "close": 163.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 153.0, "high": 156.0, "low": 151.0, "close": 162.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 156.0, "high": 153.0, "low": 151.0, "close": 161.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 156.0, "high": 156.0, "low": 151.0, "close": 159.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 156.0, "high": 153.0, "low": 151.0, "close": 161.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 156.0, "high": 156.0, "low": 151.0, "close": 159.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 156.0, "high": 153.0, "low": 151.0, "close": 161.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 156.0, "high": 156.0, "low": 151.0, "close": 159.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 156.0, "high": 153.0, "low": 151.0, "close": 161.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 156.0, "high": 156.0, "low": 151.0, "close": 159.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 157.0, "high": 158.0, "low": 151.0, "close": 163.0, "volume": 900},
    {"timestamp": "2024-01-01 09:32:00", "open": 153.0, "high": 156.0, "low": 151.0, "close": 162.0, "volume": 900},

]


