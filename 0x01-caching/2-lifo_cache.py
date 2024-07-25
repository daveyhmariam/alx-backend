#!/usr/bin/python3
"""
Caching system with FIFO algorithm
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    FIFO Caching class Inherits from BaseCaching class
    Implements get and put methon of parent class
    """
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:
            if key in self.queue:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                print(f"DISCARD: {self.queue[-1]}")
                del self.cache_data[self.queue[-1]]
                self.queue.pop(-1)
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
