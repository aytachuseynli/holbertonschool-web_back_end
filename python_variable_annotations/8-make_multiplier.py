#!/usr/bin/env python3

"""
Module: 8-make_multiplier
Contains:
    - make_multiplier: Returns a function
    that multiplies a float by a multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by a multiplier."""
    def multiplier_function(x: float) -> float:
        """Multiply a float by a multiplier."""
        return x * multiplier
    return multiplier_function
