#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ryan C. Dallavia
June 16, 2018
Lab 2
CS242 - Summer 2018

Program generates comparative data on iterative, memoized, and non-memoized
recursive implementations of the Fibonacci number generator. Eight
cases are examined for the iterative and memoized fibonacci implementations, and 
five cases are examined for the non-memoized recursive implementation, due to 
time constraints and the computational intensity of that particular 
implementation. The number of calculations and total running times are 
displayed. The iterative implementation is the most efficient. 
"""

from counter import Counter
import time

def recursive_fib(n, counter):
    '''
    Recursive implementation of fibonacci algorithm with embedded counter to 
    track recursive calls from Lambert, Kenneth A. (2014) "Fundamentals of 
    Python: Data Structures."
    
    Input: Positive integer and counter object
    Output: Fibonacci number corresponding to integer and number of recursive calls
    '''
    if n < 3:
        return 1
    else:
        counter.increment()
        return recursive_fib(n - 1, counter) + recursive_fib(n - 2, counter)

def fast_fib(num, counter, memo={}):
    '''
    Memoized implementation of the fibonacci algorithm with embedded counter to 
    track recursive calls
    
    Input: Positive integer, counter object, empty memo as dictionary
    Output: Fibonacci number corresponding to integer and number of recursive calls
    '''
    
    if num < 3:
        return 1
    if num in memo:
        return memo[num]
    else:
        counter.increment()
        answer = fast_fib(num - 1, counter) + fast_fib(num - 2, counter)
        memo[num] = answer
        return memo[num]

def iterative_fib(n, counter):
    '''
    Iterative implementation of the fibonacci algorithm from
    Lambert, Kenneth A. (2014) "Fundamentals of Python: Data Structures"
    
    Input: Positive integer and counter object
    Output: Fibonacci number corresponding to integer and number of calculations
    '''
    sum = 1
    first = 1
    second = 1
    count = 3
    while count <= n:
        counter.increment()
        sum = first + second
        first = second
        second = sum
        count += 1
    return sum
    
def fib_tester(fib_function):
    # set_range establishes number of cases to examine when fib function called
    # only 5 cases examined with recursive_fib due to exponential runtime
    if fib_function == iterative_fib:
        print("Iterative Fibonacci")
        set_range = 8
    elif fib_function == fast_fib:
        print("Memoized Fibonacci")
        set_range = 8
    elif fib_function == recursive_fib:
        print("Recursive Fibonacci")
        set_range = 5
    
    # calculate N fibonacci numbers that are successive multiples of two, where
    # N is based on the set_range assigned to each fib_function above. 
    problemSize = 2
    if fib_function == fast_fib or fib_function == recursive_fib:
        print("%12s%20s%60s%22s" % ("Problem Size", "Recursive Calls", "Fibonacci", "Time (secs)"))
    else:
        print("%12s%20s%60s%22s" % ("Problem Size", "Calculations", "Fibonacci", "Time (secs)"))
    for count in range(set_range):
        counter = Counter()
        # call and time the function
        start = time.time()
        fib = fib_function(problemSize, counter)
        elapsed = time.time() - start
        # count each of the two recursive calls individually, if applicable
        if fib_function == fast_fib or fib_function == recursive_fib:
            counter.timesTwo()
        print("%12d%20s%60d%20.6f" % (problemSize, counter, fib, elapsed))
        problemSize *= 2
    print("\n")
    
def main():
    '''
    Diver calling fib_tester function on all implementations of 
    the fibonacci algorithm.
    '''
    fib_tester(iterative_fib)
    fib_tester(fast_fib)
    fib_tester(recursive_fib)

if __name__ == '__main__':
    main()
