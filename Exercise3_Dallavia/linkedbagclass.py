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

from abstractbagclass import AbstractBag

class Node(object):
    def __init__(self, data=None, next=None):
        '''Instantiates node object'''
        self.data = data
        self.next = next

class LinkedBag(AbstractBag):
    def __init__(self, sourceCollection=None):
        self.items = None
        AbstractBag.__init__(self, sourceCollection)

    def __iter__(self):
        cursor = self.items
        # while there's something to iterate over
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next

    def add(self, item):
        self.items = Node(item, self.items)
        self.size += 1
    
    def clear(self):
        self.items = None
        self.size = 0
    
    def remove(self, item):
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        probe = self.items
        trailer = None
        for datum in self:
            if datum == item:
                break
            trailer = probe
            probe = probe.next
        if probe == self.items:
            self.items = self.items.next
        else:
            trailer.next = probe.next
            probe.next = None
            trailer = None
        self.size -= 1

