import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius=SHOT_RADIUS, velocity=None):
        super().__init__(x, y, radius=SHOT_RADIUS)
        if velocity is None:
            # handle this as you wish, but probably raise an error
            raise ValueError("Shot needs a velocity")
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        