import pygame
from constants import *

def main():
    # Initialize Pygame
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    while True:
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
