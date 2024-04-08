import pygame
from view.Canon_display import Canon_display

class Player_ship_display:        
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, 39, 95)
        self.canon_display = Canon_display()
        
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
        self.canon_display.draw_on_center(screen, self.x, self.y)
    
    def update(self,screen, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x , self.y, 39, 95)
        print("rect", self.rect)
        self.draw(screen)
    def get_rect(self):
        return self.rect
