import pygame
import sys


class Projectile_display:
    def __init__(self,game):
        self.game = game
    def draw(self, x, y, radius):
            pygame.draw.circle(self.game.screen, (255, 0, 0), (int(x), int(y)), radius)


