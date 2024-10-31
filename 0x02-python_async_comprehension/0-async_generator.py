#!/usr/bin/env python3
"""
Coroutene that loops 10x each time waiting
for 1 second then yielding a random number
between 0 and 10.
NB: the new  typing for this function shoudl be
AsyncGenerator[float, None]
"""
from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]: # type: ignore
    """
    Loop 10x each time waiting for 1 second
    then yield a random number between 0 and 10.
    """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
