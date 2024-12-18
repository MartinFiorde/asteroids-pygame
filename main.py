# this allows us to use code from the open-source pygame library throughout this file
# documentation: https://www.pygame.org/docs/ref/pygame.html
import pygame

from constants import * # NOSONAR
from models.player import Player
from models.asteroid import Asteroid
from asteroidfield import AsteroidField
from models.shoot import Shoot


def main(): # NOSONAR
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shoot.containers = (shoots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for item in updatable:
            item.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_with(player):
                print("Game over!")
                return
            for bullet in shoots:
                if asteroid.collision_with(bullet):
                    bullet.kill()
                    asteroid.split()
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
