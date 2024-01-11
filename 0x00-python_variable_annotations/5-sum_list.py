#!/usr/bin/env python3
"""
Module: Provides a function for summing list of float values.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function sums a list of float and returns the result.

    Parameters:
    input_list: List[float]: The list of float values.

    Returns:
    float: sum of list of floats.
    """
    return sum(input_list)
