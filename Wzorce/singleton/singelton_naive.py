# class Book:
#     def __init__(self, title: str, pages_number: int):
#         self.title = title
#         self.pages_number = pages_number
#
#
# if __name__ == '__main__':
#     book_1 = Book('Harry Potter', 500)
#     book_2 = Book('Star Wars', 600)
#     print(book_1)
#     print(book_2)


class Singleton:
    __instance = None

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

    def __init__(self):
        if not self.__instance:
            print('First object of the class, shared instance doesn\'t exist yet.')
        self.val = 0

    def print_val(self):
        print(self.val)

if __name__ == '__main__':
    a = Singleton.get_instance()
    a.print_val()
    a.val = 10
    a.print_val()

    b = Singleton.get_instance()
    b.print_val()

    print(a,b) # same address