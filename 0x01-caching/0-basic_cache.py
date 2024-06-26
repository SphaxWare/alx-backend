#!/usr/bin/python3
"""Basic cache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BaseCaching"""

    def put(self, key, item):
        """assign to the dict cach_data the
        'item' value for the 'key'"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return dict cach_data"""
        return self.cache_data.get(key, None)
