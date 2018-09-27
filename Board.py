
class Board:

    def __init__(self):
        self.board = None
        self.start_position = ()
        self.goal_position = ()
        self.height = 0
        self.width = 0

    def read_board(self, file_name):
        board_list = []

        with open(file_name, "r") as board:
            sentences = [elem for elem in board.read().split('\n') if elem]
            for sentence in sentences:
                board_list.append([ch for ch in sentence])
        board.close()

        return board_list

    def find_pos(self, ch):

        for line in self.board:
            for c in line:
                if c == ch:
                    return line.index(c), self.board.index(line)

    def initialize(self, file_name):

        self.board = self.read_board(file_name)
        self.start_position = self.find_pos("A")
        self.goal_position = self.find_pos("B")
        self.height = len(self.board)
        self.width = len(self.board[0])




