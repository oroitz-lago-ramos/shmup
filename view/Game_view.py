from view_model import View_state
from .View_interface import View_interface
import pygame
from .Text import Text
from .Player_ship_display import Player_ship_display

class Game_view(View_interface):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.text = Text()
        self.player_ship_display = Player_ship_display(self.game.player_ship)
    
    def draw(self):
        self.game.screen.fill((0, 0, 0))
        self.player_ship_display.draw_on_center(self.game.screen)
    
    def handle_event(self, event):
        pass