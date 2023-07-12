#!/usr/bin/env python3

import asyncio
from time import time


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
    start_time = time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time() - start_time

    threshold = 10.0 + (10.0 * 0.1)  # Calculate the threshold (10 seconds + 10% overhead)
    if end_time > threshold:
        raise ValueError("Runtime exceeds the threshold")

    return end_time


async def main() -> None:
    """
    Coroutine that calls measure_runtime and prints the result.
    """
    try:
        runtime = await measure_runtime()
        print(f"Total runtime: {runtime} seconds")
    except ValueError as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    asyncio.run(main())
