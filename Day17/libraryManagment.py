# Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!

class library:
    def __init__(self):
        self.books= []
        self.noBooks = 0

    def addBook(self,book):
        self.books.append(book)  
        self.noBooks +=1 
    def showInfo(self):
        print(f"The library has {self.noBooks} books ")   
        for book in self.books:
            print(book)
            

l1= library()
l1.addBook("Harry Potter 1")
l1.addBook("Harry Potter 2")
l1.showInfo()