from settings import *
from pygame.draw import circle
from random import randint


class Ball:
    def __init__(self, coords=CENTER, radius=AVERAGE_RADIUS,
                 colour=DEFAULT_COLOUR, speed=(0, 0), value=0):
        self.x, self.y = coords
        self.radius = radius
        self.colour = colour
        self.Vx, self.Vy = speed
        self.value = value

    def render(self, screen):
        circle(screen, self.colour, (self.x, self.y), self.radius)

    def tick(self):
        self.x += self.Vx
        self.y += self.Vy
        self.collide()

    def collide(self):
        if self.x >= (MAX_X - self.radius) or self.x <= self.radius:
            self.Vx = -self.Vx
        if self.y >= (MAX_Y - self.radius) or self.y <= self.radius:
            self.Vy = -self.Vy

    def randomize(self):
        self.x = randint(BORDER, MAX_X - BORDER)
        self.y = randint(BORDER, MAX_Y - BORDER)
        self.radius = randint(MIN_RADIUS, MAX_RADIUS)
        self.colour = PALETTE[randint(0, NUM_COLOURS - 1)]
        self.Vx = randint(-MAX_SPEED, MAX_SPEED)
        self.Vy = randint(-MAX_SPEED, MAX_SPEED)
        self.value = 1