import tile
from tile import Tile

class Grid:
    def __init__(self, size):
        self.size = size
        self.tileMap = [[Tile() for _ in range(size+1)] for _ in range(size+1)]

