#!/usr/bin/env python3

"""
This module provides a function for zooming an array.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Returns a zoomed-in list by repeating each element by the factor.

    Args:
        lst (Tuple[int, ...]): The input tuple of integers.
        factor (int): The zoom factor. Defaults to 2.

    Returns:
        List[int]: The zoomed-in list.
    """
    zoomed_in: List[int] = [
        item
        for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
