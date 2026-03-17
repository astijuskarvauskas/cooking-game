from tile import Tile

class Grid:
    def __init__(self, size):
        self.size = size
        self.tileMap = [[Tile(x * Tile.tileSize, y * Tile.tileSize) for x in range(size+1)] for y in range(size+1)]