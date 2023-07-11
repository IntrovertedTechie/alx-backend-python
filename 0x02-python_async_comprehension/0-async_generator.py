#!/usr/bin/env python3
"""
Module for an asynchronous generator function that yields a
random float between 0 and 10 after a one-second delay for a total of
10 iterations.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator function that yields a random float between 0 and 10
    after a one-second delay for a total of 10 iterations.

    Yields:
        float: Random float value between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def print_yielded_values():
    """
    Coroutine that prints the values yielded by the async_generator.
    """
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)


if __name__ == "__main__":
    asyncio.run(print_yielded_values())