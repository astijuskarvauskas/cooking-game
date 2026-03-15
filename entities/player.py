import math

class Player:
    _radius = 16

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.direction = (0, 1)
        self.selectedTile = None

    def update(self):
        pass

    def get_position(self):
        # convert pixel position on screen to grid[x][y]
        x = max(0, math.floor(int(self.x / 80)))
        y = max(0, math.floor(int(self.y / 80)))
        print("x pos in pixels: " + str(self.x)
              + "y pos in pixels: " + str(self.y) +
              "x index of array: " + str(x) + ". y index of array: " + str(y))

        # return grid.tileMap[x][y]

    def place_item(self):
        pass