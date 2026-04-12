import pandas as pd 
import numpy as np
from models.events import MarketDataEvent

class DataHandler():
    def __init__(self, data, queue):
        self.data = data
        self.df = pd.DataFrame(self.data)
        self.queue = queue
        self.iterator = 0
   

    def check_data(self):
        return  self.iterator <= len(self.data) -1
        
    def send_market_data(self):
        if self.check_data():
                current_data =self.df.iloc[self.iterator]
                market_data= MarketDataEvent(current_data['timestamp'], current_data['volume'], current_data[ 'open'], current_data[ 'high'], current_data[ 'low'], current_data[ 'close'])
                self.queue.put(market_data)
                self.iterator +=1

        pass

