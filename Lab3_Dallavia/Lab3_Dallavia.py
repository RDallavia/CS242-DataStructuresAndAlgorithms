#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ryan C. Dallavia
CS242 - Summer 2018
06/25/1018
Lab 4

The following program defines a function makeTwoWay, which takes as its sole
argument a singly-linked list.  The function returns a doubly-linked list
containing the same data elements as the function's argument.  The original 
singly-linked list is left unmutated. 

"""

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class DoubleNode(object):
    def __init__(self, data=None, previous=None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous
    
    def __str__(self):
        return "Next " + str(self.next)

class LinkedList(object):
    '''Instantiaties a singly linked list'''
    def __init__(self): 
        self.head = None
        self.size = 0
    
    def addNode(self, data):
        '''Adds node to end of linked list'''
        # Lambert, Kenneth A (2014) "Fundamentals of Python: Data Structures"
        new_node = Node(data, None)
        if self.head == None:
            self.head = new_node
        else:
            probe = self.head
            while probe.next != None:
                probe = probe.next
            probe.next = new_node
        self.size += 1
    
    def __len__(self):
        '''Returns length of linked list'''
        return self.size
    
    def __iter__(self):
        '''Supports iteration over linked list'''
        # Lambert, Kenneth A (2014) "Fundamentals of Python: Data Structures"
        probe = self.head
        while not probe is None:
            yield probe.data
            probe = probe.next
    
    def __str__(self):
        linked_list = "Head-->"
        probe = self.head
        for i in range(self.size):
            linked_list += str(probe.data) + "-->"
            probe = probe.next
        linked_list += "None"
        return linked_list

class DoublyLinkedList(object):
    '''Instantiaties a singly linked list'''
                
    def __init__(self):
        # Pointer setup from Goodrich et al. (2013)
        self.head = None
        self.tail = self.head
        self.size = 0
    
    def addNode(self, data):
        if self.size == 0 and self.head == self.tail:
            self.head = DoubleNode(data, self.tail)
            self.tail = self.head
        else:
            # Lambert, Kenneth A (2014) "Fundamentals of Python: Data Structures"
            probe = self.head
            while probe.next != None:
                probe = probe.next
            probe.next = DoubleNode(data, self.tail)
            self.tail = self.tail.next
        self.size += 1
            
    def __len__(self):
        '''Returns length of linked list'''
        return self.size
    
    def __iter__(self):
        '''Supports iteration over linked list'''
        # Lambert, Kenneth A (2014) "Fundamentals of Python: Data Structures"
        cursor = self.head
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        linked_list = "Head-->"
        probe = self.head
        for i in range(self.size):
            linked_list += str(probe.data) + "<-->"
            probe = probe.next
        linked_list += "None\n" + "Tail-->" + str(self.tail.data)
        return linked_list


def makeTwoWay(linked_list):
    doubly_linked = DoublyLinkedList()
    for item in linked_list:
        doubly_linked.addNode(item)
    return doubly_linked


def main():
    # generate linked list
    linked_list = LinkedList()
    for datum in range(5):
        linked_list.addNode(datum)
    print("Linked List")
    print("-------------------------------------------")
    print(linked_list)
    print("\n")
    #create doubly-linked list from singly-linked list
    print("Doubly-Linked List")
    print("-------------------------------------------")
    dbl_list = makeTwoWay(linked_list)
    print(dbl_list)

if __name__ == '__main__':
    main()

            
        
        
    
        

        
    