import pygame
import sys


class Projectile_display:
    def __init__(self):
        pass
    def draw(self, x, y, radius, screen):
            pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), radius)


