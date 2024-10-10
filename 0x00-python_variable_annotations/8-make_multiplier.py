#!/usr/bin/env python3
""" multiplier module. """


def make_multiplier(multiplier: float) -> callable:
    """ Returns a function that multiplies a float by multiplier. """
    def multiplier_function(x: float) -> float:
        """ Multiplies a float by multiplier. """
        return x * multiplier
    return multiplier_function
