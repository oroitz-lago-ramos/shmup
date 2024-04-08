import pygame

class Player_ship_display:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, 39, 95)
        
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
    
    def update(self,screen, x, y):
       self.rect = pygame.Rect(x , y, 39, 95)
       self.draw(screen)
    def get_rect(self):
        return self.rect
