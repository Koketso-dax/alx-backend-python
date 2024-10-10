#!/usr/bin/env python3
""" multiplier module. """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ multiplier function. """
    def multiplier_function(x: float) -> float:
        """ multiplier function. """
        return x * multiplier
    return multiplier_function
