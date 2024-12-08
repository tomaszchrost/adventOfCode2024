from typing import Final


class Direction:
    def __init__(self, x_move, y_move):
        self.x_move = x_move
        self.y_move = y_move

LEFT: Final[Direction] = Direction(-1, 0)
RIGHT: Final[Direction] = Direction(1,0)
UP: Final[Direction] = Direction(0,-1)
DOWN: Final[Direction] = Direction(0,1)
UP_LEFT: Final[Direction] = Direction(-1,-1)
UP_RIGHT: Final[Direction] = Direction(1,-1)
DOWN_LEFT: Final[Direction] = Direction(-1,1)
DOWN_RIGHT: Final[Direction] = Direction(1,1)

DIRECTION_LIST: Final[list[Direction]] = [LEFT, RIGHT, UP, DOWN, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT]

def move_valid(x, y, direction, data):
    if y + direction.y_move >= len(data) or y + direction.y_move < 0:
        return False
    elif x + direction.x_move >= len(data[y]) or x + direction.x_move < 0:
        return False
    else:
        return True

def get_opposite_direction(direction):
    return Direction(direction.x_move * -1, direction.y_move * -1)

def get_value_in_direction(x, y, direction, data):
    if move_valid(x, y, direction, data):
        return data[y + direction.y_move][x + direction.x_move]
    else:
        return None
