# aggregation represent a relation where one object (the whole)
#                  contains refrences to one or more independent objects (the parts)

class library:
    def __init__(self,name):
        self.name=name
        self.books = []


    def add_book(self,book):
        self.books.append(book)  


    def list_books(self):
        return[f"{book.title}by {book.author}"for book in self.books]      


class book:
    def __init__(self,title,author):
        self.title = title
        self.author=author


library = library("new york public library")

book1 = book("harry potter","jk")
book2 = book("the hobbit","tolken")
book3 = book("the color","terry")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)
print(library.list_books())

