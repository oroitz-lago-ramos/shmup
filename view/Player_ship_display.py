import pygame
from view.Canon_display import Canon_display

class Player_ship_display:        
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, 39, 95)
        self.image = pygame.image.load("assets\\images\\sprites\\spaceship.png")
        self.image = pygame.transform.scale(self.image, (39*2, 95*2))
        self.image_surface = pygame.Surface((39*2, 95*2), pygame.SRCALPHA)
        self.image_surface.fill((255,0,0,128))
        self.image_rect = self.image.get_rect(center=(self.x, self.y))
        self.canon_display = Canon_display()
        
    def draw(self, screen, canons):
        # pygame.draw.rect(screen, (255, 0, 0), self.rect)
        screen.blit(self.image, self.image_rect)
        screen.blit(self.image_surface, self.image_rect)

        for canon in canons:
            self.canon_display.draw_on_center(screen, canon.x, canon.y, canon.projectiles)
        
    
    def update(self,screen, x, y, canons):
        self.x = x
        self.y = y
        # self.rect.center = (self.x , self.y)
        self.image_rect.center = (self.x, self.y)
        self.draw(screen, canons)
    def get_rect(self):
        return self.rect
    
