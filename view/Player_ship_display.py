import pygame
from view.Canon_display import Canon_display

class Player_ship_display:        
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, 39, 95)
        
    def draw(self, screen, list_canons):
        self.canon_display = Canon_display()
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
        for canon in list_canons:
            self.canon_display.draw_on_center(screen, canon.x, canon.y)
    
    def update(self,screen, x, y, list_canons):
       self.rect = pygame.Rect(x , y, 39, 95)
       self.draw(screen, list_canons)
    def get_rect(self):
        return self.rect
