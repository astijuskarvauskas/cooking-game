import pygame

# class imports
from renderer import Renderer
from grid import Grid

# entity imports
from entities.player import Player

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True
dt = 0

renderer = Renderer(screen, dt)
player = Player(
    screen.get_width() / 2,
    screen.get_height() / 2,
    (255, 255, 255),
)
grid = Grid(10)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    renderer.draw_player(player)
    renderer.draw_map(grid)
    player.select_tile(grid)

    keys = pygame.key.get_pressed()
    if len(keys) > 0:
        print(player.get_position())
    if keys[pygame.K_w]:
        player.direction = (0, -1)
        player.y -= player.speed * dt
    if keys[pygame.K_s]:
        player.y += player.speed * dt
        player.direction = (0, 1)
    if keys[pygame.K_a]:
        player.x -= player.speed * dt
        player.direction = (-1, 0)
    if keys[pygame.K_d]:
        player.x += player.speed * dt
        player.direction = (1, 0)
    if keys[pygame.K_SPACE]:
        player.place_item()

    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()