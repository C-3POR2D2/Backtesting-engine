from queue import Queue 
from data.data_handler import DataHandler
 

class EventQueue():
    def __init__(self):
        self.__queue = Queue()

    def put(self, event):
        self.__queue.put(event)

    def get(self):
        return self.__queue.get()
    
    def is_empty(self):
        return self.__queue.empty() 
    
