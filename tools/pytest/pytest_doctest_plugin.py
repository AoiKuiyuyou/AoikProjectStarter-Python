# coding: utf-8
"""
Pytest plugin that filters collected test items to only keep `Doctest` items.
"""
from __future__ import absolute_import


def pytest_collection_modifyitems(items, config):
    """
    Filter given test items to only keep `Doctest` items.

    This is a hook function called by `pytest`.

    :param items: Test items list.

    :param config: Config object.

    :return: None.
    """
    # Accepted test items list
    accepted_item_s = []

    # For each test item
    for item in items:
        # If the test item is `Doctest` instance
        if 'Doctest' in item.__class__.__name__:
            # Add the test item to the accepted test items list
            accepted_item_s.append(item)

    # Set given test items list to contain only the accepted test items
    items[:] = accepted_item_s
