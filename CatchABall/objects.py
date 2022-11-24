from settings import *  # settings imports colours as well
from pygame.draw import circle
from random import randint, uniform


class Ball:
    def __init__(self, coords=CENTER, radius=AVERAGE_RADIUS, colour=DEFAULT_COLOUR, speed=(0, 0)):
        self.x, self.y = coords
        self.radius = radius
        self.colour = colour
        self.Vx, self.Vy = speed    # пикселей в секунду

        v = (speed[0] ** 2 + speed[1] ** 2) ** 0.5
        step = MAX_V / 5
        self.value = int(v / step) + 1
        if self.value > 5:
            self.value = 5

    # def args(self):
    #     return (self.x, self.y), self.radius, self.colour, (self.Vx, self.Vy)

    def render(self, screen):
        circle(screen, self.colour, (self.x, self.y), self.radius)

    def tick(self):
        self.x += self.Vx / FPS
        self.y += self.Vy / FPS
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
        self.Vx = uniform(-MAX_SPEED, MAX_SPEED)
        self.Vy = uniform(-MAX_SPEED, MAX_SPEED)
        self.value = 1


class Target(Ball):
    def render(self, screen):
        r = self.radius
        count = 0
        while r > 0:
            circle(screen, WHITE if count % 2 == 0 else self.colour, (self.x, self.y), r)
            r -= 5
            # FIXME: only renders a white ball


def new_object():
    if randint(1, 10) == 10:
        obj = Target()
    else:
        obj = Ball()
    obj.randomize()
    return obj