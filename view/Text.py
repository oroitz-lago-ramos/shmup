import pygame

# class Text:
#     def __init__(self) -> None:
#         pygame.font.init()
        
#     def draw_text(self, screen, text, x, y, size, font):
#         self.font = pygame.font.Font(None, size)
#         text = self.font.render(text, True, (0, 0, 0))
#         screen.blit(text, (x, y))

class Text:
    def __init__(self) -> None:
        pygame.font.init()
        
    def draw_text(self, screen, text, x, y, size, font, color=(0, 0, 0)):
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))
