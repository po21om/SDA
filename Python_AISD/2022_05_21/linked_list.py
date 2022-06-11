class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


l_list = LinkedList()
print(l_list)

node_1 = Node('1')
l_list.head = node_1
print(l_list)

node_2 = Node('2')
node_1.next = node_2
print(l_list)

node_3 = Node('3')
node_2.next = node_3
print(l_list)
