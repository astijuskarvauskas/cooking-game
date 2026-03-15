import pygame

class Renderer:
    def __init__(self, surface, dt):
        self.surface = surface
        self.dt = dt

    def draw_player(self, player):
        pygame.draw.circle(self.surface, player.color, (player.x, player.y), player._radius) #np.

    def draw_map(self, grid):
        for row in range(len(grid.tileMap)):
            for col in range(len(grid.tileMap[row])):
                tile_x, tile_y = col, row
                pygame.draw.rect(
                    self.surface,
                    (255, 255, 255),
                    pygame.Rect(
                        row * 80,
                        col * 80,
                        80,
                        80
                    ),
                    1)