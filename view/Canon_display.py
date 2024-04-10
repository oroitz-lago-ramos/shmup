import pygame
from pygame.math import Vector2
from pygame import sprite
import math
from .Projectile_display import Projectile_display

class Canon_display (sprite.Sprite):
    def __init__(self):
        super().__init__()  # Call the parent class (Sprite) constructor
        self.x=0
        self.y=0
        self.rotated_image = None
        self.rotated_image_rect = None
        self.load_image()
        self.projectile_display = Projectile_display()
        

    def load_image(self):
        self.image = pygame.image.load("assets\\images\\sprites\\Cetan Squall Burst.png")
        self.image = pygame.transform.scale(self.image, (30, 65))
        self.image = pygame.transform.rotate(self.image, 0)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        """self.update_image_rotation(self.calcule_angle())"""

    def draw_on_center(self, screen, x, y, projectiles):
        self.draw_projectiles(screen, projectiles)
        self.update_canon_position(x,y)
        self.update_image_rotation(self.calcule_angle())
        if self.rotated_image:
            # print("rotated image", self.rotated_image)
            screen.blit(self.rotated_image,self.rotated_image_rect)
    
    def draw_projectiles(self, screen, projectiles):
        for projectile in projectiles:
            self.projectile_display.draw(projectile.x, projectile.y, projectile.angle, screen)
            print("projectiles angle", projectile.angle)

    def calcule_angle(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx)
        angle = math.degrees(angle)
        return angle
    
    def update_image_rotation(self, angle):
        if angle:
            self.rotated_image = pygame.transform.rotate(self.image, - angle-90)
            self.rotated_image_rect = self.rotated_image.get_rect(center=self.rect.center)

    def update_canon_position(self, x, y):
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)
        # print("rect center", self.rect.center)