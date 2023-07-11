#!/usr/bin/env python3

"""
Module for an asynchronous generator function that yields random float values.
"""

import asyncio
import random
from typing import AsyncGenerator, List


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator function that yields a random float between 0 and 10.

    Yields:
        float: Random float value between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def print_yielded_values() -> None:
    """
    Coroutine that prints the values yielded by the async_generator.
    """
    result: List[float] = []
    async for i in async_generator():
        result.append(i)
    print(result)


async def main() -> None:
    """
    Coroutine that calls print_yielded_values and awaits its result.
    """
    await print_yielded_values()


if __name__ == "__main__":
    asyncio.run(main())
