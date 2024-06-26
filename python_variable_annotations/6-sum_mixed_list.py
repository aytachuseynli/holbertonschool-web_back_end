#!/usr/bin/env python3

"""
Module: 6-sum_mixed_list
Contains:
    - sum_mixed_list: Returns the sum of a list of integers and floats
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of integers and floats."""
    return sum(mxd_lst)
