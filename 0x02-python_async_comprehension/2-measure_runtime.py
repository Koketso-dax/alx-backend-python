#!/usr/bin/env python3
"""Measures async_comprehension runtime."""
from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure runtime for tasks to complete.
    NB: The runtime is approximately equal
    to the total_delay (~10) + the time required
    to run and aggregate the tasks (a few milli sec)
    """
    start = time()
    tasks = [async_comprehension() for i in range(4)]
    await gather(*tasks)
    end = time()
    return (end - start)
