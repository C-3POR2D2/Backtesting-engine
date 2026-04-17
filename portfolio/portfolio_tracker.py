from collections import defaultdict
class PortfolioTracker():
    def __init__(self, cash):
        self.cash = cash
        self.positions = defaultdict(int)
        self.last_prices = defaultdict(int)
        self.total_value = cash

    def on_fill_event(self, fillevent):
        if fillevent.orderside == 'buy' and self.cash >=(fillevent.fillprice * fillevent.numOfShares):
            self.cash -= fillevent.fillprice * fillevent.numOfShares
            
            self.positions[fillevent.Ticker] += fillevent.numOfShares
            self.last_prices[fillevent.Ticker] = fillevent.fillprice

        elif fillevent.orderside == 'buy' and self.cash <= (fillevent.fillprice * fillevent.numOfShares):
            print(f"Order Rejected:\n not enough fund to execute\n available cash:{self.cash}, order requested:{fillevent.fillprice *fillevent.numOfShares} ")

        elif fillevent.orderside == 'sell' and self.positions[fillevent.Ticker] == 0:
                       print(f"Order Rejected: no shares available to sell")
          
        else:
            self.cash +=fillevent.fillprice * fillevent.numOfShares
            if self.positions[fillevent.Ticker] >= fillevent.numOfShares:
                self.positions[fillevent.Ticker] -= fillevent.numOfShares
                self.last_prices[fillevent.Ticker] = fillevent.fillprice
            else:
                 print(f"{self.positions[fillevent.Ticker]}Sell Order Rejected: Not enough shares to sell")

        self.total_value = self.cash + sum(quantity* self.last_prices[ticker]for ticker, quantity in self.positions.items()) 
        print(f"FILL: {fillevent.orderside} {fillevent.numOfShares} {fillevent.Ticker} @ {fillevent.fillprice}")
        print(f"Cash: {self.cash:.2f} | Total Value: {self.total_value:.2f}")
    
