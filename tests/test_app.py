import unittest

from eystar import readfile, create_board, calc_heuristic


class TestApp(unittest.TestCase):

    def test_board_1(self):
        lines = readfile('boards/board-1-1.txt')
        print('BOARD 1')
        print('\n'.join(lines))
        print('\n')
        board, start_node, goal_node = create_board(lines)

        calc_heuristic(board, goal_node)

        for y in range(len(board)):
            for x in range(len(board[y])):

                if x < len(board[y]) - 1:
                    print(f'{board[y][x].symbol} {board[y][x+1].symbol}|', end='')


        self.assertEqual(goal_node.h, 0)
        self.assertEqual(start_node.g, 0)
