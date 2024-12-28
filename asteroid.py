import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    
    def draw(self, screen):
        pygame.draw.circle(screen, [255, 255, 255], self.position, self.radius, 2)


    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20, 50)
            vec1 = self.velocity.rotate(angle)
            vec2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = vec1 * 1.2
            asteroid_2.velocity = vec2 * 1.2