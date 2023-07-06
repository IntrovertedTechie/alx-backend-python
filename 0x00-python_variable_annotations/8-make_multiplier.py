#!/usr/bin/env python3

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier: The float multiplier.

    Returns:
        A function that takes a float and returns the product of the float and multiplier.
    """
    def multiply(num: float) -> float:
        return num * multiplier

    return multiply
