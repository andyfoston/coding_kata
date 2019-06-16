#!/usr/bin/env python3
""" Provides basic arithmetic functions, as well as functionality to perform
basic arithmetric operations from the command line.
"""

import sys
from argparse import ArgumentParser

def add(operand_a, operand_b):
    """ Adds the two provided arguments together.

    Args:
        operand_a: an int or float to be used in the resulting calculation.
        operand_b: an int or float to be used in the resulting calculation.
    Returns:
        The result of adding the two operands together.
    """
    return operand_a + operand_b


def subtract(operand_a, operand_b):
    """ Subtracts the first argument from the second.

    Args:
        operand_a: an int or float to be used in the resulting calculation.
        operand_b: an int or float to be used in the resulting calculation.
    Returns:
        The result of subtracting the two operands.
    """
    return operand_a - operand_b


def multiply(operand_a, operand_b):
    """ Multiplies the two provided arguments together.

    Args:
        operand_a: an int or float to be used in the resulting calculation.
        operand_b: an int or float to be used in the resulting calculation.
    Returns:
        The result of multiplying the two operands.
    """
    return operand_a * operand_b


def divide(operand_a, operand_b):
    """ Divides the two provided arguments.

    Args:
        operand_a: an int or float to be used in the resulting calculation.
        operand_b: an int or float to be used in the resulting calculation.
    Returns:
        The result of dividing the two operands.
    Raises:
        ZeroDivisionError if operand_b is equal to 0.
    """
    return operand_a / operand_b


def parse_args(args=None):
    """ Parses the command-line arguments.

    Args:
        args: A list of argument strings to be parsed. Should only be provided
         for testing.
    Returns:
        An `argparse.Namespace` instance representing the provided args.
    """
    parser = ArgumentParser(
        description="Performs basic arithmetic on two provided numbers")
    parser.add_argument(
        "operand", type=float, nargs=2,
        help="The operands that the arithmetic operation will be applied to")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-a", "--add", action='store_true',
                       help="Adds the two operands together")
    group.add_argument("-s", "--subtract", action='store_true',
                       help="Subtracts the second operand from the first")
    group.add_argument("-m", "--multiply", action='store_true',
                       help="Multiplies the two operands together")
    group.add_argument("-d", "--divide", action='store_true',
                       help="Divides the first operand by the second operand")
    return parser.parse_args(args)


def run(args):
    """ Runs the calculation and returns the formula and result.

    Args:
        An instance of `argparse.Namespace`.
    Returns:
        A string containing the formula and result of the calculation.
    Raises:
        ZeroDivisionError if operand_b is equal to 0.
    """
    if args.add:
        operator = "+"
        result = add(*args.operand)
    elif args.subtract:
        operator = "-"
        result = subtract(*args.operand)
    elif args.multiply:
        operator = "*"
        result = multiply(*args.operand)
    else: # divide
        operator = "/"
        result = divide(*args.operand)
    return f"{args.operand[0]} {operator} {args.operand[1]} = {result}"


if __name__ == '__main__':
    ARGS = parse_args()
    try:
        print(run(ARGS))
    except ZeroDivisionError:
        print("Cannot divide {} by {}".format(*ARGS.operand))
        sys.exit(1)
