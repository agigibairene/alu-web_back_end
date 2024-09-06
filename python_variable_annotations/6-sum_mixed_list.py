#!/usr/bin/env python3
from typing import List, Union

'''function sum_mixed_list which takes a list mxd_lst'''
def sum_mixed_list(input_list: List[Union[float, int]]) -> float:
    """returns their sum as a float"""
    return float(sum(input_list))
