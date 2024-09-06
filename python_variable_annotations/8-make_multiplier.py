#!/usr/bin/env python3
''' function make_multiplier that takes a float multiplier as argument'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns a multiplier function.'''
    return lambda x: x * multiplier
