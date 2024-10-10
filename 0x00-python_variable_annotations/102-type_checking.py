#!/usr/bin/env python3
""" mypy validation """
from typing import Tuple, List, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> List[Any]:
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple[int, ...] = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3)
