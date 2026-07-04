import math

class Player:
    # TODO: Account for diagonal movement.
    # Should NOT move faster diagonally than on single-axis
    # SHOULD select diagonal tile if there is both vertical and horizontal movement
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.radius = 16
        self.color = color
        self.direction = (0, -1)
        
        self.speed = 175
        
        self.tileQueue = {}
        self.q = []

    def update(self):
        pass

    def select_tile(self, grid):
        x, y = self.get_position()
        xd, yd = self.get_direction()

        # next non-occupied tile in player's direction
        curr = None

        if (x + xd > -1 and 
            x + xd < grid.size and 
            y + yd > -1 and 
            y + yd < grid.size):
                curr = grid.tileMap[y + yd][x + xd]

        if curr is not None:
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
        return self.direction

    # Converts player's pixel position to Grid coords and returns them
    def get_position(self) -> tuple:
        x = max(0, math.floor(int(self.x / 80)))
        y = max(0, math.floor(int(self.y / 80)))
        return x, y

    def place_item(self):
        pass