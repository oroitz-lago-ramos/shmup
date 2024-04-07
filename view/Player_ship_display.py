import pygame

class Player_ship_display:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        
    def draw_on_center(self, screen, x , y):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
    
    def update(self,screen, x, y):
       self.rect = pygame.Rect(x - 10, y - 10, 20, 20)
       self.draw_on_center(screen, x, y)
    def get_rect(self):
        return self.rect
