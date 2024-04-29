#!/usr/bin/env python3

"""
Module: 7-to_kv
Contains:
    - to_kv: Returns a tuple containing a string
    and the square of an int or float
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple containing a string k and
    the square of an int or float v.
    """
    return (k, v ** 2)
