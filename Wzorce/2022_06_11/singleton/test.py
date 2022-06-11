class Book:
    def __init__(self):
        self.title = '1234'
        self._iban = "12412"
        self.__secret = '1245151124124'

book = Book()
print(book.title)
print(book._iban)
print(book.__class__.__secret) # brak możliowści8 dostania sie
