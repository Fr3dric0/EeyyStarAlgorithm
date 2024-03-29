import sys

WEIGHTS = {
    # Wall
    '#': sys.maxsize,
    # Water
    'w': 100,
    # Mountains
    'm': 50,
    # Forests
    'f': 10,
    # Grasslands
    'g': 5,
    # Roads
    'r': 1,
    # Floor
    '.': 1
}


def get_path_weight(symbol: str) -> int:
    return WEIGHTS[symbol] if symbol in WEIGHTS else 0


class Node:
    def __init__(self, x, y, symbol=None):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.g = get_path_weight(symbol)
        # Heuristics has to be set initially in a sensible way
        self.h: int = sys.maxsize

        self.parent = None
        self.visited = False

    def __str__(self):
        return f'Node(x: {self.x}, y: {self.y}, symbol: {self.symbol}, g: {self.g}, h: {self.h})'

    def is_wall(self):
        return self.symbol == '#'

    def is_goal(self):
        return self.h == 0

    def set_h(self, h):
        self.h = h

    @property
    def f(self):
        return self.g + self.h

    def __lt__(self, other):
        """
        Used by heapq to sort the elements.
        Ensures that the smallest f value is last in the heap.
        """
        return self.f < other.f
