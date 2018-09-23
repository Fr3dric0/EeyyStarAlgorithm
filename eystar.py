import heapq

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


def map_neighbors(board):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if x > 0:
                node = board[y][x]
                # To the right
                node.add_neighbor(board[y][x-1])
                # Node to the right gets a reference to it's node to the left
                board[y][x-1].add_neighbor(node)

            if y > 0:
                # Over
                node.add_neighbor(board[y-1][x])
                # Node over gets a reference to the node bellow
                board[y - 1][x].add_neighbor(node)


def calc_heuristic(board, goal_node):
    for row in board:
        for node in row:
            # Keep the infinite heuristic on walls
            if node.symbol == '#':
                continue

            # Else update the heuristic with the manhattan distance
            node.h = manhattan_heuristic(node.x, node.y, goal_node)


def best_first_search(board, start_node):
    closed = set()
    # Must be in sorted order
    open = list()

    g = start_node.g
    f = start_node.f
    n0 = start_node

    open.append(n0)

    solved = False
    while not solved:
        if not len(open):
            raise ValueError('Could not find a solution')

        x: Node = open.pop()
        closed.add(x)

        if x.is_goal():
            return x


def eystar(filename):
    lines = readfile(filename)
    print('\n'.join(lines))
    board, start_node, goal_node = create_board(lines)
    calc_heuristic(board, goal_node)
    map_neighbors(board)

    n = start_node
    for i in range(5):
        n.visited = True
        print(n)
        if not n.neighbors:
            raise TypeError('Node has no more neigbors')

        if not n.neighbors[0].visited:
            n = n.neighbors[0]
        else:
            n = n.neighbors[1]

    # print(f'Current: {start_node}')
    # for n in start_node.neighbors:
    #     print(n)

    closed = set()
    open = set()

    # for y in range(len(board)):
    #     for x in range(len(board[y])):
    #
    #         if x < len(board[y]) - 1:
    #             print(f'{board[y][x].symbol} {board[y][x+1].symbol}|', end='')
