
class Board:

    def __init__(self):
        self.grid = None
        self.start_position = ()
        self.goal_position = ()
        self.height = 0
        self.width = 0

    def read_board(self, file_name):
        grid_list = []

        with open(file_name, "r") as grid:
            sentences = [elem for elem in grid.read().split('\n') if elem]
            for sentence in sentences:
                grid_list.append([ch for ch in sentence])
        grid.close()

        return grid_list

    def find_pos(self, ch):

        for line in self.grid:
            for c in line:
                if c == ch:
                    return line.index(c), self.grid.index(line)

    def initialize(self, file_name):

        self.grid = self.read_board(file_name)
        self.start_position = self.find_pos("A")
        self.goal_position = self.find_pos("B")
        self.height = len(self.grid)
        self.width = len(self.grid[0])




