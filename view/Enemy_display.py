import pygame
class Enemy_display:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.width = 40
        self.height = 40
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.load_image()

    def load_image(self):
        self.image_phase_1 = pygame.image.load("assets\\images\\sprites\\csp_altergeist.png")
        self.image_phase_1 = pygame.transform.scale(self.image_phase_1, (self.width, self.height))

        self.image_phase_2 = pygame.image.load("assets\\images\\sprites\\sprite_tank-removebg-preview.png")
        self.image_phase_2 = pygame.transform.scale(self.image_phase_2, (self.width/2, self.height/2))
        
    def update(self,screen, x, y, width, height, second_phase):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        if second_phase == False:
            self.rect = self.image_phase_1.get_rect(center=(self.x, self.y))
            screen.blit(self.image_phase_1, self.rect)
        else:
            self.rect = self.image_phase_2.get_rect(center=(self.x, self.y))
            screen.blit(self.image_phase_2, self.rect)

    def draw(self, screen, color=(0, 0, 255)):
        pygame.draw.rect(screen, color, self.rect)
        
    def get_rect(self):
        return self.rect