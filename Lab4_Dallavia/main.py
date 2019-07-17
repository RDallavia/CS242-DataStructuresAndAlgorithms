#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ryan C. Dallavia
CS242 - Summer 2018
06/25/1018
Lab 4

The following driver program tests the functionality added to the ArraySortedBag
class. Our focus is on the __contains__, add, remove, and clear methods. 
Steps are taken to expose those aspects of the add and remove routines intended
to increase/decrease the physical size of the underlying array in response to
changes in the array's logical size.
"""

import random
from arraysortedbag import ArraySortedBag

def main():
    bags = []
    for index in range(0, 4):
        bags.append(ArraySortedBag())
    
    print("""Expected: Four sorted array bags""")
    for index in range(len(bags)):
        print("Bag " + str(index) + " " + str(type(bags[index])))
    print("\n")
    
    print("""Expected: Four bags will contain one number""")
    for index in range(0,4):
        num = random.randint(0,20)
        bags[index].add(num)
        print("Bag " + str(index) + " " + str(bags[index]))
    print("\n")
    
    print("""Expected: Four bags will contain 5 numbers in sorted order""")
    for bag in bags:
        for j in range(4):
            num = random.randint(0,20)
            bag.add(num)
        print(bag)
    print("\n")
    
    print("""Expected: List 'd' will contain 7 ints and these will be added
          in sorted order to Bag 1 upon instatiation""")
    nums = [9,3,5,4,1,7,10]
    Bag5 = ArraySortedBag(nums)
    print("Bag " + str(5) + " " + str(Bag5))
    print("\n")
    
    print("""Expected: 'Contains' method determines precense of item in bag""")
    for index in range(len(bags)):
        if index not in bags[index]:
            print(str(index) + " not in " + "bag " + str(index))
        else:
            print(str(index) + " in " + "bag " + str(index))
            
    # manual test of bag 5 which is static    
    if 10 in Bag5:
        print("10 in bag 5")
    else:
        print("10 not in bag 5")
    print("\n")
    
    print("""Expected: Bags 0, 1, and 2 are cleared""")
    for index in range(0,3):
        bags[index].clear()
        print("Bag " + str(index) + " " + str(bags[index]))
    print("\n")
    
    print("""Remove items 3 items from Bag 5 and print contents. 
          Expected: Logical length of Bag 5 is 4.""")
    Bag5.remove(5)
    Bag5.remove(7)
    Bag5.remove(1)
    print(Bag5)
    print("""Reveal physical size of Bag 5. Expected: Physical length of Bag 5 is 10.""")
    print(Bag5._items)
    print("\n")
    print("""Remove items 2 more items from Bag 5 and print contents. Expected logical length of Bag 5 is 2.""")
    Bag5.remove(3)
    Bag5.remove(10)
    print(Bag5)
    print("\n")
    print("""Expected: Physical size of Bag 5 has decresed to 2, as load factor has now dropped below .25.""")
    print(Bag5._items)
    print("\n")
    print("""Fill Bag 0 to capacity and print.""")
    for i in range(10):
        bags[0].add(i)
    print("Bag 0 " + str(bags[0]))
    print("\n")
    print("""Reveal physical size of Bag 0. Expected: Physical length of Bag 0 is 10.""")
    print(bags[0]._items)
    print("\n")
    print("""Add item to Bag 0 forcing increase in physical length. Expected: New physical length is 20.""")
    bags[0].add(25)
    print(bags[0]._items)
    print("\n")
        

if __name__ == '__main__':
    main()
        