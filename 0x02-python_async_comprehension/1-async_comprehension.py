#!/usr/bin/env python3

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random number.
    """
    return [num async for num in async_generator()]


async def main():
    """
    Coroutine that calls async_comprehension and awaits its result.
    """
    print(await async_comprehension())


asyncio.run(main())
