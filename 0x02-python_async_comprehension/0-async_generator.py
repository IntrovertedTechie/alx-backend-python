import asyncio
import random
from typing import AsyncGenerator, List


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields a random number between 0 and 10
    after waiting for 1 second in each iteration, for a total of 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def print_yielded_values():
    result: List[float] = []
    async for i in async_generator():
        result.append(i)
    print(result)


asyncio.run(print_yielded_values())