import pygame

from constants import *
from circleshape import CircleShape


class Shoot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, SHOOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt
