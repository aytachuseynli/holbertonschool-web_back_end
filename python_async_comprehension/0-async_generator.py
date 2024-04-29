#!/usr/bin/env python3

"""
Module: 0-async_generator
Contains:
    - async_generator:
    Asynchronous generator that yields random numbers
"""

import asyncio
import random


async def async_generator() -> float:
    """
    Asynchronous generator that yields random numbers.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
