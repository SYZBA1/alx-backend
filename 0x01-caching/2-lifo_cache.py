#!/usr/bin/env python3
"""LIFO cache replacement property"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching"""

    def put(self, key, item):
        """Add item to cache"""
        if len(self.cache_data) == self.MAX_ITEMS:
            last_item = list(self.cache_data.keys())[self.MAX_ITEMS - 1]
            del self.cache_data[last_item]
            print("DISCARD: {}".format(last_item))

        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get item from cache"""
        return self.cache_data.get(key)
