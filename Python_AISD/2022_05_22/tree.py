from collections import deque


class Tree:
    def __init__(self, key, value):
        self.children = []
        self.key = key
        self.value = value


def bfs(node, f):
    q = deque([node])
    while q:
        current = q.pop()
        q.extend(current.children)
        f(current.children)

def dfs(node, f):

