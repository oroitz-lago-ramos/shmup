from views import View_interface, Text
from shared import View_State
import pygame

class Start_menu_view(View_interface):
    def __init__(self, main_game) -> None:
        self.main_game = main_game
        self.text = Text()
        
    def draw(self) -> None:
        self.text.draw_text(self.game.screen, "Start", 200, 200)
    
    def handle_event(self, event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.app.change_view(View_State.MAIN_MENU)