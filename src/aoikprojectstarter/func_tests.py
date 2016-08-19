# coding: utf-8
"""
Tests module.

This module contains tests for function `factorial`.
"""
from __future__ import absolute_import

# Standard-library imports
from unittest import TestCase

# First-party imports
from aoikprojectstarter.func import factorial


def test_factorial_0():
    """
    Test factorial of 0.

    :return: None.
    """
    assert factorial(0) == 1


def test_factorial_1():
    """
    Test factorial of 1.

    :return: None.
    """
    assert factorial(1) == 1


def test_factorial_2():
    """
    Test factorial of 2.

    :return: None.
    """
    assert factorial(2) == 2


def test_factorial_3():
    """
    Test factorial of 3.

    :return: None.
    """
    assert factorial(3) == 6


def test_factorial_4():
    """
    Test factorial of 4.

    :return: None.
    """
    assert factorial(4) == 24


class FactorialTests(TestCase):
    """
    Tests for function `factorial`.
    """

    def setUp(self):
        """
        Set-up function.

        :return: None.
        """

    def tearDown(self):
        """
        Tear-down function.

        :return: None.
        """

    def test_factorial_0(self):
        """
        Test factorial of 0.

        :return: None.
        """
        assert factorial(0) == 1

    def test_factorial_1(self):
        """
        Test factorial of 1.

        :return: None.
        """
        assert factorial(1) == 1

    def test_factorial_2(self):
        """
        Test factorial of 2.

        :return: None.
        """
        assert factorial(2) == 2

    def test_factorial_3(self):
        """
        Test factorial of 3.

        :return: None.
        """
        assert factorial(3) == 6

    def test_factorial_4(self):
        """
        Test factorial of 4.

        :return: None.
        """
        assert factorial(4) == 24
