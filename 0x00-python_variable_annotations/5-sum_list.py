#!/usr/bin/env python3
""" Complex type annotations list of floats """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ returns the sum of a list of floats """
    return sum(input_list)
