import sys


def rush(x, y):
    """
    Display a square pattern based on x (width) and y (height).

    Top-left and bottom-right corners use '/'.
    Top-right and bottom-left corners use '\\'.
    All edges (top, bottom, left, right) use '*'.
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

            # A corner only applies when it is unambiguous
            # (i.e., the top row is distinct from the bottom row
            # and the left column is distinct from the right column).
            corner_tl = is_top and is_left and not is_bot and not is_right
            corner_tr = is_top and is_right and not is_bot and not is_left
            corner_bl = is_bot and is_left and not is_top and not is_right
            corner_br = is_bot and is_right and not is_top and not is_left

            if corner_tl or corner_br:
                row += "/"
            elif corner_tr or corner_bl:
                row += "\\"
            elif is_top or is_bot or is_left or is_right:
                row += "*"
            else:
                row += " "
        print(row)
