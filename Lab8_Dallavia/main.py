#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ryan C. Dallavia
07/20/2018
CS242 - Summer 2018

Driver program to produce balanced binary search
tree using rebalanced method, installed by student, in 
linkedBST class. 
"""
from linkedbst import LinkedBST

def main():
    data = ['R','G','T','F','J','S','W','A','P','Z']
    tree = LinkedBST(data)
    print("Tree prior to rebalance:")
    print(tree)
    print("Tree after rebalance:")
    tree.rebalance()
    print(tree)
    

if __name__ == '__main__':
    main()