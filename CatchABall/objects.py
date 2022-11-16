from settings import *
from pygame.draw import circle


class Ball:
    x = MAX_X / 2
    y = MAX_Y / 2
    radius = DEFAULT_RADIUS
    colour = DEFAULT_COLOUR

    def __init__(self, x, y, r, colour):
        self.x = x
        self.y = y
        self.r = r
        self.colour = colour

    def render(self, screen):
        circle(screen, self.colour, (self.x, self.y), self.radius)
