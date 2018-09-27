
class SearchNode:

    def __init__(self, state):
        self.state = state
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = None
        self.kids = []

    def __cmp__(self, other):
        return cmp(self.f, other.f)



