import sys


class Node:
    def __init__(self, x, y, symbol='#'):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.g = 0
        self.h: int = sys.maxsize

    def is_goal(self):
        return self.h == 0

    def set_h(self, h):
        self.h = h


def manhattan_heuristic(x, y, goal: Node):
    return abs(x - goal.x) + abs(y - goal.y)


def readfile(path):
    with open(path, 'r') as f:
        return f.readlines()

    return []


def main():
    print(readfile('boards/board-1-1.txt'))
    pass


main()