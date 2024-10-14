#!/usr/bin/env/ python3
""" Spawns async function wait_random n
number of times and returns a list of
all the delays """
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Invoke wait_random n times. """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return (delays)
