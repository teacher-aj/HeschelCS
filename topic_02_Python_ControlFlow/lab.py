"""
Lab Instructions (VS Code Version):

1. Complete each function below so that all doctests pass.
2. Save your work.
3. To check your work, click ▶️ “Run Python File” at the top right of VS Code,
   OR right-click the file and choose “Run Python File in Terminal”.
4. The test results will print at the bottom of VS Code.

You do NOT need to use the terminal manually.
"""

import math
import doctest

def hypotenuse(a, b):
    '''
    Return the square root of a squared plus b squared.

    >>> hypotenuse(3.0, 4.0)
    5.0
    >>> hypotenuse(12.0, 5.0)
    13.0
    >>> hypotenuse(12, 5)
    13.0
    >>> type(hypotenuse(12.0, 5.0))
    <class 'float'>
    '''


def is_even(n):
    '''
    Return True if n is even and False if n is odd.

    >>> is_even(0)
    True
    >>> is_even(1)
    False
    >>> is_even(2000)
    True
    >>> is_even(-8)
    True
    >>> is_even(-9)
    False
    >>> type(is_even(0))
    <class 'bool'>
    '''


def is_odd(n):
    '''
    Return True if n is odd and False if n is even.

    >>> is_odd(0)
    False
    >>> is_odd(1)
    True
    >>> is_odd(2000)
    False
    >>> is_odd(-8)
    False
    >>> is_odd(-9)
    True
    >>> type(is_odd(0))
    <class 'bool'>
    '''


def absolute_value(n):
    '''
    Return the absolute value of n.

    >>> absolute_value(5)
    5
    >>> absolute_value(-5)
    5
    >>> absolute_value(5.5)
    5.5
    >>> absolute_value(-5.5)
    5.5
    '''


def max_num(a, b):
    '''
    Return the maximum of a and b.

    >>> max_num(4, 5)
    5
    >>> max_num(5, 4)
    5
    >>> max_num(-4, -5)
    -4
    >>> max_num(4, 4)
    4
    >>> type(max_num(4, 4))
    <class 'int'>
    '''


def max_num_4(a, b, c, d):
    '''
    Return the maximum of a, b, c, and d.

    >>> max_num_4(1,2,3,4)
    4
    >>> max_num_4(2,3,4,1)
    4
    >>> max_num_4(3,4,1,2)
    4
    >>> max_num_4(4,1,2,3)
    4
    >>> max_num_4(10,1,2,3)
    10
    '''


def max_num_abs(a, b):
    '''
    Return the number with the highest absolute value.

    >>> max_num_abs(4,5)
    5
    >>> max_num_abs(-4,-5)
    -5
    >>> max_num_abs(4,4)
    4
    >>> type(max_num_abs(4, 4))
    <class 'int'>
    '''


def is_leap_year(n):
    '''
    Return True if n is a leap year and False otherwise.

    >>> is_leap_year(1582)
    False
    >>> is_leap_year(2000)
    True
    >>> is_leap_year(2018)
    False
    >>> is_leap_year(2019)
    False
    >>> is_leap_year(2020)
    True
    >>> is_leap_year(2200)
    False
    >>> is_leap_year(2400)
    True
    '''


def num_digits(n):
    '''
    Return the number of digits in the input n.

    >>> num_digits(5)
    1
    >>> num_digits(10)
    2
    >>> num_digits(45678)
    5
    >>> num_digits(123456789012345678901234567890)
    30
    >>> num_digits(-5)
    1
    >>> num_digits(-10)
    2
    >>> type(num_digits(4))
    <class 'int'>
    '''


def factorial(n):
    '''
    Return the factorial of n.

    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    >>> factorial(10)
    3628800
    '''


# Optional extra credit examples below:
def is_prime(n):
    '''
    Return True if n is prime, and False otherwise.

    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(97)
    True
    >>> is_prime(99)
    False
    '''


def fibonacci(n):
    '''
    Return the nth fibonacci number.

    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(4)
    3
    >>> fibonacci(5)
    5
    >>> fibonacci(6)
    8
    >>> fibonacci(7)
    13
    >>> type(fibonacci(4))
    <class 'int'>
    '''


# ✅ Run all doctests when this file is executed
if __name__ == "__main__":
    print("Running doctests...\n")
    doctest.testmod(verbose=True)
    print("\n✅ All doctests complete.")
