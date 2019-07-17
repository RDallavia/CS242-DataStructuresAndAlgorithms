#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ryan C. Dallavia
CS242 - Summer 2018
06/25/1018
Lab 4

The following is a completed version of the ArraySortedBag Class from 
Lambert, Kenneth A. (2014) "Fundamentals of Python: Data Structures"
with additional code for memory resizing added by the student. 
"""

from arrays import Array
from arraybag import ArrayBag
from abstractbag import AbstractBag

class ArraySortedBag(AbstractBag):
    """An array-based bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = Array(ArraySortedBag.DEFAULT_CAPACITY)
        AbstractBag.__init__(self, sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __contains__(self, item):
        """Binary Search for Item in Bag"""
        length = len(self)
        low = 0
        high = length - 1
        while low <= high:
            mid = low + (high - low)//2
            if item == self._items[mid]:
                return True
            elif item > self._items[mid]:
                low = mid+1
            elif item < self._items[mid]:
                high = mid-1
        return False

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArraySortedBag.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        # Check array memory here and increase it if necessary
        if len(self._items) == len(self):
            new_bag = Array(ArraySortedBag.DEFAULT_CAPACITY*2)
            for index in range(len(self)):
                new_bag[index] = self._items[index]
            self._items = new_bag
        # Empty or last item, call ArrayBag.add
        if self.isEmpty() or item >= self._items[len(self) - 1]:
            ArrayBag.add(self, item)
        else:
            # Search for first item >= new item
            targetIndex = 0
            while item > self._items[targetIndex]:
                targetIndex += 1
            # Open a hole for new item
            for i in range(len(self), targetIndex, -1):
                self._items[i] = self._items[i - 1]
            # Insert item and update size
            self._items[targetIndex] = item
            self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # Search for the index of the target item
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        # Shift items to the left of target up by one position
        for i in range(targetIndex, len(self) - 1):
            self._items[i] = self._items[i + 1]
        # Decrement logical size
        self._size -= 1
        # Check array memory here and decrease it if necessary 
        load_factor = round(len(self)/len(self._items),2)
        if load_factor < .25:
            new_bag = Array(len(self))
            for i in range(len(self)):
                new_bag[i] = self._items[i]
            self._items = new_bag