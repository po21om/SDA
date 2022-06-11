class BinarySearchTree:
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.left = None
        self.right = None

    def insert(self, new_data, new_key):
        if self.key:
            if new_key < self.key:
                if self.left is None:
                    self.left = BinarySearchTree(new_data, new_key)
                else:
                    self.left.insert(new_data, new_key)
            elif new_key > self.key:
                if self.right is None:
                    self.right = BinarySearchTree(new_data, new_key)
                else:
                    self.right.insert(new_data, new_key)
        else:
            self.key = new_key
            self.data = new_data

    def __repr__(self):
        result = ''
        if self.left:
            result += self.left.__repr__()
        # result += 'key: ' + str(self.key) + ' data: ' + self.data + '\n'
        result += f'key: {self.key} data: {self.data}\n'
        if self.right:
            result += self.right.__repr__()
        return result

    def find_data(self, fkey):
        if fkey < self.key:
            if self.left:
                return self.left.find_data(fkey)
            return None
        elif fkey > self.key:
            if self.right:
                return self.right.find_data(fkey)
            return None
        else:
            return self.data


bst = BinarySearchTree("Luiza", 6)
bst.insert("Anatol", 9)
bst.insert("Józefina", 3)
bst.insert("Emanuel", 12)
bst.insert("Jaskier", 10)
bst.insert("Tifa", 7)
print(bst)

print(bst.find_data(5))
print(bst.find_data(10))