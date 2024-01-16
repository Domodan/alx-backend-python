#!/usr/bin/env python3
"""
Module: Asynchronous generator function
"""
from asyncio import sleep
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator function that yields a random float between 0 and 10
    after a one second delay for a total of 10 iterations.

    Returns:
        Generator: Asynchronous generator object that can be used in an
        awaitable context.
    """
    for _ in range(10):
        await sleep(1)
        yield 10 * random()
