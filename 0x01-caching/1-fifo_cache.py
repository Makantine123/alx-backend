#!/usr/bin/python3
"""FIFOCache Module"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache Class"""

    def __init__(self):
        """Initialisation of class"""
        super().__init__()

    def put(self, key, item):
        """Assigns the dictionary self.cache_data the key and its value"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_item = next(iter(self.cache_data))
            self.cache_data.pop(first_item)
            print(f"DISCARD: {first_item}")
        self.cache_data[key] = item

    def get(self, key):
        """Returns self.cache_data data for the key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
