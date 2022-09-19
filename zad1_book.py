class Book:

    def __init__(self, title: str, author: str, yrOfPublishment: int, nbrOfPages: int, owner_name: str ):
        self.title = title
        self.author = author
        self.yrOfPublishment = yrOfPublishment
        self.nbrOfPages = nbrOfPages
        self.owner_name = owner_name

    def set_owner_name(self, owner_name):
        self.owner_name = owner_name


HP = Book('Harry Potter', 'J.K Rowling', 1998, 499, 'Bartek')
LoR = Book('Lords of Rings', 'J.R.R Tolkien', 1995, 350, 'Przemysław')
GM = Book('Green Mile', 'S.King', 1996, 730, 'Kamila')

list_of_books = []

list_of_books.append(HP)
list_of_books.append(LoR)
list_of_books.append(GM)

for i in list_of_books:
    print('*'*15,'\nTitle: ',i.title, '\nAuthor: ', i.author,'\nYear of publishment: ', i.yrOfPublishment, '\nNumber of pages:', i.nbrOfPages,'\nOwner: ', i.owner_name)
