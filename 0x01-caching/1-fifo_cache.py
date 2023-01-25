#!/usr/bin/python
"""FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """inherits BaseCaching"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """inserts item in the cache and if the cache is
        full remove the first element"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                for k, v in self.cache_data.items():
                    print("DISCARD: {}".format(k))
                    del self.cache_data[k]
                    break

    def get(self, key):
        """Retrieves item by key"""
        return self.cache_data.get(key, None)
