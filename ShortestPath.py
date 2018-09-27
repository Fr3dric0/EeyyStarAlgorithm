from SearchNode import SearchNode
import heapq

def calculate_heuristics(state, goal):
    x_val = abs(state[0] - goal[0])
    y_val = abs(state[1] - goal[1])
    return x_val + y_val

class ShortestPath:

    def __init__(self, board, algorithm_type):
        self.board = board
        self.algorithm = algorithm_type
        self.goal = board.goal_position
        self.start = board.start_position
        self.open = []
        self.closed = []

    def initialize(self):
        start_node = SearchNode(self.start)
        start_node.g = 0
        start_node.h = calculate_heuristics(self.start, self.goal)

        # Make open list a priority queue if algorithm is a-star or dijkstra
        if self.algorithm in [0, 2]:
            if self.algorithm == 0:
                start_node.f = start_node.g + start_node.h
            else:
                # Let f value equal g value for comparison in priority queue
                start_node.f = start_node.g

            heapq.heapify(self.open)
            heapq.heappush(self.open, start_node)

        # Keep open list as list object if algorithm is BFS
        if self.algorithm == 1:
            self.open.append(start_node)

    def get_cost(self, node):
        x = node.state[0]
        y = node.state[1]
        elem = self.board.grid[y][x]
        return {
            # Water
            'w': 100,
            # Mountain
            'm': 50,
            # Forrest
            'f': 10,
            # Grass
            'g': 5,
            # Road
            'r': 1,
            # Otherwise cost is 1
                }.get(elem, 1)

    def generate_neighbours(self, node):
        x = node.state[0]
        y = node.state[1]

        # generate all neighbour nodes in each direction from parent node
        self.generate_node(x - 1, y, node)
        self.generate_node(x + 1, y, node)
        self.generate_node(x, y - 1, node)
        self.generate_node(x, y + 1, node)

    def generate_node(self, x, y, node):
        child = SearchNode((x, y))
        exists = self.get_if_exists(child)

        if exists is not None:
            node.children.append(exists)

        if self.is_valid(x, y):
            if exists is None:
                node.children.append(child)
                self.attach_and_eval(node, child)

                # Add newly created node to priority queue/list based on algorithm
                heapq.heappush(self.open, child) if self.algorithm in [0, 2] else self.open.append(child)

            elif node.g + self.get_cost(child) < child.g:
                self.attach_and_eval(node, child)
                if child in self.closed:
                    self.propagate_path_improvements(child)

    def attach_and_eval(self, node, child):
        child.parent = node
        child.g = (node.g + self.get_cost(child))
        child.h = calculate_heuristics(child.state, self.goal)
        if self.algorithm in [0, 1]:
            child.f = child.g + child.h
        else:
            child.f = child.g

    # Update f value and parent of children when a better/less cost parent is found
    def propagate_path_improvements(self, node):
        for child in node.children:
            if node.g + self.get_cost(child) < child.g:
                child.parent = node
                child.g = node.g + self.get_cost(child)
                if self.algorithm in [0, 1]:
                    child.f = child.g + child.h
                else:
                    child.f = child.g
                self.propagate_path_improvements(child)

    # Determine if node state is a valid position on the board
    def is_valid(self, x, y):
        if (x < 0) or (y < 0):
            return False
        if (x >= self.board.width) or (y >= self.board.height):
            return False
        if self.board.grid[y][x] == '#':
            return False

        return True

    # Fetch node if it already exists in open or closed lists
    def get_if_exists(self, node):
        for o in self.open:
            if node.state == o.state:
                return o

        for c in self.closed:
            if node.state == c.state:
                return c

        return None

    # Mark all node states on shortest path to visualize path on the board
    def generate_path(self, node):
        if node.parent.state is not self.start:
            parent_state = node.parent.state
            x = parent_state[0]
            y = parent_state[1]
            self.board.grid[y][x] = 'x'

            self.generate_path(node.parent)

    def display_open_closed(self):
        for o in self.open:
            self.board.grid[o.state[1]][o.state[0]] = '*'
        for c in self.closed:
            self.board.grid[c.state[1]][c.state[0]] = '+'

    def process(self):
        self.initialize()

        while True:
            if not self.open:
                return -1
            node = None

            if self.algorithm in [0, 2]:
                node = heapq.heappop(self.open)
            else:
                node = self.open.pop(0)

            self.closed.append(node)

            if node.state == self.goal:
                self.display_open_closed()
                self.generate_path(node)
                return 1

            self.generate_neighbours(node)




























