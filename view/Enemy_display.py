import pygame
class Enemy_display:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.width = 40
        self.height = 40
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def update(self,screen, x, y, width, height, color=(0, 0, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.center = (x, y)
        self.draw(screen, color)
    
    def draw(self, screen, color=(0, 0, 255)):
        pygame.draw.rect(screen, color, self.rect)
        
    def get_rect(self):
        return self.rect