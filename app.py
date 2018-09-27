from Board import Board
from AStar import AStar
from visualize import generate_board_image
import sys

filePath = "boards/"
textFile = "board-2-4.txt"


def a_star():
    global textFile

    textFile = sys.argv[1] if len(sys.argv) > 0 else textFile

    board = Board()
    board.initialize(filePath + textFile)
    astr_board = Board()
    astr_board.initialize(filePath+textFile)
    astr = AStar(astr_board)
    astr.process()
    generate_board_image(board, astr.board)


def main():
    a_star()


if __name__ == '__main__':
    main()

