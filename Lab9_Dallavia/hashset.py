"""
File: hashdict.py

An hash-based dictionary.
"""

from node import Node
from arrays import Array
from abstractcollection import AbstractCollection
from abstractset import AbstractSet

class HashSet(AbstractCollection, AbstractSet):
    """Represents a hash-based set."""

    DEFAULT_CAPACITY = 9

    def __init__(self, sourceCollection = None):
        self._array = Array(HashSet.DEFAULT_CAPACITY)
        self._foundNode = self._priorNode = None
        self._index = -1
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __contains__(self, item):
        """Returns True if item is in self or False otherwise."""
        self._index = abs(hash(item)) % len(self._array)
        self._priorNode = None
        self._foundNode = self._array[self._index]
        while self._foundNode != None:
            if self._foundNode.data == item: 
                return True
            else:
                self._priorNode = self._foundNode
                self._foundNode = self._foundNode.next
        return False

    def __str__(self):
        """
        Refactored string representation of table, by student, to clearly 
        demonstrate structure of hash table as an array of linked lists
        """
        view = "{"
        for i in range(len(self._array)):
            if self._array[i] != None:
                view += str(i) + ":"
                probe = self._array[i]
                for j in range(self._size):
                    view += str(probe.data)
                    if probe.next != None:
                        view += " --> "
                        probe = probe.next
                    else:
                        if i != len(self._array) - 1:
                            view += ",\n"
                        break
        view += "}"
        return view

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self._array):
            node = self._array[cursor]
            while node != None:
                yield node.data
                node = node.next
            cursor += 1

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._array = Array(HashSet.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        if not item in self: 
            self._array[self._index] = Node(item,
                                            self._array[self._index])
            self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        if not item in self:
            raise KeyError(str(item) + " not in set")
        elif self._priorNode == None:
            self._array[self._index] = self._foundNode.next
        else:
            self._priorNode.next = self._foundNode.next
        self._size -= 1 

    # Utility methods
    def loadFactor(self):
        return len(self) / len(self._array)

    def rehash(self):
        """ 
        Rehash method of Lambert, Kenneth A. (2014) with max load factor
        adjusted from 0.5 to 0.8
        """
        if self.loadFactor() > 0.8:
            items = list(self)
            self._array = Array(len(self._array) * 2)
            self._size = 0
            for item in items:
                self.add(item)
        return self 


        
