import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)
    AsteroidField()
    Clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        for drawobj in drawable:
            drawobj.draw(screen)
        dt = Clock.tick(60) / 1000
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.colliding(player):
                print("Game over!")
                exit()
            for bullet in shots:
                if asteroid.colliding(bullet):
                    asteroid.split()
                    bullet.kill()
        pygame.display.flip()


if __name__ == "__main__":
    main()
