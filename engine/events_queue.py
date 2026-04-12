from queue import Queue 

class EventQueue():
    def __init__(self):
        self.__queue = Queue()

    def put(self, event):
        self.__queue.put(event)

    def get(self):
        return self.__queue.get()
    
    def is_empty(self):
        return self.__queue.empty() 
    

# while (EventQueue.is_empty(Queue)== False OR /data has candels):
#     if (queue.isnotempty):
#         get the queue item 
#             if item is order:
#                 apply the strategy 
#             else:
#                 apply the according one 
#      else:
            # ask DataHandler for next candle
            # if DataHandler has data:
            #     DataHandler puts MarketDataEvent into queue
            # else:
            #     stop
                    