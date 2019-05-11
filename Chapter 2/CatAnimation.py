import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 120 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 280
caty = 220
direction = 'up'
loop =0
while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'up'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'right'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'down'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'left'
    loop+=1
    if (loop%500==0):
        catx = 0
        caty = 0
        direction = 'down'
    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

    fpsClock.tick(FPS)