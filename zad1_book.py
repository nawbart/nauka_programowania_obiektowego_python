class book:

    def __init__(self, title, author, yrOfPublishment, nbrOfPages, owner):
        self.title = title
        self.author = author
        self.yrOfPublishment = yrOfPublishment
        self.nbrOfPages = nbrOfPages
        self.owner = owner

    def newOwner(self, newOwner):
        self.owner = newOwner


HP = book('Harry Potter', 'J.K Rowling', 1998, 499, 'Bartek')
LoR = book('Lords of Rings', 'J.R.R Tolkien', 1995, 350, 'Michał')
GM = book('Green Mile', 'S.King', 1996, 730, 'Kamila')

list_of_books = []



list_of_books.append(HP)
list_of_books.append(LoR)
list_of_books.append(GM)

for i in list_of_books:
    print('*********','\nTitle: ',i.title, '\nAuthor: ', i.author,'\nYear of publishment: ', i.yrOfPublishment, '\nNumber of pages:', i.nbrOfPages,'\nOwner: ', i.owner)
