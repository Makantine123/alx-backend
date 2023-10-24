#!/usr/bin/python3
"""MRUCache Module"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class"""

    def __init__(self):
        """Initialisation of class"""
        super().__init__()

    def put(self, key, item):
        """Assigns the dictionary self.cache_data the key and its value"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = list(self.cache_data.keys())[-1]
            self.cache_data.pop(mru_key)
            print(f"DISCARD: {mru_key}")
        self.cache_data[key] = item

    def get(self, key):
        """Returns self.cache_data data for the key"""
        if key is None or key not in self.cache_data:
            return None
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return item
