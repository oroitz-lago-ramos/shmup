from views import View_interface, Text
import pygame
from shared import View_State

class Main_menu_view(View_interface):
    def __init__(self, main_game) -> None:
        self.main_game = main_game
        self.text = Text() 
        
    def draw(self) -> None:
        self.text.draw_text(self.game.screen, "Main menu", 200, 200)
    
    def handle_event(self, event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.app.change_view(View_State.GAME)
    