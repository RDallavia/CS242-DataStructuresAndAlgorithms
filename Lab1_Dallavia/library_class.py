#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ryan C. Dallavia
Lab 1
CS-242 Summer 2018
6/11/2018

The following program simulates a virtual library and its file system. 
Books and patrons are created using imported Book and Patron classes. 
Method defined below, in addition to those from imported classes, permit
the user to add/remove books to/from the library collection, add/remove patrons
to/from the system, permit patrons to checkout/return books, and determine 
whether or not a book or patron exists in the system. 
"""
from patron_class import Patron
from book_class import Book

class Library(object):
    '''
    Class simulates file system for library.  It is the controller -- though
    not official 'parent' class -- of the above imported Book and Patron classes
    on which it relies.
    '''
    
    def __init__(self, libraryBooks):
        '''Instantiates Library class with iterable (list) of book objects'''
        self.books = libraryBooks
        self.patrons = []
        # database pairing patrons & the books they checkout
        self.db = {}
    
    def addBook(self, book):
        '''
        Input: Book object
        Output: None
        Adds book object to library collection
        '''
        if book not in self.books:
            self.books.append(book)
    
    def addPatron(self, patron):
        '''
        Input: Patron object
        Output: None
        Adds patron object to master list and as key to library db with
        empty list as value, which will hold book objects checked out
        '''
        if patron not in self.patrons:
            self.patrons.append(patron)
        if patron not in self.db:
            self.db[patron] = []
    
    def removeBook(self, book):
        '''
        Input: Book object
        Output: None
        Removes book object from library system & decouples from
        patrons if assigned.
        '''
        if book in self.books:
            self.books.remove(book)
        for patron, book_list in self.db.items():
            if len(book_list):
                for assigned_book in book_list:
                    if book == assigned_book:
                        # reduce patron book count and remove from 
                        # patron db list
                        patron.returnBook(book)
                        book_list.remove(book)
    
    def removePatron(self, patron):
        '''
        Input: Patron object
        Output: None
        Deletes patron object from system & marks books as returned
        '''
        if self.findPatron(patron):
            self.patrons.remove(patron)
        if patron in self.db:
            books_out = self.db[patron]
            for book in books_out:
                patron.returnBook(book)
            del self.db[patron]
    

    def findBook(self, book):
        '''
        Input: Book object
        Output: Returns True if book is in library collection, else False
        '''
        if book in self.books:
            return True
        else:
            return False
    
    def findPatron(self, patron):
        '''
        Input: Patron object
        Output: Returns True if patron object exists in system, else False
        '''
        if patron in self.patrons:
            return True
        else:
            return False
    
    def borrowBook(self, book, patron):
        '''
        Input: Book object & patron Object
        Output: None
        If book and patron in system, book eligible for checkout, and patron has not overborrowed,
        then book assigned to patron, else patron placed on book's waitlist or error message.
        '''
        if self.findBook(book) and self.findPatron(patron):
            # book eligible to be borrowed if not already assigned, no waitlist, or patron has < 3 books
            if book.assigned_patron == None and not len(book.waitListObjs) and not patron.isMax():
                book.borrow(patron)
                patron.addBook(book)
                self.db[patron].append(book)
            else:
                book.borrow(patron)
        elif not self.findBook(book):
            print("Book not in stock.\n")
        else:
            print("Patron not found.\n")
    
    def returnBook(self, book):
        '''
        Input: Book object
        Output: None
        Removes book from patron db entry and reduces patron book count when 
        book returned to library. 
        '''
        if self.findBook(book):
            for patron, books in self.db.items():
                for text in books:
                    if book == text:
                        self.db[patron].remove(book)
                        patron.returnBook(book)
                        break
            print("Returned: " + Book.__str__(book))
            book.assigned_patron = None
        else:
            print("Book not found in library collection.\n")

    def __str__(self):
        '''
        Utilizes __str__ methods from Book and Patron classes to print library
        state
        '''
        book_string = ""
        patron_string = "\nPatrons:\n"
        
        if len(self.books):
            for book in self.books:
                book_string += Book.__str__(book) + "\n"
                
        if len(self.patrons):
            for patron in self.patrons:
                patron_string += Patron.__str__(patron) + "\n"
        
        return "Books:\n" + book_string + "\n" + patron_string

def main():        
    book1 = Book("Of Mice and Men", "Steinbeck")
    book2 = Book("The Great Gatsby", "Fitzgerald")
    book3 = Book("1984", "Orwell")
    book4 = Book("One Flew Over the Cuckoo's Nest", "Kesey")
    book5 = Book("The Sheltering Sky", "Bowles")
    book6 = Book("The Mayor of Casterbridge", "Hardy")
    book7 = Book("Dracula", "Stoker")
    book8 = Book("The Bell Jar", "Plath")

    libraryBooks = []
    libraryBooks.append(book1)
    libraryBooks.append(book2)
    libraryBooks.append(book3)
    libraryBooks.append(book4)
    libraryBooks.append(book5)
    libraryBooks.append(book6)
    libraryBooks.append(book7)
        
    patron1 = Patron("Ivan")
    patron2 = Patron("Jimmy")
    patron3 = Patron("Bob")
    patron4 = Patron("Mark")
    patron5 = Patron("Ryan")
        
    myLibrary = Library(libraryBooks)
    myLibrary.addPatron(patron1)
    myLibrary.addPatron(patron2)
    myLibrary.addPatron(patron3)
    myLibrary.addPatron(patron4)
    
    print("""Expected: Ivan borrows 'Of Mice and Men' and total books out for
          Ivan goes to one. All other books in library not checked out and 
          waitlists empty.""")
    myLibrary.borrowBook(book1, patron1)
    print(str(myLibrary))
    print("\n")
    
    print("""Expected: Bob tries to borrows 'Of Mice and Men' and waitlisted.
          Ivan borrows Gatsby. Bob tries to borrow Gatsby and gets waitlisted. 
          All other books in library remain unchecked with waiting lists empty. 
          Ivan has two books, and Bob is on two waitlists.""")
    myLibrary.borrowBook(book1, patron3)
    myLibrary.borrowBook(book2, patron1)
    myLibrary.borrowBook(book2, patron3)
    print(str(myLibrary))
    print("\n")
    
    print("""Expected: Bob borrows 1984, Cuckoo's Nest, The Sheltering Sky. 
          Bob's book count goes to three. Bob remains on two waiting lists:
          Of Mice and Men and Gatsby. Ivan retains two books, and Bob now has three.""")
    myLibrary.borrowBook(book3, patron3)
    myLibrary.borrowBook(book4, patron3)
    myLibrary.borrowBook(book5, patron3)
    print(str(myLibrary))
    print("\n")
    
    print("""Expected: Bob tries and fails to borrow Dracula. Book count for Bob remains at three. Bob
          remains on two waiting lists. Ivan's data remains unchanged. Two books have no
          patrons assigned: Mayor of Casterbridge & Dracula.
          Dracula has a waiting list: Bob.""")
    myLibrary.borrowBook(book7, patron3)
    print(str(myLibrary))
    print("\n")
    
    print("""Expected: Mark tries to checkout Mayor of Casterbridge and Dracula. 
          Mark is assigned Mayor of Casterbridge and waitlisted behind Bob for Dracula. 
          Mark tries to fool the system by checking out the Mayor of Casterbridge 
          again, thus putting himself on the waitinglist for a book he has already borrowed; 
          he fails. Ivan has two books, Bob has three books, and Mark has one book. 
          Bob is on three waiting lists, and Mark is on one.""")
    myLibrary.borrowBook(book6, patron4)
    myLibrary.borrowBook(book7, patron4)
    myLibrary.borrowBook(book6, patron4)
    print(str(myLibrary))
    print("\n")
    
    print("""Expected: Ivan, Jimmy, and Mark go on the waiting list for The Sheltering Sky.
          Ivan has two books, Jimmy has zero books, Bob has three books, Mark has one book. 
          Ivan is on one waiting list, Bob is on three waiting lists, Mark is on two
          waiting lists, and Jimmy is on 1.""")
    myLibrary.borrowBook(book5, patron1)
    myLibrary.borrowBook(book5, patron2)
    myLibrary.borrowBook(book5, patron4)
    print(str(myLibrary))
    print("\n")
    
    print("""Expected: Mark returns Mayor of Caterbridge and has no books left. He 
          remains on two waiting lists.""")
    myLibrary.returnBook(book6)
    print(str(myLibrary))
    print("\n")
    
    print("""Expected: The Sheltering Sky is dropped from the system. Bob no longer has it,
          therefore, his book count drops to two and the waitlist consisting of Ivan, 
          Jimmy, and Mark is destroyed. findBook method subsequently returns False.
          Ivan continues to have two books. Bob now has two books.""")
    myLibrary.removeBook(book5)
    print(str(myLibrary))
    print(myLibrary.findBook(book5))
    print("\n")
    
    print("""Expected: Ivan's account removed from system. Of Mice and Men and 
          Gatsby no longer assigned to anyone, but Bob remains on their respective
          waiting lists. Ivan disappears from list of patrons. Bob has two books.
          A findPatron method search for Ivan returns False""")
    myLibrary.removePatron(patron1)
    print(str(myLibrary))
    print(myLibrary.findPatron(patron1))
    print("\n")
    
    print("""Expected: Error message when someone attempts to checkout a book 
          not yet added to system, but perhaps physically present.""")
    myLibrary.borrowBook(book8, patron2)
    print(str(myLibrary))
    print("\n")
    
    print("""Expected: Error message when someone not added to system 
          attempts to check out book.""")
    myLibrary.borrowBook(book6, patron5)
    print(str(myLibrary))
    print("\n")

    
    
if __name__ == '__main__':
    main()

        
                
                    
            
    
    
    
            