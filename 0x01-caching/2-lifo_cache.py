#!/usr/bin/python3
"""LIFOCache Module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache Class"""

    def __init__(self):
        """Initialisation of class"""
        super().__init__()

    def put(self, key, item):
        """Assigns the dictionary self.cache_data the key and its value"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_item = self.cache_data.popitem()
            print(f"DISCARD: {last_item[0]}")
        self.cache_data[key] = item

    def get(self, key):
        """Returns self.cache_data data for the key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
