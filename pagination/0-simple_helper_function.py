#!/usr/bin/env python3
"""
Module for simple pagination helper function.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start and end indexes corresponding to the range
    of indexes to return in a list for a particular pagination.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
