#!/usr/bin/env python3
"""LIFO Caching"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """FIFO caching"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key.
        """
        if key is None or item is None:
            return
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data[key] = item
                else:
                    first, _ = self.cache_data.popitem(last=True)
                    print("DISCARD: {}".format(first))
            self.cache_data[key] = item

    def get(self, key):
        """"
        Must return the value in
        self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
