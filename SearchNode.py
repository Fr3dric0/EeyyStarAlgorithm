
class SearchNode:

    def __init__(self, state):

        # State represents position of node on the board
        self.state = state
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = None
        self.children = []

    def __cmp__(self, other):
        return cmp(self.f, other.f)



