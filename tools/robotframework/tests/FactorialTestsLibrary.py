# coding: utf-8
"""
Robot framework library module.
"""
from __future__ import absolute_import

# First-party imports
from aoikprojectstarter.func import factorial


class FactorialTestsLibrary(object):
    """
    Robot framework library class.
    """

    def __init__(self):
        """
        Constructor.

        :return: None.
        """
        # Stored result
        self._result = None

    def factorial(self, value):
        """
        Compute given value's factorial and store.

        :param value: Value for which to compute factorial.

        :return: Computed factorial.
        """
        # Compute given value's factorial and store
        self._result = factorial(value)

        # Return the computed factorial
        return self._result

    def result(self):
        """
        Get stored result.

        :return: Stored result.
        """
        # Return the stored result
        return self._result
