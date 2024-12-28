import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):
    
    cooldown = 0
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        # self.containers = None
        self.rotation = 0
        
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    
    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED
    
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        Player.cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if Player.cooldown <= 0:
                self.shoot()
    
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    
    # override draw() method
    def draw(self, screen):
        pygame.draw.polygon(screen, [255, 255, 255], self.triangle(), 2)
    
    
    def shoot(self):
        # print(f'Position: {(self.position.x, self.position.y)}')
        Player.cooldown = PLAYER_SHOOT_COOLDOWN
        new_shot = Shot(self.position.x, self.position.y)
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        