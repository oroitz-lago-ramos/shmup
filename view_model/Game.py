import pygame
from view_model import View_state, Event_handler
from view import Start_menu_view, Main_menu_view, Game_view, End_menu_view
from model import Player_ship_model, Player_base_model, Enemy_model

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
        self.event_handler = Event_handler(self)
        
        
        self.player_ship = Player_ship_model(self.screen.get_width()/2, self.screen.get_height()/2, 39, 95, 1, 10,(255, 0, 0))
        self.player_base = Player_base_model((0,255,0), self.screen.get_width()/2, self.screen.get_height()/2, 50, 50, 1000)
        self.enemy = Enemy_model(50, 50, 1, 5, (255, 0, 0), 100, self.player_base.get_center())
        
    def change_view(self, state):
        self.current_view = self.VIEW_STATES[state](self)
    
    def main(self) -> None:
        while self.running:
            self.event_handler.handle_event()
            self.screen.fill((255, 255, 255))
            self.current_view.draw()
            self.update()
            pygame.display.update()
            
            self.frame_time = self.clock.tick(60)
    
    def update(self):
        if isinstance(self.current_view, Game_view):
            """self.player_ship.update()"""
            self.current_view.draw_player_base(self.player_base.x, self.player_base.y, self.player_base.color)
            self.current_view.draw_player_ship(self.player_ship.x, self.player_ship.y)
            
            self.enemy.update()
            self.current_view.draw_enemy(self.enemy.x, self.enemy.y)
    def check_collision(self):
        pass
    
    def run(self) -> None:
        self.main()
        pygame.quit()
        
    def stop(self) -> None:
        self.running = False