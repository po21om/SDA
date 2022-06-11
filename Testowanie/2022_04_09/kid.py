class Kid:
    def __init__(self, first_name, second_name):
        self._first_name = first_name
        self._second_name = second_name
        self._marks = []
    def __str__(self):
        return f"{self._first_name} {self._second_name}"
    def get_mark(self, mark):
        self._marks.append(mark)

dziecko = Kid(first_name="Jacek", second_name="Placek")
print(dziecko)