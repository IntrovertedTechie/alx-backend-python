import asyncio
from typing import List, AsyncGenerator

async_generator: AsyncGenerator = __import__('0-async_generator').async_generator


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


asyncio.run(main())
