#!/usr/bin/env python3
'''Write an asynchronous coroutine that takes in an integer argument'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''await for random delay between 0 and max_delay'''
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
