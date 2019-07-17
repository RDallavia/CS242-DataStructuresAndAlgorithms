#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ryan C. Dallavia
CS242 - Summer 2018
07/22/2018
Lab9

The following driver program instantiates the HashSet object,
tests the rehash function with a load factor of .80, and
runs tests that are germane to asked questions. 
"""

from hashset import HashSet
import time
import random

def main():
    data = [i for i in range(100)]
    hash_set = HashSet(data)
    print("\nTest initial hash table")
    print("------------------\n")
    print(hash_set)
    print("\n")
    print("Test hash table after rehash")
    print("-------------------------\n")
    print(hash_set.rehash())
    print("\n")
    print("Clear hashtable and insert random integers from 1 to 400.")
    hash_set.clear()
    start = time.process_time()
    for i in range(400):
        integer = random.randint(1,400)
        hash_set.add(integer)
    elapsed = time.process_time() - start
    print("Elapsed CPU processing time for insertion of 400 random ints is: " + str(elapsed) + " seconds" + "\n")
    print("Clear hashtable and insert sequential integers from 1 to 400.")
    hash_set.clear()
    start = time.process_time()
    for i in range(400):
        hash_set.add(i)
    elapsed = time.process_time() - start
    print("Elapsed CPU processing time for insertion of 400 sequential ints is: " + str(elapsed) + " seconds" + "\n")
    print("Clear hashtable and insert integers from 1 to 10.")
    hash_set.clear()
    start = time.process_time()
    for i in range(1,11):
        hash_set.add(i)
    if 3 in hash_set:
        print(True)
    elapsed = time.process_time() - start
    print("Elapsed CPU processing time for insertion of 10 ints and finding the number '3' : " + str(elapsed) + " seconds" + "\n")
    print("Clear hashtable and insert integers from 1 to 3.")
    hash_set.clear()
    start = time.process_time()
    for i in range(1,4):
        hash_set.add(i)
    if 3 in hash_set:
        print(True)
    elapsed = time.process_time() - start
    print("Elapsed CPU processing time for insertion of 3 ints and finding the number '3' : " + str(elapsed) + " seconds" + "\n")
    
    print("Clear hashtable, insert integers from 1 to 10, remove ints 4 thru 10, find 3.")
    hash_set.clear()
    start = time.process_time()
    for i in range(1,11):
        hash_set.add(i)
    for i in range(4,11):
        hash_set.remove(i)
    if 3 in hash_set:
        print(True)
    elapsed = time.process_time() - start
    print("Elapsed CPU processing time to insert integers from 1 to 10, remove ints 4 thru 10, find '3': " + str(elapsed) + " seconds" + "\n")
    print("Clear hashtable and insert integers from 1 to 3, remove ints 1 and 2, find 3.")
    hash_set.clear()
    start = time.process_time()
    for i in range(1,4):
        hash_set.add(i)
    for i in range(1,2):
        hash_set.remove(i)
    if 3 in hash_set:
        print(True)
    elapsed = time.process_time() - start
    print("Elapsed CPU processing time to insert integers from 1 to 3, remove ints 1 thru 2, find '3': " + str(elapsed) + " seconds" + "\n")
    
if __name__ == '__main__':
    main()
