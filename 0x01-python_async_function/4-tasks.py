#!/usr/bin/env python3
""" Multiple entry """

import asyncio
from typing import List

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Takes two integers n and max_delay and returns a list of delays using task_wait_random.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays


if __name__ == '__main__':
    n = 5
    max_delay = 9
    asyncio.run(task_wait_n(n, max_delay))
