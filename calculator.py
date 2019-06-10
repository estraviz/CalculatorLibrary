"""
Calculator library containing basic math operations.
"""

import pytest


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def multiply(first_term, second_term):
    return first_term * second_term


def divide(first_term, second_term):
    try:
        return first_term / second_term
    except ZeroDivisionError as e:
        pytest.fail(e, pytrace=True)
