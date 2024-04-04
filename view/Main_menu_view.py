from view_model import View_state
from .View_interface import View_interface
import pygame
from .Text import Text

class Main_menu_view(View_interface):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.text = Text()
    
    def draw(self):
        self.text.draw_text(self.game.screen, "WELCOME TO MAIN MENU", 50, 50, 30)
 
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.game.change_view(View_state.GAME)
            elif event.key == pygame.K_ESCAPE:
                self.game.change_view(View_state.START_MENU)