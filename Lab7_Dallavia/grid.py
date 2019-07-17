"""
File: grid.py
"""

from arrays import Array

class Grid(object):
    """Represents a two-dimensional array."""

    def __init__(self, rows, columns, fillValue):
        self._data = Array(rows)
        for row in range(rows):
            self._data[row] = Array(columns, fillValue)
        if fillValue:
            self._setValues(fillValue)

    def getHeight(self):
        """Returns the number of rows."""
        return len(self._data)

    def getWidth(self):
        """Returns the number of columns by accessing row zero and taking length."""
        return len(self._data[0])
    
    def getSumTotal(self):
        '''Sum all values in table'''
        sum = 0
        for i in range(self.getHeight()):
            for j in range(self.getWidth()):
                sum += self[i][j]
        return sum

    def __getitem__(self, index):
        """Supports two-dimensional indexing with [][]."""
        return self._data[index]

    def __str__(self):
        """Returns a string representation of the grid."""
        result = ""
        # works exactly like iterating over any matrix, just looks a bit different
        # for i in range(number of rows)
        for row in range(self.getHeight()):
            # for j in range(number of columns)
            for col in range(self.getWidth()):
                # get the cell data
                result += str(self._data[row][col]) + " "
            result += "\n"
        return result
    
    def _setValues(self, value):
        """Change all values in table"""
        for i in range(self.getHeight()):
            for j in range(self.getWidth()):
                self[i][j] = value[i][j]
        

#def main():
#    c = [[1, 2, 3], [4, 5, 6]]
#    g = Grid(2, 3, c)
#    print(g)

#if __name__ == "__main__":
#    main()
    
            
