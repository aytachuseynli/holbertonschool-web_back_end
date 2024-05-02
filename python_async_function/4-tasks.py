#!/usr/bin/env python3

"""
Module: 4-tasks
Contains:
    - task_wait_n: Returns a list of asyncio.Tasks
"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of asyncio.Tasks."""
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*delays)