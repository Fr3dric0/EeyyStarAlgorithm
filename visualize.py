from PIL import Image
from PIL import ImageDraw


def generate_board_image(grid, a_star_grid):

    w = grid.width*100
    h = grid.height*100

    im = Image.new("RGB", (w, h), "white")
    draw = ImageDraw.Draw(im)

    for r in range(grid.height):
        y0 = r*100
        for c in range(grid.width):
            elem = grid.board[r][c]
            state = a_star_grid.board[r][c]
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


