from SearchNode import SearchNode
import heapq


class AStar:

    def __init__(self, board):
        self.board = board
        self.goal = board.goalPos
        self.start = board.startPos
        self.open = []
        self.closed = []

    def initialize(self):
        start_node = SearchNode(self.start)
        start_node.g = 0
        start_node.h = self.calculate_heuristics(self.start, self.goal)
        start_node.f = start_node.g + start_node.h
        self.open.append(start_node)
        heapq.heapify(self.open)

    def calculate_heuristics(self, state, goal):
        x_val = abs(state[0] - goal[0])
        y_val = abs(state[1] - goal[1])
        return x_val + y_val

    def get_cost(self, node):
        x = node.state[0]
        y = node.state[1]
        elem = self.board.board[y][x]
        return {'w': 100,
                'm': 50,
                'f': 10,
                'g': 5,
                'r': 1,
                }.get(elem, 1)

    def generate_neighbours(self, node):
        x = node.state[0]
        y = node.state[1]

        self.generate_node(x - 1, y, node)
        self.generate_node(x + 1, y, node)
        self.generate_node(x, y - 1, node)
        self.generate_node(x, y + 1, node)

    def generate_node(self, x, y, node):
        child = SearchNode((x, y))
        exists = self.get_if_exists(child)

        if exists is not None:
            node.kids.append(exists)

        if self.is_valid(x, y):
            if exists is None:
                node.kids.append(child)
                self.attach_and_eval(node, child)
                heapq.heappush(self.open, child)
                heapq.heapify(self.open)

            elif node.g + self.get_cost(child) < child.g:
                self.attach_and_eval(node, child)
                if child in self.closed:
                    self.propagate_path_improvements(child)

    def attach_and_eval(self, node, child):
        child.parent = node
        child.g = (node.g + self.get_cost(child))
        child.h = self.calculate_heuristics(child.state, self.goal)
        child.f = child.g + child.h

    def propagate_path_improvements(self, node):
        for kid in node.kids:
            if node.g + self.get_cost(kid) < kid.g:
                kid.parent = node
                kid.g = node.g + self.get_cost(kid)
                self.propagate_path_improvements(kid)

    def is_valid(self, x, y):
        if (x < 0) or (y < 0):
            return False
        if (x >= self.board.width) or (y >= self.board.height):
            return False
        if self.board.board[y][x] == '#':
            return False

        return True

    def get_if_exists(self, node):
        for o in self.open:
            if node.state == o.state:
                return o

        for c in self.closed:
            if node.state == c.state:
                return c

        return None

    def generate_path(self, node):
        if node.parent.state is not self.start:
            parent_state = node.parent.state
            x = parent_state[0]
            y = parent_state[1]
            self.board.board[y][x] = 'x'

            self.generate_path(node.parent)

    def display_open_closed(self):
        for o in self.open:
            self.board.board[o.state[1]][o.state[0]] = '*'
        for c in self.closed:
            self.board.board[c.state[1]][c.state[0]] = '+'

    def process(self):
        self.initialize()

        while True:
            if not self.open:
                return -1
            node = heapq.heappop(self.open)
            heapq.heappush(self.closed, node)

            if node.state == self.goal:
                self.display_open_closed()
                self.generate_path(node)
                return 1

            self.generate_neighbours(node)




























