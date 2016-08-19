# coding: utf-8
"""
Function module.

This module contains function `factorial`.
"""
from __future__ import absolute_import


def factorial(value):
    """
    Compute factorial of given value.

    :param value: A non-negative integer.

    :return: Factorial of given value.

    >>> factorial(0)
    1

    >>> factorial(1)
    1

    >>> factorial(2)
    2

    >>> factorial(3)
    6

    >>> factorial(4)
    24
    """
    # If given value is 0 or 1
    if (value == 0) or (value == 1):
        # Return 1
        return 1

    # If given value is not 0 or 1
    else:
        # Return given value multiplied by factorial of previous value
        return value * factorial(value - 1)
