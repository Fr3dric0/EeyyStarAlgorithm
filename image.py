from PIL import Image
import numpy as np

SYMBOLS = {
    'A': [158, 0, 8],
    'B': [34, 255, 8],
    '#': [55, 55, 55],
    'w': [60, 44, 92],
    'm': [149, 149, 149],
    'f': [15, 112, 1],
    'g': [115, 255, 109],
    'r': [117, 109, 50],
    '.': [117, 109, 50],
    'o': [25, 25, 25]
}


def project_board_to_image(board, name, show=False):
    imgarray = np.zeros([len(board), len(board[0]), 3], dtype=np.uint8)

    for y in range(len(board)):
        for x in range(len(board[y])):
            imgarray[y, x] = SYMBOLS[board[y][x]]

    img = Image.fromarray(imgarray)
    img.save(f'images/{name}.png')

    if show:
        img.show()
