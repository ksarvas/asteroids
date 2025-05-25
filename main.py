# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    FPS = 60
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        updatable.update(dt)
        new_shot = player.update(dt)
        if new_shot:
            shots.add(new_shot)
            drawable.add(new_shot)
            updatable.add(new_shot)
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                # Handle collision logic here
                pygame.quit()
                return
            for shot in shots:
                if asteroid.check_collision(shot):
                    print("Asteroid destroyed!")
                    asteroid.split()
                    shot.kill()
                    break
        screen.fill((0, 0, 0))
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
        dt = clock.tick(FPS) / 1000.0
        

if __name__ == "__main__":
    main()