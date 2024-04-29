#!/usr/bin/env python3

"""
Module: 9-element_length
Contains:
    - element_length: Returns a list of tuples containing elements from lst
                      and their lengths
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing elements
    from lst and their lengths.
    """
    return [(i, len(i)) for i in lst]
