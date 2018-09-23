import sys


class Node:
    def __init__(self, x, y, symbol='#'):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.g = 0
        self.h: int = sys.maxsize

        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.neighbors = []

        self.visited = False

    def __str__(self):
        return f'Node(x: {self.x}, y: {self.y}, symbol: {self.symbol}, g: {self.g}, h: {self.h})'

    def add_neighbor(self, node):
        self.neighbors.append(node)
        # Ensure that the minimum item comes first
        self.neighbors = sorted(self.neighbors, key=lambda n: n.f)

    def is_goal(self):
        return self.h == 0

    def set_h(self, h):
        self.h = h

    @property
    def f(self):
        return self.g + self.h