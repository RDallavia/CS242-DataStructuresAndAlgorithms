#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ryan C. Dallavia
CS242 - Summer 2018
07/21/2018
Exercise 5

The following program demonstrates the use of the remove() and get() methods
added to the HashTable implemented by Lambert, Kenneth A. (2014) "Fundamentals
of Python: Data Structures." __str__ and __len__ methods were also added to
provide a view of the table. While the author implemented the table using an
array, the view produced here is that of a dictionary, which is the more common
visualization of a hashtable used in Python. 
"""
from hashtable import HashTable

def main():
    """Uses an example data set from Chapter 19."""
    table = HashTable(8, lambda x : x)
    for item in (range(10, 71, 10)):
        table.insert(item)
    print("Original Hash Table")
    print(table)
    print("\n")
    print("Get 31: Expect -1")
    print(table.get(31))
    print("\n")
    print("Get 10: Expect 2")
    print(table.get(10))
    print("\n")
    print("Remove 11: Expect -1")
    print(table.remove(11))
    print("\n")
    print("Remove 60: Expect True")
    print(table.remove(60))
    print("\n")
    print("Hash Table After Removal")
    print(table)
    print("\n")
    

if __name__ == "__main__":
    main()