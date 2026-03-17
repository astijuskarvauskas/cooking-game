import pygame

from tile import Tile

class Renderer:
    def __init__(self, surface, dt):
        self.surface = surface
        self.dt = dt

    def draw_player(self, player):
        pygame.draw.circle(self.surface, player.color, (player.x, player.y), player._radius) #np.

    def draw_tile(self, tile):
        default_color = (255, 255, 255)
        selected_color = (255, 0, 0)

        if tile.selected:
            pygame.draw.rect(
                self.surface,
                selected_color,
                pygame.Rect(
                    tile.x,
                    tile.y,
                    Tile.tileSize,
                    Tile.tileSize
                ), 1)
        else:
            pygame.draw.rect(
                self.surface,
                default_color,
                pygame.Rect(
                    tile.x,
                    tile.y,
                    Tile.tileSize,
                    Tile.tileSize
                ), 1)

    def draw_map(self, grid):
        for row in range(len(grid.tileMap)):
            for col in range(len(grid.tileMap[row])):
                # tile_x, tile_y = col, row
                self.draw_tile(grid.tileMap[row][col])