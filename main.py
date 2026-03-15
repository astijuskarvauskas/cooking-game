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
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # player is just sprite for now
    # diagonal movement looks faster than single axis? test somehow... and fix if needed
        # it is faster - make player a class. on move key pressed, add to velocity. cap x+y vel at limit?
    renderer.draw_player(player)
    renderer.draw_map(grid)

    # player movement
    keys = pygame.key.get_pressed()
    if len(keys) > 0:
        print(player.get_position())
    if keys[pygame.K_w]:
        player.y -= 175 * dt
        player.direction = (0, -1)
    if keys[pygame.K_s]:
        player.y += 175 * dt
        player.direction = (0, 1)
    if keys[pygame.K_a]:
        player.x -= 175 * dt
        player.direction = (-1, 0)
    if keys[pygame.K_d]:
        player.x += 175 * dt
        player.direction = (1, 0)
    if keys[pygame.K_SPACE]:
        player.place_item()

    # select tile
        # this is where we really need to create a tile class

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()