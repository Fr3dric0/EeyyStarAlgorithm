from PIL import Image
from PIL import ImageDraw


def generate_board_image(board, path_board):

    """
    Takes two boards, one is the initial board read from
    text file and the other is the same board modified by the
    algorithm to indicate shortest path and opened and closed nodes.

    Returns a visualization of the board where different colors indicate
    different elements, grass, water ect. Circles/"x" represent the shortest path from
    start node to goal node, "/" represent nodes that are in the open list and the
    rectangles/"+" represent nodes in the closed list.

    """

    w = board.width*100
    h = board.height*100

    im = Image.new("RGB", (w, h), "white")
    draw = ImageDraw.Draw(im)

    for r in range(board.height):
        y0 = r*100
        for c in range(board.width):
            elem = board.grid[r][c]
            state = path_board.grid[r][c]
            x0 = c*100
            fill_color = get_color(elem)
            draw.rectangle([(x0, y0), (x0+100, y0+100)], fill=fill_color, outline="black")
            if state == 'x':
                draw.ellipse([(x0+30, y0+30), (x0+70, y0+70)], fill="red", outline="black")
            elif state == '*':
                draw.line([(x0+25, y0+25), (x0+75, y0+75)], width=2)
            elif state == '+':
                draw.rectangle([(x0+30, y0+30), (x0+70, y0+70)], fill="black", outline="black")

    im.show()


def get_color(elem):
    return {'w': "blue",
            'm': "grey",
            'r': "sienna",
            'f': "green",
            'g': "lime",
            'A': "red",
            'B': "yellow",
            '#': "black"}.get(elem, "white")


