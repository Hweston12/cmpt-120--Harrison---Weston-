from math import pi
from unittest import result


def calculate_sum(n):
    '''
    This function should calculate the sum every number from 0 up until n (NON-INCLUSIVE).
    @return: this method should just return the sum of every number from 0 to n.
    '''


    result = 0
    # your logic
    for i in range(0,n):
        result = result + i

    return result


def calculate_pi(n):
    '''
    This function calculates Pi using Leibniz's formula. The formula is calculated as
    the following:
        X = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + 4/13 - ...
    Notice the pattern within the formula. Please note that this series is never-ending
    and the higher value you pass in for n the closer the value of X converges to the value
    of Pi.
    Hint: 
        1. init your denominator k outside your loop.
        2. run a loop from 0 to n
        3. use mod inside the loop to determine whether to add or subtract 4/k
        4. increment k by 2
        5. repeat from step 2 until you reach end of range.
    @arg(n): the number of terms in the series to calculate (must be odd) (INCLUSIVE).
    @return: the calculated
    '''

    result = 0
    # your logic
    denom = 1
    for i in range(n): 
        if i % 2 == 0:
            result += 4 / denom
        else: 
            result -= 4 / denom 
        denom += 2
    return result


def fibonacci(n):
    '''
    The fibonacci sequence is a series of numbers. The next number is found
    by adding up the two numbers before it in the sequence. The series looks
    like this [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...]
    Hint: the first two numbers are 0 and 1. 
    @arg(n): the number of terms in the series to calculate.
    @return: the sum of the fibonacci numbers up until n.
    '''

    fib = [0, 1]

    for i in range(1,n):
        if n > 2:
            val = fib[i] + fib[i - 1]
            fib.append(val)
    return fib[n - 1]
