import pygame
from pygame.draw import *
from random import randint

pygame.init()

MAX_X, MAX_Y = 1200, 700
BORDER = 100
BULLSEYE = 5

FPS = 2
screen = pygame.display.set_mode((MAX_X, MAX_Y))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

# DEFAULT_BALL = (MAX_X / 2, MAX_Y / 2, 50, (255, 255, 255))

count = 0


def new_ball():
    '''
    рисует новый шарик
    '''
    x = randint(BORDER, MAX_X - BORDER)
    y = randint(BORDER, MAX_Y - BORDER)
    r = randint(30, 70)
    color = COLORS[randint(0, 5)]
    global current_ball
    current_ball = (x, y, r, color)


def click(event):
    distance_to_center_of_ball = ((event.pos[0] - current_ball[0]) ** 2
                                  + (event.pos[1] - current_ball[1]) ** 2) ** 0.5
    if distance_to_center_of_ball <= BULLSEYE:
        new_ball()
        return 5
    elif distance_to_center_of_ball <= current_ball[2]:
        new_ball()
        return 1
    else:
        return 0


pygame.display.update()
clock = pygame.time.Clock()
finished = False

new_ball()
# count = 0
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            score = click(event)
            if score > 0:
                count += score
            else:
                count = 0
    circle(screen, current_ball[2], (current_ball[0], current_ball[1]), current_ball[2])
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
