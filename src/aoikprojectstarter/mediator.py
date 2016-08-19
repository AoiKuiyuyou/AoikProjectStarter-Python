# coding: utf-8
#
"""
Mediator module.

This module puts together other modules to implement the program logic.
"""
from __future__ import absolute_import

# Standard-library imports
from argparse import ArgumentParser
from argparse import ArgumentTypeError
import sys
import traceback

# Local imports
from .func import factorial


def int_ge0(text):
    """
    Convert given text to an integer greater than or equal to 0.

    Used by `ArgumentParser`.

    :param text: Text to convert to integer.

    :return: An integer greater than or equal to 0.
    """
    try:
        # Convert to int
        int_value = int(text)

        # Ensure greater than or equal to 0
        assert int_value >= 0
    except Exception:
        # Raise an exception to notify ArgumentParser
        raise ArgumentTypeError(
            '`%s` is not an integer greater than or equal to 0.' % text)

    # Return the valid value
    return int_value


def get_cmdargs_parser():
    """
    Create command line arguments parser.

    :return: Command line arguments parser, an `ArgumentParser` instance.
    """
    # Create command line arguments parser
    parser = ArgumentParser(prog='aoikprojectstarter')

    # Add argument
    parser.add_argument(
        'number',
        type=int_ge0,
        default=None,
        metavar='NUMBER',
        help='the number for which to compute factorial.',
    )

    # Return the command line arguments parser
    return parser


def main_core(args=None, step_func=None):
    """
    Implement program core logic.

    :param args: Command line arguments list.

    :param step_func: Step info setter function.

    :return: Exit code.
    """
    # If step function is not given
    if step_func is None:
        # Raise error
        raise ValueError('Error (3P92V): Argument `step_func` is not given.')

    # If step function is given.

    # Set step info
    step_func(title='Parse command line arguments')

    # Create command line arguments parser
    cmdargs_parser = get_cmdargs_parser()

    # If command line arguments list is not given
    if args is None:
        # Use default command line arguments list
        args = sys.argv[1:]

    # If command line arguments list is empty
    if not args:
        # Print help
        cmdargs_parser.print_help()

        # Return without error
        return 0

    # If command line arguments list is not empty.

    # Parse command line arguments
    cmdargs = cmdargs_parser.parse_args(args)

    # Set step info
    step_func(title='Compute factorial')

    # Get number
    number = cmdargs.number

    # Compute the number's factorial
    result = factorial(number)

    # Get message
    msg = 'Factorial of {} is {}'.format(number, result)

    # Print the message
    print(msg)

    # Return without error
    return 0


def main_wrap(args=None):
    """
    Wrap `main_core` to provide uncaught exception handling.

    :param args: Command line arguments list.

    :return: Exit code.
    """
    # Dict that contains step info
    step_info = {
        # Step title
        'title': '',

        # Exit code
        'exit_code': 0
    }

    # Create step info setter function
    def _step_func(title=None, exit_code=None):
        """
        Step info setter function.

        :param title: Step title.

        :param exit_code: Exit code.

        :return: None.
        """
        # If step title is given
        if title is not None:
            # Update step title
            step_info['title'] = title

        # If exit code is given
        if exit_code is not None:
            # Update exit code
            step_info['exit_code'] = exit_code

    #
    try:
        # Call `main_core` to implement program core logic
        return main_core(args=args, step_func=_step_func)

    # Catch exit
    except SystemExit:
        # Re-raise
        raise

    # Catch keyboard interrupt
    except KeyboardInterrupt:
        # Return without error
        return 0

    # Catch other exceptions
    except BaseException:
        # Get step title
        step_title = step_info.get('title', '')

        # Get traceback
        tb_msg = traceback.format_exc()

        # If step title is not empty
        if step_title:
            # Get message
            msg = '# Error (5QDEX): {0}\n---\n{1}---\n'.format(
                step_title, tb_msg
            )
        else:
            # Get message
            msg = '# Error (5QDEX)\n---\n{0}---\n'.format(tb_msg)

        # Print message
        sys.stderr.write(msg)

        # Get exit code
        exit_code = step_info.get('exit_code', 8)

        # Return exit code
        return exit_code
