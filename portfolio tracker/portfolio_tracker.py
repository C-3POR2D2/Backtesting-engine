from collections import defaultdict

class PortfolioTracker():
    def __init__(self, cash):
        self.cash = cash
        self.positions = defaultdict(int)
        self.last_prices = defaultdict(int)
        self.total_value = cash

    def on_fill_event(self, fillevent):
        if fillevent.orderside == 'buy':
            self.cash -= fillevent.fill_price * fillevent.num_of_shares
            
            self.positions[fillevent.ticker] += fillevent.num_of_shares
            self.last_prices[fillevent.ticker] = fillevent.fill_price
        else:
            self.cash +=fillevent.fill_price * fillevent.num_of_shares

            self.positions[fillevent.ticker] -= fillevent.num_of_shares
            self.last_prices[fillevent.ticker] = fillevent.fill_price

        self.total_value = self.cash + sum(quantity* self.last_prices[ticker]for ticker, quantity in self.positions.items()) 

    
