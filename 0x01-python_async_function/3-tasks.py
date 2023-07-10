#!/usr/bin/env python3

import asyncio
from typing import Callable

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task.
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    loop = asyncio.get_event_loop()
    task: asyncio.Task = loop.create_task(wait_random(max_delay))
    return task
