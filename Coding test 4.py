class Book:
    def __init__(self,title,author,is_borrowed = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed 

    def borrow(self):
        if self.is_borrowed == False:
            print("You did not borrowed this book.")

        else:
            print("You borrowed this book.")

    def return_book(self):
        if self.is_borrowed == False:
            print("You returned the book.")

        else:
            print("You did not returned the book.")

book1 = Book("Queen of dragons","raj",False)
book1.borrow()
book1.return_book()
book2 = Book("luse","rena",True)
book2.borrow()
book2.return_book()
book3 = Book("wild animals","glenda",False)
book3.borrow()
book3.return_book()

        