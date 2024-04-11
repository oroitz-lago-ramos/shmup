import pygame
import sys
import math


class Projectile_display:
    def __init__(self):
        self.image = self.load_image()

    def draw(self, x, y, angle, screen):
            # pygame.draw.circle(screen, (0, 255, 0), (int(x), int(y)), 10)
            self.rect = self.image.get_rect(center=(x,y))
            image = pygame.transform.rotate(self.image, (-(math.degrees(angle)+90)))
            screen.blit(image, self.rect)
    
    def update_rotation(self, angle):
        if angle:
            
            self.rect_rotated = self.image.get_rect(center=self.rect.center)

    def load_image(self):
        image = pygame.image.load("assets\\images\\sprites\\09.png")
        image = pygame.transform.scale(image, (30, 65))
        return image

