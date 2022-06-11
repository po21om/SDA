class LinkedList:

    def __init__(self, V, next = None):
        self.V = V
        self.next = next

    def head(self):
        return self.V

    def tail(self):
        return self.next

    def push(self, V):
        return LinkedList(V, self)

    def exist(self, V):
        if V == self.V:
            return True
        if self.next is None:
            return False
        return self.next.exist(V)

    def map(self, f):
        if self.next is None:
            return LinkedList(f(self.V))
        return LinkedList(f(self.V), self.next.map(f))

    def filter(self, f):
        if f(self.V):
            return LinkedList(self.V, self.next.filter(f))
        if self.next is None:
            return None
        return self.next.filter(f)

    def insert(self, V, i):
        if i < 1:
            return LinkedList(V, self)
        return LinkedList(self.V, self.next.insert(V, i - 1))


link = LinkedList(1)
link = link.push(2)
link = link.push(3)
link.map(print)
