#!/usr/bin/env python3
'''Write a coroutine called async_generator that takes no arguments'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' yields or returns a random number between 0 and 10'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
