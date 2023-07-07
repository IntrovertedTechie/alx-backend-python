#!/usr/bin/env python3
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns the value associated with the given key in the dictionary `dct`.
    If the key is not found, returns the default value.

    Args:
        dct: A mapping object (e.g., dictionary).
        key: The key to search for in `dct`.
        default: The default value to return if the key is not found (default: None).

    Returns:
        The value associated with the key if found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
