#!/usr/bin/env python3
"""
Use async_generator function to
write a function async_comprehension.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an
    async generator and returns them as a list.
    """
    return [i async for i in async_generator()]
