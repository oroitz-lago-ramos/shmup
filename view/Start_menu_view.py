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
        self.text.draw_text(self.game.screen, "Press space to start", 50, 50, 30)
    