#!/usr/bin/python3
"""
Caching system with no limit
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Caching class Inherits from BaseCaching class
    Implements get and put methon of parent class
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
