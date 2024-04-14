from view.View_interface import View_interface
from view.Text import Text
import pygame

class Bonus_view(View_interface):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.text = Text()
        self.boost1 = "Boost 1"
        self.boost2 = "Boost 2"
    
    def draw(self) -> None:
        self.text.draw_text(self.game.screen, "Choose a bonus", 50, 50, 50, "none_font", (0, 0, 0))  # Draw the title
        self.text.draw_text(self.game.screen, "Boost 1", 100, 250, 50, "none_font", (0, 0, 0))
        self.text.draw_text(self.game.screen, "Boost 2", 500, 250, 50, "none_font", (0, 0, 0))