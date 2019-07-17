"""
Ryan C. Dallavia
7/16/2018
CS242 - Summer Session
Exercise 4

1) The line of code evaluates to true when the modifications to the list and the backingStore
are misaligned (i.e., an illegal modification to the list, from outside of the list iterator, context) has been
made.
2)  Take the data in the class instance (an iterable), run it thru the string function using the map function, 
output a string in which the elements are separated a comma followed by a space (i.e., the elements are joined by
a comma and a space). 
3) Graphic arts is completely out of my wheelhouse. 
"""


from linkedlist import LinkedList

def main(ListType):
    """Expects a list type as an argument and runs some tests
    on a list iterator on that type."""
    print("\nTESTING A LIST ITERATOR FOR THE TYPE " + str(ListType) )
    print("Create a list with 1-9")
    lyst = ListType(range(1, 10))
    print("Length:", len(lyst))
    print("Items in list (first to last):", lyst)
    
    # Create and use a list iterator
    listIterator = lyst.listIterator()
    print("Forward traversal with list iterator: ", end="")
    listIterator.first()
    while listIterator.hasNext(): 
            print(listIterator.next(), end = " ")

    print("\nBackward traversal: ", end="")
    listIterator.last()
    while listIterator.hasPrevious(): 
            print(listIterator.previous(), end=" ")

    print("\nInserting 10 before 3: ", end="")
    listIterator.first()
    for count in range(3):
            listIterator.next()
    listIterator.insert(10)
    print(lyst)
    print("Removing 2: ", end="")
    listIterator.first()
    for count in range(2): 
            listIterator.next()
    listIterator.remove()
    print(lyst)

    print("Replace all items with 0: ", end="")
    listIterator.first()
    while listIterator.hasNext():
            listIterator.next()
            listIterator.replace(0)
    print(lyst)
    
    print("Removing all items (reverse): Expect []: ", end = "")
    listIterator.last()
    while listIterator.hasPrevious():
                listIterator.previous()
                listIterator.remove()
    print(lyst)
    print("Length:", len(lyst))
    
    print("Insert 1's everywhere: ", end="")
    for i in range(1, 10):
        listIterator.insert(1)
        listIterator.next()
    print(lyst)

    print("Removing all items (forward): Expect []: ", end = "") 
    listIterator.first()
    while listIterator.hasNext():
                listIterator.next()
                listIterator.remove()
    print(lyst)
    print("Length:", len(lyst))
    
    print("Insert 2's everywhere: ", end="")
    for i in range(1, 10):
        listIterator.insert(2)
        listIterator.next()
    print(lyst)
    
    print("Removing all items: Expect []: ", end = "")
    listIterator.first()
    while listIterator.hasNext():
            listIterator.next()
            listIterator.remove()
    print(lyst)
    print("Length:", len(lyst))
    
if __name__ == '__main__':
    main(LinkedList)


    
