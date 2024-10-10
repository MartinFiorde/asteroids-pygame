import pygame

from models.circleshape import CircleShape
from constants import *
from models.shoot import Shoot


# Base class for game objects
class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.radius = PLAYER_RADIUS

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) * 1.5
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius / 1.5 - right
        c = self.position - forward * self.radius / 1.5 + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        bullet = Shoot(self.position.x, self.position.y, SHOOT_RADIUS, velocity)
        
