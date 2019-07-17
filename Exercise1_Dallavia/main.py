#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ryan C. Dallavia
Exercise 1
CS-242 Summer 2018
6/11/2018

Driver code for Book and Patron Classes
"""

from book_class import Book
from patron_class import Patron

def main():
    
    books = []
    book1 = Book("The Berlin Stories", "Isherwood")
    book2 = Book("Postcards from the Edge", "Fisher")
    book3 = Book("The Bell Jar", "Plath")
    book4 = Book("Patriot Games", "Clancy")
    book5 = Book("Ruby Fruit Jungle", "Brown")
    
    books.append(book1)
    books.append(book2)
    books.append(book3)
    books.append(book4)
    books.append(book5)
    
    patrons = []
    patron1 = Patron("Mark")
    patron2 = Patron("Sarah")
    patron3 = Patron("Ryan")
    patron4 = Patron("Jack")
    
    patrons.append(patron1)
    patrons.append(patron2)
    patrons.append(patron3)
    patrons.append(patron4)
    
    print("""Expected: Mark borrows max number of books (3).\n""")
    book1.borrow(patron1)
    patron1.addBook(book1)
    book2.borrow(patron1)
    patron1.addBook(book2)
    book3.borrow(patron1)
    patron1.addBook(book3)

    
    for book in books:
        print(book)
    
    print("""Expected: Mark prevented from borrowing too many books and
          added to waitlist for Patriot Games instead.\n""")
    book4.borrow(patron1)
    patron1.addBook(book4)
    
    for book in books:
        print(book)
        
    print("""Expected: Jack is added to the waiting list for Patriot Games 
          behind Mark.\n""")
    book4.borrow(patron4)
    patron4.addBook(book4)
    
    for book in books:
        print(book)
    
    print("""Expected: Ryan tries to borrow Ruby Fruit Jungle twice and 
          is blocked by system.\n""")
    book5.borrow(patron3)
    patron3.addBook(book5)
    book5.borrow(patron3)
    patron3.addBook(book5)

    
    for book in books:
        print(book)
    
    print("""Expected: True -- Indicating Mark has borrowed max number 
          of books.\n""")
    print(patron1.isMax())
    print("\n")
    
    print("""Expected: Mark returns The Bell Jar. His book count declines 
          from three to two.\n""")
    patron1.returnBook(book3)
    
    for book in books:
        print(book)
    

if __name__ == '__main__':
    main()