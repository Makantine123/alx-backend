#!/usr/bin/python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache Class
    """

    def __init__(self):
        """Initialisation of the class"""
        super().__init__()

    def put(self, key, item):
        """Assigns to dictionary self.cache_data the item value for the key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Returns self.cache_data for the linked key"""
        if key is None or key not in self.cache_data:
            return
        return self.cache_data[key]
