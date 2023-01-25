#!/usr/bin/python
"""LFU caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """inherits BaseCaching"""
    data_freq = {}

    def __init__(self):
        super().__init__()

    def get_min_val_key(self):
        """get key with minimum value in dict"""
        if len(self.data_freq) == 0:
            return
        min_value = 0
        min_value_key = ""
        flag = True
        for k, v in self.data_freq.items():
            if flag:
                min_value = v
                min_value_key = k
                flag = False
            else:
                if v < min_value:
                    min_value_key = k
                    min_value = v
        return min_value_key

    def put(self, key, item):
        """inserts item in the cache and if the cache is
        full remove the first element"""
        if key and item:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    lfu_key = self.get_min_val_key()
                    print("DISCARD: {}".format(lfu_key))
                    del self.cache_data[lfu_key]
                    del self.data_freq[lfu_key]
                self.cache_data[key] = item
                self.data_freq[key] = 1
            else:
                self.cache_data[key] = item
                self.data_freq[key] += 1

    def get(self, key):
        """Retrieves item by key"""
        if key is not None and key in self.cache_data:
            self.data_freq[key] += 1
        return self.cache_data.get(key, None)
