import pygame
class Enemy_display:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, 40, 40)
        
    def update(self,screen, x, y):
       self.rect.center = (x, y)
       self.draw(screen)
    
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)
        
    def get_rect(self):
        return self.rect