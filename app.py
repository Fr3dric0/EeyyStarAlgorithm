
from node import Node


def manhattan_heuristic(x, y, goal: Node):
    return abs(x - goal.x) + abs(y - goal.y)


def readfile(path):
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]


def create_board(lines):
    board = []
    start_node = None
    goal_node = None

    for y in range(len(lines)):
        row = []
        for x in range(len(lines[y])):
            node = Node(x, y, lines[y][x])

            if node.symbol == 'B':
                goal_node = node
            elif node.symbol == 'A':
                start_node = node

            row.append(node)
        board.append(row)

    return board, start_node, goal_node


def calc_heuristic(board, goal_node):
    for row in board:
        for node in row:
            # Keep the infinite heuristic on walls
            if node.symbol == '#':
                continue

            # Else update the heuristic with the manhattan distance
            node.h = manhattan_heuristic(node.x, node.y, goal_node)


def main():
    lines = readfile('boards/board-1-1.txt')
    board, start_node, goal_node = create_board(lines)

    calc_heuristic(board, goal_node)

    closed = set()
    open = set()

    for b in board:
        for n in b:
            print(n)


main()
