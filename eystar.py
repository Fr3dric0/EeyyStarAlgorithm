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


def attach_and_eval(child, parent):
    child.parent = parent
    child.g = parent.f


def propagate_path_improvements(child):
    pass


def update_node(successor: Node, current: Node, goal_node: Node):
    successor.g = current.g + 10
    successor.h = manhattan_heuristic(successor.x, successor.y, goal_node)
    successor.parent = current


def best_first_search(board, start_node, goal_node):
    closed = set()
    # Must be in sorted order
    open = []
    heapq.heapify(open)

    heapq.heappush(open, start_node)

    iterations = 0

    while len(open):
        iterations += 1
        x: Node = heapq.heappop(open)
        print(f'{iterations}. {x}')
        closed.add(x)

        if x.is_goal():
            print(iterations)
            print(x.parent)
            return x

        successors = x.neighbors

        for s in successors:
            if not s.is_wall(len(board[0]), len(board)) and s not in closed:
                if s in open:
                    if s.g > (x.g + 10):
                        update_node(s, x, goal_node)
                else:
                    update_node(s, x, goal_node)
                    heapq.heappush(open, s)

    print(iterations)
    return None


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

    for row in board:
        new_board.append(list(map(lambda n: n.symbol, row)))

    node = goal
    while node.parent != start:
        node = node.parent
        new_board[node.y][node.x] = '⬅'

    for row in new_board:
        for col in row:
            print(col, end='')
        print()


def eystar(filename):
    lines = readfile(filename)
    board, start_node, goal_node = create_board(lines)
    calc_heuristic(board, goal_node)
    map_neighbors(board)

    goal = best_first_search(board, start_node, goal_node)

    print_best_path(goal, start_node)
    project_best_path(board, goal, start_node)
