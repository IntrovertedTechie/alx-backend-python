#!/usr/bin/env python3

"""
This module provides a function for converting a string.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string k as the first element.
    """
    return k, v ** 2
