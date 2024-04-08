import pygame

class Player_base_display:
    def __init__(self):
        self.x = 600
        self.y = 600
        self.rect = pygame.Rect(self.x - 25, self.y - 25, 50, 50)
        
    def draw_on_center(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)
    
    def update(self,screen, x, y, color):
         self.rect = pygame.Rect(x - 25, y - 25, 50, 50)
         self.draw_on_center(screen, color)    
         
    def get_rect(self):
        return pygame.Rect(self.x - 25, self.y - 25, 50, 50)