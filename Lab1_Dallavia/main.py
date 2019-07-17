#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 07:57:14 2018

@author: RCD
"""
from book_class import Book
from patron_class import Patron
from library_class import Library

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
    
    print("""Expected: Bob tries to borrows 'Of Mice and Men' and is waitlisted.
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
    
    print("""Expected: Bob tries and fails to borrow Dracula. Book count for Bob 
          remains at three. Bob is added to Dracula waiting list and remains on 
          two others. Ivan's data remains unchanged. Two books have no
          patrons assigned: Mayor of Casterbridge & Dracula.""")
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
          A findPatron method search for Ivan returns False.""")
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