import pygame

class Player_base_display:
    def __init__(self):
        self.x = 600
        self.y = 600
        self.rect = pygame.Rect(self.x, self.y, 77, 65)
        self.image = pygame.image.load("assets\\images\\background\\player_base.png") 
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))  
        self.image_planet = pygame.image.load("assets\\images\\background\\earth.png") 
        
    def draw_on_center(self, screen, radius):
        diameter = 2 * radius
        planet_image_resized = pygame.transform.scale(self.image_planet, (diameter, diameter))
        planet_rect = planet_image_resized.get_rect()
        planet_rect.center = self.rect.center
        screen.blit(planet_image_resized, planet_rect)
        screen.blit(self.image, self.rect)
    
    def update(self,screen, x, y, radius):
         self.rect.center = (x, y)
         self.draw_on_center(screen, radius)    
         
    def get_rect(self):
        return self.rect