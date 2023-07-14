#!/usr/bin/env python3
"""
Module for an asynchronous function that measures the total runtime.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension 4X in parallel
     """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
async_comprehension(), async_comprehension())
    return time.perf_counter() - start_time