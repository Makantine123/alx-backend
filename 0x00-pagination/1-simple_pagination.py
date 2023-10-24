#!/usr/bin/env python3
"""
Module contains Server class
"""

import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple:
        """
        Function returns a tuple of size two conating a
        start index amd an end index
        """
        if page <= 0 or page_size <= 0:
            return (0, 0)

        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Takes two integer arguments
        """
        assert isinstance(page, int) and isinstance(
            page_size, int) and page > 0 and page_size > 0

        data_set = self.dataset()
        total_pages = math.ceil(len(data_set) / page_size)

        if page > total_pages:
            return []

        start, end = self.index_range(page, page_size)
        return data_set[start:end]
