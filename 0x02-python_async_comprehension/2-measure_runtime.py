#!/usr/bin/env python3
"""
Module: Asynchronous function for measuring the runtime of running 4 instances
    of the async_comprehension function
"""
from asyncio import gather
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Asynchronous function that measures and returns the runtime of
    running 4 instances of the async_comprehension function.

    Returns:
        float: The runtime of the async_comprehension function in seconds.
    """
    start_time = time.time()
    await gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
