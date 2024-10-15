#!/usr/bin/env python3
"""
Coroutene that loops 10x each time waiting
for 1 second then yielding a random number
between 0 and 10.
"""
from asyncio import sleep
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Loop 10x each time waiting for 1 second
    then yield a random number between 0 and 10.
    """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
