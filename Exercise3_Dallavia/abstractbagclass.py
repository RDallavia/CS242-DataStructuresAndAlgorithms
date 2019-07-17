#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ryan C. Dallavia
6/29/2018
CS242 - Summer 2018
Exercise 3

Sample code from Lambert, Kenneth A. (2014)
"Fundamentals of Python: Data Structures"
"""

class AbstractBag(object):
    def __init__(self, sourceCollection=None):
        '''Initialize size variable & routine for
        instantiation with pre-existing collection'''
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
                
    def isEmpty(self):
        '''Return length of Bag'''
        return len(self) == 0
    
    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"
            
    def __len__(self):
        '''Returns number of items in the bag'''
        return self.size
    
    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result
    
    def __eq__(self, other):
        '''Determines if two bags are the same'''
        if self is other:
            return True
        if type(self) != type(other) or \
        len(self) != len(other):
            return False
        for item in other:
            if not item in self:
                return False
        return True
            