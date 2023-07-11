#!/usr/bin/env python3

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather and measures the total runtime.
    """
    start = time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end = time() - start
    return end


async def main():
    """
    Coroutine that calls measure_runtime and awaits its result.
    """
    return await measure_runtime()


print(asyncio.run(main()))
