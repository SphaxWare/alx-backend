#!/usr/bin/env python3
"""LRU Caching"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU caching"""
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
                    lru, _ = self.cache_data.popitem(True)
                    print("DISCARD: {}".format(lru))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """"
        Must return the value in
        self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
