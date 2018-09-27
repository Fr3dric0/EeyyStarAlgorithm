import heapq

from node import Node, get_path_weight, WEIGHTS


def manhattan_heuristic(x, y, goal: Node):
    return abs(x - goal.x) + abs(y - goal.y)


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


def update_node(successor: Node, current: Node, goal_node: Node):
    successor.g = current.g + get_path_weight(current.symbol)
    successor.h = manhattan_heuristic(successor.x, successor.y, goal_node)
    successor.parent = current


def find_neighbor(board: list, x: int, y: int, goal_node: Node) -> Node:
    """
    Fetches a single neighbor by the boards (x, y) coordinates,
    and fetches at the same time the initial heuristic.
    :param board:
    :param x:
    :param y:
    :param goal_node:
    :return:
    """
    node = board[y][x]
    node.h = manhattan_heuristic(x, y, goal_node)
    return node


def find_neighbors(board: list, current: Node, goal_node: Node) -> list:
    """
    Identifies all the neighbors to a node on the board.
    The neighbors is pushed to a heap.
    :param board:
    :param current:
    :return:
    """
    neighbors = []
    heapq.heapify(neighbors)

    if current.x < len(board[0]) - 1:
        node = find_neighbor(board, current.x + 1, current.y, goal_node)
        heapq.heappush(neighbors, node)

    if current.x > 0:
        node = find_neighbor(board, current.x - 1, current.y, goal_node)
        heapq.heappush(neighbors, node)

    if current.y > 0:
        node = find_neighbor(board, current.x, current.y - 1, goal_node)
        heapq.heappush(neighbors, node)

    if current.y < len(board) - 1:
        node = find_neighbor(board, current.x, current.y + 1, goal_node)
        heapq.heappush(neighbors, node)

    return heapq.nsmallest(4, neighbors)


def best_first_search(board: list, start_node: Node, goal_node: Node) -> (Node, list, set):
    """
    Finds the Best-First path, from start to goal in a two dimentional
    board of nodes.

    :return: The goal node with references to it's parents (i.e. path back to start),
             the open heap and closed set.
    """
    closed = set()
    # Must be in sorted order
    opened = []
    heapq.heapify(opened)

    heapq.heappush(opened, start_node)

    while len(opened):
        x: Node = heapq.heappop(opened)
        closed.add(x)

        if x.is_goal():
            return x, opened, closed

        successors = find_neighbors(board, x, goal_node)

        for s in successors:
            if not s.is_wall() and s not in closed:
                if s in opened:
                    arc_cost = WEIGHTS[s.symbol] if s.symbol in WEIGHTS else 1
                    if s.g > (x.g + arc_cost):
                        update_node(s, x, goal_node)
                else:
                    update_node(s, x, goal_node)
                    heapq.heappush(opened, s)

    return None, opened, closed


def eystar(board, start_node, goal_node) -> (Node, list, set):
    """
    Uses Best-First-Search with manhattan heuristic to determine the best path
    from a start node to a goal node
    :param board:
    :param start_node:
    :param goal_node:
    :return (Node, list, set): Returns the goal node if found, and the opened and closed list.
                                The opened list is a max-heap and has to be used with heapq
    """
    goal, opened, closed = best_first_search(board, start_node, goal_node)

    return goal, opened, closed
