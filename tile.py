class Tile:
    tileSize = 80
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.selected = False

    def is_selected(self) -> bool:
        return self.selected