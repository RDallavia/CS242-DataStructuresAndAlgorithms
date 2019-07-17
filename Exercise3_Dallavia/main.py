#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ryan C. Dallavia
6/29/2018
CS242 - Summer 2018
Exercise 3

The following driver program tests the modification of the LinkedBag class, 
after it has become a subclass of AbstractBag. We have retained in LinkedBag 
only those methods that cannot be moved to AbstractBag.
"""
from linkedbagclass import LinkedBag

def main():
    print("""Instantiate linked bag, add 4 items individually, and print""")
    linked_bag1 = LinkedBag()
    linked_bag1.add(1)
    linked_bag1.add(2)
    linked_bag1.add(3)
    linked_bag1.add(4)
    print(linked_bag1)
    print("")
    print("""Instantiate second linked bag using source collection""")
    linked_bag2 = LinkedBag([5,6,7,8])
    print(linked_bag2)
    print("")
    print("""Add additional element to second bag post instantiation""")
    linked_bag2.add(12)
    print(linked_bag2)
    print("")
    print("""Remove 8 and 6 from second bag. Expected {12, 7, 5}""")
    linked_bag2.remove(8)
    linked_bag2.remove(6)
    print(linked_bag2)
    print("")
    print("""Retrieve length of bag 1. Expected 4""")
    print(len(linked_bag1))
    print("")
    print("""Test if bag 1 is empty. Expected False""")
    print(linked_bag1.isEmpty())
    print("")
    print("""Test if bag 1 == bag 2. Expected False""")
    print(linked_bag1 == linked_bag2)
    print("")
    print("""Create bag 3 same as bag 2 and test equality. Expected True""")
    linked_bag3 = LinkedBag([12,7,5])
    print(linked_bag2 == linked_bag3)
    print("")
    print("""Clear bag 3""")
    linked_bag3.clear()
    print(linked_bag3)
    print("")
    
if __name__ == '__main__':
    main()