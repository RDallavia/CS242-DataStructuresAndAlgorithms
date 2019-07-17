#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ryan C. Dallavia
Exercise 1
CS-242 Summer 2018
6/11/2018

The following class models a book object. It relies on the Patron class and supports the 
Library class. The borrow method anticipates a patron object
(i.e., someone to do the borrowing). Aside from having a title, author, assigned_patron
(if checked out), each book is equipped with a waiting list implemented with a queue.
Books not signed out, but with a waiting list, are ineligible for checkout.
Note, docstrings designating 'Output: None' indicates the return type/value
of the method.  
"""

from collections import deque
from patron_class import Patron

class Book(object):
    '''Instantiates Book objects for use with Library Class. Expects Patron objects
    from Patron class and partially relies on Patron.__str__ to generate output '''
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.assigned_patron = None
        self.waitListObjs = deque()
        # saves patron object passed to borrow method for future use
        self.patron = None
    
    def borrow(self, patron):
        '''
        Input: Patron object
        Output: None
        Assigns patron name to book and stores patron, if book unassigned, 
        has no waiting list, and patron not at max borrowing limit. Else, 
        patron added to waiting list implemented as queue. 
        '''
        if not self.assigned_patron and not len(self.waitListObjs):
            if not patron.isMax():
                self.assigned_patron = patron.name
                self.patron = patron
            else:
                self.waitListObjs.append(patron)
        # prevent attempted double reborrowing and double waitlisting
        elif patron.name != self.assigned_patron and patron not in self.waitListObjs:
            self.waitListObjs.append(patron)
            
    def __str__(self):
        '''
        Prints book titles, individuals who have borrowed books, and accompanying 
        waiting lists. Relies in part on __str__ method from Patron class. 
        '''
        waiting_string = "Waiting:\n\t"
        if not len(self.waitListObjs):
            waiting_string += "Waiting list empty.\n"
        else:
            for i in range(len(self.waitListObjs)):
                waiting_string += str(i+1) + "." + " " + self.waitListObjs[i].name + " has " + str(self.waitListObjs[i].numBooks) + " book(s).\n\t"
        if self.assigned_patron:    
            return self.title + ", " + self.author + " in care of: " + Patron.__str__(self.patron) + "\n"\
            + waiting_string
        else:
            return self.title + ", " + self.author + " has not been borrowed.\n" + waiting_string 

