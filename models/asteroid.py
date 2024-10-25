import pygame
import random

from models.circleshape import CircleShape
from constants import * # NOSONAR


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        first = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        first.velocity = self.velocity.rotate(random_angle) * 1.2
        second = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        second.velocity = self.velocity.rotate(-random_angle) * 1.2

