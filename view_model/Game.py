import pygame
from view_model import View_state
from view import Start_menu_view, Main_menu_view, Game_view, End_menu_view
from model import Player_ship_model

class Game:
    VIEW_STATES = {
        View_state.START_MENU: Start_menu_view,
        View_state.MAIN_MENU: Main_menu_view,
        View_state.GAME: Game_view,
        View_state.END_MENU: End_menu_view
    }    
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.running = True
        self.change_view(View_state.START_MENU)
        
        self.player_ship = Player_ship_model(self.screen.get_width(), self.screen.get_height(), 39, 95, 5)
    
        
    def change_view(self, state):
        self.current_view = self.VIEW_STATES[state](self)
    
    def main(self) -> None:
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                self.handle_event(event)
            
            
            self.screen.fill((255, 255, 255))
            self.current_view.draw()
            self.update()
            pygame.display.update()
            
            self.frame_time = self.clock.tick(60)
    
    def handle_event(self, event):
        if isinstance(self.current_view, Start_menu_view):
            self.current_view.handle_event(event)
        elif isinstance(self.current_view, Main_menu_view):
            self.current_view.handle_event(event)
        elif isinstance(self.current_view, Game_view):
            self.handle_game_event(event)
        elif isinstance(self.current_view, End_menu_view):
            self.current_view.handle_event(event)
    
    def handle_game_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.change_view(View_state.END_MENU)
            elif event.key == pygame.K_UP:
                self.player_ship.move_up()
            elif event.key == pygame.K_DOWN:
                self.player_ship.move_down()
            elif event.key == pygame.K_LEFT:
                self.player_ship.move_left()
            elif event.key == pygame.K_RIGHT:
                self.player_ship.move_right()
    
    def update(self):
        if isinstance(self.current_view, Game_view):
            self.player_ship.update()
            self.current_view.draw_player_ship(self.player_ship.x, self.player_ship.y)
    
    def run(self) -> None:
        self.main()
        pygame.quit()
        
    def stop(self) -> None:
        self.running = False