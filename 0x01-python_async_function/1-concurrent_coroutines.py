#!/usr/bin/env python3

import asyncio
from typing import List
import random


async def wait_random(max_delay: float = 10) -> float:
    """
    Asynchronous coroutine.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return  
async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine.
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
