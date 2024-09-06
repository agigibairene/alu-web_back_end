#!/usr/bin/env python3
'''function sum_mixed_list which takes a list mxd_lst'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Return the sum of a list of union of integers and floats.
    '''
    return float(sum(mxd_lst))
