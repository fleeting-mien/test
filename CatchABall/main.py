import pygame
# from pygame.draw import *
from random import randint

# from colours import *
from settings import *
from objects import *

pygame.init()
FPS = 2
screen = pygame.display.set_mode((MAX_X, MAX_Y))

count = 0


def new_ball():
    x = randint(BORDER, MAX_X - BORDER)
    y = randint(BORDER, MAX_Y - BORDER)
    r = randint(DEFAULT_RADIUS - 20, DEFAULT_RADIUS + 20)
    colour = PALETTE[randint(0, 5)]
    global current_ball
    current_ball = Ball(x, y, r, colour)


def click(event):
    distance_to_center_of_ball = ((event.pos[0] - current_ball.x) ** 2
                                  + (event.pos[1] - current_ball.y) ** 2) ** 0.5
    if distance_to_center_of_ball <= BULLSEYE:
        add = 5
    elif distance_to_center_of_ball <= current_ball.radius:
        add = 1
    else:
        add = 0
    new_ball()
    return add

pygame.display.update()
clock = pygame.time.Clock()
finished = False

new_ball()
score = 0
font = pygame.font.SysFont("Calibri", 18)
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            add = click(event)
            if add > 0:
                score += add
            else:
                score = 0

    current_ball.render(screen)
    label = font.render("SCORE: " + str(score), 1, WHITE)
    screen.blit(label, (50, 50))

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
