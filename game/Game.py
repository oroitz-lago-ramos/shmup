from views import Start_menu_view, Main_menu_view, Game_view, End_menu_view
from shared import View_State
import pygame

class Game:
    VIEW_STATES = {
        View_State.START_MENU: Start_menu_view,
        View_State.MAIN_MENU: Main_menu_view,
        View_State.GAME: Game_view,
        View_State.END_MENU: End_menu_view
    }
    
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.change_view(View_State.START_MENU)
        self.running = True
    
    def change_view(self, state: View_State) -> None:
        self.view_instance = self.VIEW_STATES[state](self)
        
    def main(self) -> None:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.view_instance.handle_event(event)
            self.screen.fill((255, 255, 255))
            self.view_instance.draw()
            pygame.display.update()