import pygame
from pygame import sprite

class Canon_display (sprite.Sprite):
    def __init__(self,canon_model):
        super().__init__()  # Call the parent class (Sprite) constructor
        self.canon = canon_model


    def draw_on_center(self, screen, x , y):
        pygame.draw.rect(screen, (0, 255, 0), (x + 10, y - 10, 10, 10))
