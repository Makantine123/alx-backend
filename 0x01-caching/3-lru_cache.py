#!/usr/bin/python3
"""LRUCache Module"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache Class"""

    def __init__(self):
        """Initialisation of class"""
        super().__init__()

    def put(self, key, item):
        """Assigns the dictionary self.cache_data the key and its value"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_items = list(self.cache_data.keys())
            discarded_key = lru_items[0]
            self.cache_data.pop(discarded_key)
            print(f"DISCARD: {discarded_key}")
        self.cache_data[key] = item

    def get(self, key):
        """Returns self.cache_data data for the key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
