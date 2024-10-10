#!/usr/bin/env python3
""" To kv tuple function """
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ To kv tuple function """
    return (k, v ** 2)
