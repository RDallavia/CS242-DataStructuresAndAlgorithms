"""
File: hashtable.py

Case study for Chapter 11.
"""

from arrays import Array

class HashTable(object):
    "Represents a hash table."""

    EMPTY = None
    DELETED = True

    def __init__(self, capacity = 29,
                 hashFunction = hash,
                 linear = True):
        self._table = Array(capacity, HashTable.EMPTY)
        self._size = 0
        self._hash = hashFunction
        self._homeIndex = -1
        self._actualIndex = -1
        self._linear = linear
        self._probeCount = 0

    def insert(self, item):
        """Inserts item into the table
        Preconditions: There is at least one empty cell or
        one previously occupied cell.
        There is not a duplicate item."""
        self._probeCount = 0
        # Get the home index
        self._homeIndex = abs(self._hash(item)) % len(self._table)
        distance = 1
        index = self._homeIndex

        # Stop searching when an empty cell is encountered
        while not self._table[index] in (HashTable.EMPTY,
                                         HashTable.DELETED):

            # Increment the index and wrap around to first 
            # position if necessary
            if self._linear:
                increment = index + 1
            else:
                # Quadratic probing
                increment = self._homeIndex + distance ** 2
                distance += 1
            index = increment % len(self._table)
            self._probeCount += 1

        # An empty cell is found, so store the item
        self._table[index] = item
        self._size += 1
        self._actualIndex = index
    
    def get(self, item):
        """
        Takes item requested and returns index if found, else returns -1
        """
        # start with home index of item
        index = abs(self._hash(item)) % len(self._table)
        
        # search down the table until item found or you hit empty cell
        while self._table[index] != item and self._table[index] != HashTable.EMPTY:
            index = (index + 1) % len(self._table)
        
        # exited loop without finding item
        if self._table[index] != item:
            return -1
        else:
            return index

    def remove(self, item):
        """
        Takes item as the parameter and will return true, if the item requested
        is removed; otherwise, the method will return -1, if the item is not 
        found and, thus, not removed.
        """
        # start with home index of item
        index = abs(self._hash(item)) % len(self._table)
        
        # search down the table until item found or you hit empty cell
        while self._table[index] != item and self._table[index] != HashTable.EMPTY:
            index = (index + 1) % len(self._table)
        
        # exited loop without finding item
        if self._table[index] != item:
            return -1
        else:
            self._table[index] = HashTable.DELETED
            return True
        
    def __len__(self):
        return self._size
    
    def __str__(self):
        view = "{"
        for index in range(len(self)):
            view += str(index)+":"+str(self._table[index])
            if index != len(self) - 1:
                view += ", "
        view += "}"
        return view
    

        
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

# __str__(), loadFactor(), homeIndex(),
# actualIndex(), and probeCount() are exercises.

#        print("Home:", table.homeIndex(), "Probes:", table.probeCount(),
#              "Load factor:", table.loadFactor())
        



