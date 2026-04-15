from collections import defaultdict
class PortfolioTracker():
    def __init__(self, cash):
        self.cash = cash
        self.positions = defaultdict(int)
        self.last_prices = defaultdict(int)
        self.total_value = cash

    def on_fill_event(self, fillevent):
        if fillevent.orderside == 'buy':
            self.cash -= fillevent.fillprice * fillevent.numOfShares
            
            self.positions[fillevent.Ticker] += fillevent.numOfShares
            self.last_prices[fillevent.Ticker] = fillevent.fillprice
        else:
            self.cash +=fillevent.fillprice * fillevent.numOfShares

            self.positions[fillevent.Ticker] -= fillevent.numOfShares
            self.last_prices[fillevent.Ticker] = fillevent.fillprice

        self.total_value = self.cash + sum(quantity* self.last_prices[ticker]for ticker, quantity in self.positions.items()) 

    
