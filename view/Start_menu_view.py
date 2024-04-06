from .View_interface import View_interface
from view_model import View_state
import pygame
from .Text import Text


class Start_menu_view(View_interface):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.text = Text()
    
    def draw(self):
        background_start_menu = pygame.image.load("assets/images/start_menu.png")
        background_start_menu = pygame.transform.scale(background_start_menu, (self.game.screen.get_width(), self.game.screen.get_height()))
        self.game.screen.blit(background_start_menu, (0, 0))
        
        start_font = pygame.font.Font('assets/font/pdark.ttf', 80)
        self.text.draw_text(self.game.screen, "START", (self.game.screen.get_width()//2) - 100, self.game.screen.get_height()//1.37, 30, start_font, (255, 184, 28))


        
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.game.change_view(View_state.MAIN_MENU)
            elif event.key == pygame.K_ESCAPE:
                self.game.stop()