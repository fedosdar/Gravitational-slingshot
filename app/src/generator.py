import numpy as np

rng = np.random.default_rng()


def generate_integer(left: int, right: int) -> int:
    """
    Generate random integer number using numpy generator.
    :param left: left part of the interval (included)
    :param right: right part of the interval (included)
    :return: random integer number
    """
    return rng.integers(low=left, high=right + 1)


def generate_float(left: float, right: float) -> float:
    """
    Generate random float number using numpy generator.
    If number is out of bounds - using modulo operations it's scaled to number in the given interval.
    :param left: left part of the interval (included)
    :param right: right part of the interval (included)
    :return: random float number
    """
    num = rng.random()
    if num > right or num < left:
        num = num % (right - left) + left
    return num

