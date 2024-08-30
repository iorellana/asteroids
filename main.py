# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from asteroidfield import AsteroidField
from constants import *
from player import *
from asteroid import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for u in updatable:
            u.update(dt)

        for asteroid in asteroids:
            asteroid: Asteroid
            if player.collide(asteroid):
                print("Game Over!")
                return
            shot: Shot
            for shot in shots: 
                if shot.collide(asteroid):
                    shot.kill()
                    asteroid.split()
            
        
        
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()