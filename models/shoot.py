import pygame

from constants import *
from models.circleshape import CircleShape


class Shoot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, SHOOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt
