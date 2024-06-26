#!/usr/bin/env python3
"""FIFO Caching"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key.
        """
        if key is None and item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first, _ = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(first))
        self.cache_data[key] = item

    def get(self, key):
        """"
        Must return the value in
        self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
