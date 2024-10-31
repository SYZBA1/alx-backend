#!/usr/bin/env python3
"""
LRU cache replacement property
cache_info is arranged in reverse order
most recently used is put at the end of
the list, least recently used is at the
beginning of the list
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU caching"""
    cache_info = []  # holds and arranges cache items based on recently used

    def put(self, key, item):
        """Add item to cache"""
        self.cache_data[key] = item

        # check if value is already in cache
        if key not in self.cache_info:
            self.cache_info.append(key)

        if len(self.cache_info) > self.MAX_ITEMS:
            print("Discard: {}".format(self.cache_info[0]))
            self.cache_info.pop(0)  # remove least recently used item

            # if key is not in cache_info remove from cache_data
            for val in self.cache_data:
                if val not in self.cache_info:
                    del self.cache_data[val]
                    break

    def get(self, key):
        """get item from cache"""
        data = self.cache_data.get(key)

        # put recently used item at top of cache
        if data is not None:
            self.cache_info.remove(key)
            self.cache_info.append(key)

        return data
