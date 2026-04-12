import pandas as pd 
import numpy as np



class DataHandler():
    def __init__(self, data, queue):
        self.data = data
        self.queue = queue

    def check_data(self, queue):
        return self.queue.empty()
        
    def source_data(self):
        df = pd.Dataframe(self.data)
        # market_data= MarketDataEvent(df.loc[0])
        
        pass

    def next_candle(self):
        pass 
