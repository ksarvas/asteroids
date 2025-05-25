import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y,):
        super().__init__(x, y, radius=PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # draw the player as a triangle
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), width=2)
    
    def rotate(self, dt):
        # rotate the player
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        # move the player
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # create a shot at the player's position
        if self.timer > 0:
            return None
        shot = Shot(self.position.x, self.position.y, radius=SHOT_RADIUS, velocity=pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED)
        # shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN
        return shot

    def update(self, dt):
        self.timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # rotate left
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            # rotate right
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_w]:
            # move forward
            self.move(dt)
        if keys[pygame.K_s]:
            # move backward
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            # shoot
            return self.shoot()
        return None
            