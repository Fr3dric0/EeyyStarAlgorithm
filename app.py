import sys
from eystar import eystar
from image import project_board_to_image
from node import Node


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


def print_best_path(goal: Node, start: Node):
    if not goal:
        return None

    print(f'Goal: {goal}')

    node = goal
    while node.parent != start:
        node = node.parent
        print(f'\t{node}')

    print(f'Start: {node.parent}')


def project_best_path(board, goal: Node, start: Node):
    new_board = []
    steps = 0

    for row in board:
        new_board.append(list(map(lambda n: n.symbol, row)))

    if goal is not None:
        node = goal
        while node.parent is not None and node.parent != start:
            node = node.parent
            new_board[node.y][node.x] = 'o'

            steps += 1

    for row in new_board:
        for col in row:
            print(col, end='')
        print()

    print(f'Path length: {steps}')

    return new_board


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else None

    if filename is None:
        print('You need to specify filepath to board when calling this script')
        sys.exit(1)

    lines = readfile(filename)
    board, start_node, goal_node = create_board(lines)

    goal, opened, closed = eystar(board, start_node, goal_node)

    print_best_path(goal, start_node)
    solution = project_best_path(board, goal, start_node)

    project_board_to_image(solution, filename.replace('boards/', ''))


if __name__ == '__main__':
    main()
