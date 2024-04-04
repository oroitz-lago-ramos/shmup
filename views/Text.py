import pygame

class Text:
    def __init__(self, text):
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
    
    def draw_text(self, screen, text, x, y):
        text = self.font.render(text, True, (255, 255, 255))
        screen.blit(text, (x, y))