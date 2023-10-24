#!/usr/bin/env python3
"""
Module contains index_range function
"""


def index_range(page: int, page_size: int):
    """
    Function returns a tuple of size two conating a
    start index amd an end index
    """
    if page <= 0 or page_size <= 0:
        return (0, 0)

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
