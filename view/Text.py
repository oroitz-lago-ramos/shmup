import pygame

# class Text:
#     def __init__(self) -> None:
#         pygame.font.init()
        
#     def draw_text(self, screen, text, x, y, size, font):
#         self.font = pygame.font.Font(None, size)
#         text = self.font.render(text, True, (0, 0, 0))
#         screen.blit(text, (x, y))

class Text:
    pygame.font.init()
    FONTS = {"start_font": pygame.font.Font('assets/font/pdark.ttf', 80),
             "name_font" : pygame.font.Font("./assets/font/nasalization.otf", 30),
             "menu_font" : pygame.font.Font("./assets/font/nasalization.otf", 30),
             "player_name" : pygame.font.Font("./assets/font/nasalization.otf", 30)
             }
    def __init__(self) -> None:
        # pygame.font.init()
        # self.fonts = {"start_font": pygame.font.Font('assets/font/pdark.ttf', 80)}
        pass
    def draw_text(self, screen, text, x, y, size, font, color=(0, 0, 0)):
        font = Text.FONTS[font]
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))
