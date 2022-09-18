class book:
    title = ''
    author = ''
    yrOfPublishment = None
    nbrOfPages = None
    owner = ''

    def __int__(self, title, author, yrOfPublishment, nbrOfPages, owner):
        self.title = title
        self.author = author
        self.yrOfPublishment = yrOfPublishment
        self.nbrOfPages = nbrOfPages
        self.owner = owner

    def newOwner(self, newOwner):
        self.owner = newOwner
