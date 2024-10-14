#!/usr/bin/env python3
""" Calculate the total exec time for wait_n() """

from asyncio import run
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure the total exec time for wait_n() """
    start = perf_counter()
    run(wait_n(n, max_delay))
    end = perf_counter()
    total_time = end - start
    return total_time / n
