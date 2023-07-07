#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element from `lst` and its length.

    Args:
        lst: An iterable object containing sequences.

    Returns:
        A list of tuples where each tuple contains an element from `lst` and its length.
    """
    return [(i, len(i)) for i in lst]
