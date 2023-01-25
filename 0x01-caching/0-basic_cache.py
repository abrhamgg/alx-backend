#!/usr/bin/env python3
"""basic cache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """basic caching that inherits from class Basic Caching"""
    def put(self, key, item):
        """Must assign to the dictionary self.cache_data
        the item value for the key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves item by key"""
        return self.cache_data.get(key, None)
