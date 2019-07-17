#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ryan C. Dallavia
Exercise 1
CS-242 Summer 2018
6/11/2018

This class is responsible for the instantiation of Patron objects
utiized by both the Book and Library classes. See accompanying main()
file, which validates the methods contained herein. Note, docstrings
designating 'Output: None' indicates the return type/value of the method. 
"""

class Patron(object):
    
    # max number of books patrons can checkout at one time
    LIMIT = 3
    
    def __init__(self, name):
        '''Instantiation requries patron name as string'''
        self.name = name
        self.numBooks = 0
        # local storage for books borrowed
        self.bookObjs = []
    
    def addBook(self, bookObj):
        '''
        Input: Book object
        Output: None
        Increments book count on book borrow, if possible. Ensures book is
        not borrowed twice. 
        '''
        if self.numBooks < Patron.LIMIT and not len(bookObj.waitListObjs):
            if bookObj not in self.bookObjs:
                self.numBooks += 1
                self.bookObjs.append(bookObj)

    def isMax(self):
        '''
        Input: None; Attaches to instance of class. 
        Output: True, and error message, if user has checkedout
        max number of books
        '''
        if self.numBooks >= Patron.LIMIT:
            #print("Can't borrow more books -- MAX REACHED!")
            return True
        else:
            return False
        
    # add bookObj as parameter and use remove method on list if you intend to keep this here
    def returnBook(self, bookObj):
        '''
        Input: Book object
        Output: None
        Reduces patron book count when book returned to library and 
        removes from local storage.
        '''
        if bookObj in self.bookObjs and self.numBooks > 0:
            self.numBooks -= 1
            self.bookObjs.remove(bookObj)
            bookObj.assigned_patron = None

    def __str__(self):
        return self.name + " has " + str(self.numBooks) + " books."