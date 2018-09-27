from Board import Board
from ShortestPath import ShortestPath
from visualize import generate_board_image


filePath = "boards/"
textFile = "board-1-1.txt"

A_STAR = 0
BFS = 1
DIJKSTRA = 2


def run():

    board = Board()
    board.initialize(filePath + textFile)
    path_board = Board()
    path_board.initialize(filePath+textFile)
    find_path = ShortestPath(path_board, A_STAR)
    find_path.process()
    generate_board_image(board, path_board)


def main():
    run()


if __name__ == '__main__':
    main()

