#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ryan C. Dallavia
06/12/2018
CS242 - Summer Session
Exercise 2

Driver program providing head-to-head comparison of original quickSort
versus modified quickSort. Original quickSort, insertionSort, and profiler
codes provided by Lambert, Kenneth A. (2014), "Fundamentals of Python:
Data Structures." Modifications to quickSort & driver code provided by student.

Note, based on the elapsed time data reported, and multiple tials, modified 
quickSort tends to return a result faster when the problem's input size cosists  
of less than approximately 275 integers. The result seems to be consistent with
what we know about algorithmic performance and input sizes. At small input sizes, 
we are generally indifferent to algorithmic time complexity, and the algorithm 
with the slower big-O performance profile may actually perform better. 
However, as the input size increases, we would rather employ the fastest 
algorithm -- from a big-O perspective -- at our disposal.
"""
import random
from profiler import Profiler
from modified_qsort import mod_quicksort
from testquicksort import quicksort


def main():
    # requested test cases per problem specs, plus cases used to determine optimization
    problem_sizes = [50, 160, 200, 275, 500, 5000]
    for problem_size in problem_sizes:
        lyst = []
        for count in range(problem_size):
            lyst.append(random.randint(1, problem_size + 1))
        # test and profile original quicksort
        print("Original quicksort: Problem Size = " + str(problem_size) + " integers.")
        print("_______________________________________________________________________")
        profiler = Profiler()
        profiler.test(quicksort, lyst=lyst, comp=True, exch=True)
        print("\n")
        # test and profile modified quicksort
        print("Modified quicksort: Problem Size = " + str(problem_size) + " integers.")
        print("_______________________________________________________________________")
        profiler = Profiler()
        profiler.test(mod_quicksort, lyst=lyst, comp=True, exch=True)
        print("\n")

            


if __name__ == "__main__":
    main() 