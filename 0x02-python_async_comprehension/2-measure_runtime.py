#!/usr/bin/env python3

import asyncio
from time import time


async def async_comprehension() -> float:
    """
    Coroutine that performs some asynchronous computation.
    """
    await asyncio.sleep(1)
    return 1


async def measure_runtime() -> bool:
    """
    Coroutine that executes async_comprehension four times in parallel and checks if the runtime falls within the desired range.
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

    return end_time <= threshold


async def main() -> None:
    """
    Coroutine that calls measure_runtime and prints the result.
    """
    runtime_within_range = await measure_runtime()
    print(f"Runtime within range: {runtime_within_range}")


if __name__ == "__main__":
    asyncio.run(main())