import pygame

class Player_base_display:
    def __init__(self):
        self.x = 600
        self.y = 600
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.image = pygame.image.load("assets\\images\\background\\player_base.png") 
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))  
        
    def draw_on_center(self, screen, color):
        screen.blit(self.image, self.rect)
    
    def update(self,screen, x, y, color):
         self.rect.center = (x, y)
         self.draw_on_center(screen, color)    
         
    def get_rect(self):
        return self.rect