import pygame
from view.Canon_display import Canon_display

class Player_ship_display:        
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, 39, 95)
        self.canon_display = Canon_display()
        
    def draw(self, screen, canons):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
        for canon in canons:
            self.canon_display.draw_on_center(screen, self.x, self.y, canon.projectiles)
        
    
    def update(self,screen, x, y, canons):
        self.x = x
        self.y = y
        self.rect.center = (self.x , self.y)
        self.draw(screen, canons)
    def get_rect(self):
        return self.rect
    
