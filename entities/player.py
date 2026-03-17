import math

class Player:
    _radius = 16

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.direction = (0, -1) #face up by default
        self.tileQueue = {}
        self.q = []

    def update(self):
        pass

    # TODO: Fix deselected tiles no longer being able to be selected
    def select_tile(self, grid):
        x, y = self.get_position()
        xd, yd = self.get_direction()

        # next non-occupied tile in player's direction
        curr = grid.tileMap[y + yd][x + xd]

        if self.tileQueue.get((curr.y, curr.x), 0) == 0:
            self.tileQueue[(curr.y, curr.x)] = 1
            self.q.append(curr)
            curr.selected = True

        if len(self.q) > 1:
            t = self.q.pop(0)
            self.tileQueue[(t.y, t.x)] = 0
            t.selected = False

    # dist between player and tile, may be useful for later
    def tile_in_range(self, tile) -> bool:
        pass

    # returns x, y
    def get_direction(self) -> tuple:
        return self.direction[0], self.direction[1]

    def get_position(self) -> tuple:
        # convert pixel position on screen to grid[x][y]
        x = max(0, math.floor(int(self.x / 80)))
        y = max(0, math.floor(int(self.y / 80)))

        # returns x, y coordinates of tile player is on
        # return grid.tileMap[y][x].x, grid.tileMap[y][x].y

        # print(x, y)
        # works, but if player leaves screen it will cause out of index error
        # add collision so player can't leave screen

        return x, y

        # return grid.tileMap[y][x]

    def place_item(self):
        pass