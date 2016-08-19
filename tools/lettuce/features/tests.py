# coding: utf-8
"""
Lettuce tests module.
"""
from __future__ import absolute_import

# Third-party imports
from lettuce import step

# First-party imports
from aoikprojectstarter.func import factorial


@step(r'Factorial of (\d+) is (\d+)')
def factorial_of_x_is_y(step_obj, value, result):
    """
    Test given value's factorial is given result.

    :param step_obj: Step object.

    :param value: Value for which to compute factorial.

    :param result: Expected result.

    :return: None.
    """
    # Assert given value's factorial is given result
    assert factorial(int(value)) == int(result)
