#!/usr/bin/env python3

import asyncio
from typing import List
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay (inclusive) seconds.
    Returns the randomly generated delay.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns `wait_random` n times with the specified max_delay.
    Returns the list of delays in ascending order.
    """
    delays: List[float] = []
    tasks: List[asyncio.Task] = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in tasks:
        delay = await task
        delays.append(delay)

    delays.sort()
    return delays
