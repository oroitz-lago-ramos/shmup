import pygame
from view_model import View_state
from view import Start_menu_view, Main_menu_view, Game_view, End_menu_view

class Game:
    VIEW_STATES = {
        View_state.START_MENU: Start_menu_view,
        View_state.MAIN_MENU: Main_menu_view,
        View_state.GAME: Game_view,
        View_state.END_MENU: End_menu_view
    }    
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        self.change_view(View_state.START_MENU)
        
    def change_view(self, state):
        self.current_view = self.VIEW_STATES[state](self)
    
    def main(self) -> None:
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                self.current_view.handle_event(event)
            self.screen.fill((255, 255, 255))
            self.current_view.draw()
            pygame.display.update()
    
    def run(self) -> None:
        self.main()
        pygame.quit()
        
    def stop(self) -> None:
        self.running = False