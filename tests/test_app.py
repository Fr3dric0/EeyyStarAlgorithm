##
#
# Run tests by calling ./run_test.sh in the root of the projects.
# The script will generate all the expected boards with solutions
##
import unittest

from app import readfile, project_best_path, create_board, get_clean_board
from eystar import eystar
from visualize import generate_board_image


def assert_path_length(goal, start, expected_length):
    if goal.parent is None:
        raise AssertionError(f'No solution is present')

    node = goal
    count = 0
    while node.parent is not None and node.parent != start:
        node = node.parent
        count += 1

    assert count == expected_length, f'Expected path length to be {expected_length}, instead got {count}'


def generic_board_test(filename, path_length, omit_stats=True):
    lines = readfile(filename)
    board, start_node, goal_node = create_board(lines)

    goal, opened, closed = eystar(board, start_node, goal_node)

    print('\n'.join(lines))
    print('\n')

    if omit_stats:
        solution = project_best_path(board, goal, start_node)
    else:
        solution = project_best_path(board, goal, start_node, opened, closed)

    generate_board_image(get_clean_board(board), solution, filename.replace('boards/', ''), False)

    assert_path_length(goal, start_node, path_length)


class TestUnweightedBoards(unittest.TestCase):
    def test_board_1(self):
        generic_board_test('boards/board-1-1.txt', 15)

    def test_board_2(self):
        generic_board_test('boards/board-1-2.txt', 32)

    def test_board_3(self):
        generic_board_test('boards/board-1-3.txt', 27)

    def test_board_4(self):
        generic_board_test('boards/board-1-4.txt', 25)

    def test_board_5(self):
        generic_board_test('boards/board-1-5.txt', 14)


class TestWeightedBoards(unittest.TestCase):
    def test_board_1(self):
        generic_board_test('boards/board-2-1.txt', 32, False)

    def test_board_2(self):
        generic_board_test('boards/board-2-2.txt', 37, False)

    def test_board_3(self):
        generic_board_test('boards/board-2-3.txt', 46, False)

    def test_board_4(self):
        generic_board_test('boards/board-2-4.txt', 54, False)

    def test_board_5(self):
        generic_board_test('boards/board-2-5.txt', 47, False)
