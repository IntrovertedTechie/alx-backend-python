#!/usr/bin/env python3

"""
Module for an asynchronous function that measures the total runtime.
"""

import asyncio
import time


async def async_comprehension() -> float:
    """
    Coroutine that performs some asynchronous computation.
    """
    await asyncio.sleep(1)
    return 1


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel and measures the total runtime.
    """
    start_time = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time() - start_time
    return end_time


async def main() -> None:
    """
    Coroutine that calls measure_runtime and prints the result.
    """
    runtime = await measure_runtime()
    print(f"Total runtime: {runtime} seconds")


if __name__ == "__main__":
    asyncio.run(main())
