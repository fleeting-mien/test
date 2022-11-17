import pygame
# from pygame.draw import *
# from random import randint

# from colours import *
# from settings import *
from objects import *

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y))


def click(event):
    distance_to_center_of_ball = ((event.pos[0] - current_ball.x) ** 2
                                  + (event.pos[1] - current_ball.y) ** 2) ** 0.5
    add = current_ball.value
    current_ball.randomize()
    return add

pygame.display.update()
clock = pygame.time.Clock()
finished = False

current_ball = Ball()
current_ball.randomize()
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
    current_ball.tick()
    current_ball.render(screen)
    label = font.render("SCORE: " + str(score), 1, WHITE)
    screen.blit(label, (50, 50))

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
