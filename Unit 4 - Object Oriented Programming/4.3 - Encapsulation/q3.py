"""
Author: Dinesh Sinnathamby
Date: April 21st, 2026
Description: Simple program demonstrating the use of a Book class, 
"""

class Book:
    def __init__(self, title, author, publisher):
        self.__title = title
        self.__author = author
        self.__publisher = publisher

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_publisher(self):
        return self.__publisher

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_publisher(self, publisher):
        self.__publisher = publisher

    def __str__(self):
        return ("Book Details:" + "\n" +
                "Title: " + self.__title + "\n" +
                "Author: " + self.__author + "\n" +
                "Publisher: " + self.__publisher)

def main():
    my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", "Charles Scribner's Sons")
    
    print("Initial State:")
    print(my_book)
    
    my_book.set_publisher("Penguin Books")
    
    print(my_book.get_publisher())
    
    print(my_book)

main()