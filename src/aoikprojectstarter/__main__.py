# coding: utf-8
"""
Program main module.

This module contains program main function.

This module is named ``__main__.py`` so that the program can be run via:
::

    python -m aoikprojectstarter
"""
from __future__ import absolute_import

# Standard-library imports
import os.path
import sys


def syspath_init():
    """
    Prepare `sys.path` so that program users do not need set up PYTHONPATH.

    :return: None.
    """
    # Get this file's directory path
    my_dir = os.path.dirname(os.path.abspath(__file__))

    # Remove some paths from `sys.path` to avoid unexpected import resolution.

    # For each path in the list
    for path in ['', '.', my_dir]:
        # If the path is in `sys.path`
        if path in sys.path:
            # Remove the path from `sys.path`
            sys.path.remove(path)

    # Get `src` directory path
    src_dir = os.path.dirname(my_dir)

    # If the `src` directory path is not in `sys.path`
    if src_dir not in sys.path:
        # Add the `src` directory to `sys.path`
        sys.path.insert(0, src_dir)


def check_deps():
    """
    Check whether dependency packages have been installed.

    Print hint message if a package is not installed.

    :return: True if all packages have been installed, otherwise False.
    """
    # Whether all dependency packages have been installed
    result = True

    #
    try:
        # Import package
        import json

        # Make linter happy
        json = json
    except ImportError:
        # Get message
        msg = 'Error: Package `json` is not installed.\n'

        # Print message
        sys.stderr.write(msg)

        # Set result be False
        result = False

    # Return whether all dependency packages have been installed
    return result


def main(args=None):
    """
    Program main function.

    This function does three things:

    - Prepare `sys.path` so that program users do not need set up PYTHONPATH.

    - Check whether dependency packages have been installed.

    - Call the mediator module that implements the program logic.

    :param args: Command line arguments list.

    :return: Exit code.
    """
    # Prepare `sys.path`
    syspath_init()

    # If not all dependency packages have been installed
    if not check_deps():
        # Return 9 to mean dependency missing
        return 9

    # If all dependency packages have been installed.

    # Import `main_wrap` function.
    # Notice can not use relative import in main module.
    from aoikprojectstarter.mediator import main_wrap

    # Call `main_wrap` function
    return main_wrap(args=args)


# If this module is the main module
if __name__ == '__main__':
    # Call `main` function
    sys.exit(main())
