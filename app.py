import pygame
from scene import Scene
from creature import *

height = 720
width = 1280

# pygame setup
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

scene = Scene(width, height)
node = Node(3, 500, 7)
node2 = Node(3, 700, 100)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    scene.draw(screen)
    node.draw(screen, 2*height/3)
    node2.draw(screen, 2*height/3)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60) # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.

pygame.quit()