#!/usr/bin/env python3

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string k as the first element
    and the square of the int/float v as the second element.

    Args:
        k: The input string.
        v: The input int or float.

    Returns:
        A tuple with the string k and the square of v as a float.
    """
    return k, v ** 2
