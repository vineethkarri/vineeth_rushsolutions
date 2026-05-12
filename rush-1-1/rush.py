import sys


def rush(x, y):
    """
    Display a square pattern based on x (width) and y (height).

    Corners use 'o'.
    Horizontal edges (top/bottom) use '-'.
    Vertical edges (left/right) use '|'.
    Interior cells are spaces.
    """
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for i in range(y):
        row = ""
        for j in range(x):
            is_top = (i == 0)
            is_bot = (i == y - 1)
            is_left = (j == 0)
            is_right = (j == x - 1)

            if (is_top or is_bot) and (is_left or is_right):
                row += "o"
            elif is_top or is_bot:
                row += "-"
            elif is_left or is_right:
                row += "|"
            else:
                row += " "
        print(row)
