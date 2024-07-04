#!/usr/bin/env python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function to multiply a float"""
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
