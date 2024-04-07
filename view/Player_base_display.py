import pygame

class Player_base_display:
    def __init__(self):
        self.x = 600
        self.y = 600
        self.rect = pygame.Rect(self.x - 25, self.y - 25, 50, 50)
        
    def draw_on_center(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
    
    def get_rect(self):
        return pygame.Rect(self.x - 25, self.y - 25, 50, 50)