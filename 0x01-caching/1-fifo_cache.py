#!/usr/bin/env python3
"""FIFO cache replacement property"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching"""

    def put(self, key, item):
        """Add item to cache"""
        if len(self.cache_data) == self.MAX_ITEMS:
            first_item = next(iter(self.cache_data))
            del self.cache_data[first_item]
            print("DISCARD: {}".format(first_item))

        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get item from cache"""
        return self.cache_data.get(key)
