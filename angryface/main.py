import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

tps = 30
done = False

from colours import vibrant as v
from colours import koch as k

screen.fill(k.beige)

# face
center = (200, 150)
circle(screen, v.yellow, center, 100)
circle(screen, k.black, center, 100, 3)

# left eye
left_eye = (160, 130)
circle(screen, v.red, left_eye, 20)
circle(screen, k.black, left_eye, 20, 2)
circle(screen, k.black, left_eye, 8)

# right eye
right_eye = (240, 130)
circle(screen, v.red, right_eye, 15)
circle(screen, k.black, right_eye, 15, 2)
circle(screen, k.black, right_eye, 8)

#eyebrows
polygon(screen, k.black, ((100, 50), (200, 100), (190, 120), (90, 70)))
polygon(screen, k.black, ((300, 55), (210, 100), (219, 118), (309, 73)))
rect(screen, k.black, (150, 180, 100, 20))

pygame.display.update()
while not done:
    clock.tick(tps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
