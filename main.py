from typing import Union


def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Adds two numbers and returns the result.

    Args:
        a: The first number (int or float).
        b: The second number (int or float).

    Returns:
        The sum of a and b.
    """
    return a + b


if __name__ == "__main__":
    print(add_numbers(5, 3))
