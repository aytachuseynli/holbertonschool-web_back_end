#!/usr/bin/env python3

"""
Module: 3-tasks
Contains:
    - task_wait_random: Returns an asyncio.Task
"""

import asyncio
from typing import Coroutine


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns an asyncio.Task."""
    return asyncio.create_task(wait_random(max_delay))
