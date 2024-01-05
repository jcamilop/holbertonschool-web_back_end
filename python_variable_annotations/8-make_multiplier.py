#!/usr/bin/env python3
""" Functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ type-annotated function make_multiplier, takes a float multiplier
        as argument and returns a function that multiplies a float by
        multiplier. """
    def fn(n: float):
        return n * multiplier
    return fn
