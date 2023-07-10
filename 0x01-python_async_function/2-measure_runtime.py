#!/usr/bin/env python3
""" Runtime Measurement """

from time import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    returns execution time of async function
    """
    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time() - start
    return end / n
