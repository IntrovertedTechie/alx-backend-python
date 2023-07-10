#!/usr/bin/env python3

import asyncio
from typing import List
import random


async def wait_random(max_delay: float = 10) -> float:
    """
    Asynchronous coroutine that returns a random delay.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: float) -> List[float]:
    """
    Asynchronous coroutine that spawns multiple wait_random tasks and returns a list of delays.
    """
    delays: List[float] = []
    tasks: List[asyncio.Task[float]] = []

    for _ in range(n):
        task: asyncio.Task[float] = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in tasks:
        delay: float = await task
        delays.append(delay)

    delays.sort()
    return delays
