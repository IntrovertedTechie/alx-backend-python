#!/usr/bin/env python3

"""
Module for an asynchronous generator function that yields a
random float between 0 and 10 after a one-second delay for a total of
10 iterations.
"""

import asyncio
import random
from typing import AsyncGenerator, List

async_generator: AsyncGenerator[float, None] = \
    __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers.

    Returns:
        List[float]: List of random float numbers.
    """
    return [num async for num in async_generator()]


async def main() -> None:
    """
    Coroutine that calls async_comprehension and awaits its result.
    """
    print(await async_comprehension())


if __name__ == "__main__":
    asyncio.run(main())