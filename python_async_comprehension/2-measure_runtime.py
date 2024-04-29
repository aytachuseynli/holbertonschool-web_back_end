#!/usr/bin/env python3

"""
Module: 2-measure_runtime
Contains:
    - measure_runtime: Measures the total runtime
    for executing async_comprehension four times in parallel
"""

import asyncio
from typing import List
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime for executing
    async_comprehension four times in parallel.
    """
    start_time = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time()
    return end_time - start_time
