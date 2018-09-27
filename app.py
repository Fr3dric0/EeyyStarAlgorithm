import sys
from eystar import eystar
from node import Node
from visualize import generate_board_image


def readfile(path):
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]


def create_board(lines: list) -> (list, Node, Node):
    """
    Takes in a list of strings,
    where the strings is each row in the board.
    Converts this to a matrix of Nodes
    """
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
    """ Prints out all the nodes in the best path in reverse order (from goal, to start) """
    if not goal:
        return None

    steps = 0
    total_weight = 0
    print(f'Goal: {goal}')

    node = goal
    total_weight += node.f

    while node.parent != start:
        steps += 1
        node = node.parent
        total_weight += node.f
        print(f'\t{node}')

    print(f'Start: {node.parent}')
    print(f'Path length: {steps}')
    print(f'Total cost: {total_weight}')


def project_best_path(board, goal: Node, start: Node, opened: list=None, closed: list=None) -> list:
    """
    Projects the best path, including open and closed nodes, onto the board.
    :return: The board containing the best path
    """
    new_board = []

    for row in board:
        new_board.append(list(map(lambda n: n.symbol, row)))

    if opened:
        for node in opened:
            new_board[node.y][node.x] = '*'

    if closed:
        for node in closed:
            new_board[node.y][node.x] = '+'

    if goal is not None:
        node = goal
        while node.parent is not None and node.parent != start:
            node = node.parent
            new_board[node.y][node.x] = 'x'

    return new_board


def get_clean_board(board: list) -> list:
    """
    Retrieves a clean version of the board,
    where only the symbols are kept in each column.
    :return:
    """
    clean = []

    for row in board:
        temp = []
        for node in row:
            temp.append(node.symbol)

        clean.append(temp)

    return clean


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else None

    if filename is None:
        print('You need to specify filepath to board when calling this script')
        sys.exit(1)

    lines = readfile(filename)
    board, start_node, goal_node = create_board(lines)

    goal, opened, closed = eystar(board, start_node, goal_node)

    #print_best_path(goal, start_node)
    solution = project_best_path(board, goal, start_node, opened, closed)

    generate_board_image(get_clean_board(board), solution, filename.replace('boards/', ''), True)


if __name__ == '__main__':
    main()
