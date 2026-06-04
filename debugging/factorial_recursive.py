#!/usr/bin/python3
import sys

def factorial(n):
    """
    Computes the factorial of a given number recursively.
    For example, factorial(5) returns 120 because 5 * 4 * 3 * 2 * 1 = 120.

    Parameters:
        n (int): The number to calculate the factorial for. Must be 0 or positive.

    Returns:
        int: The factorial of n. If n is 0, returns 1 (since 0! = 1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)