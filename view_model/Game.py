import pygame
from view_model import View_state, Event_handler
from view import Start_menu_view, Main_menu_view, Game_view, End_menu_view
from model import Player_ship_model, Player_base_model, Enemy_model, Canon_model

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
        self.enemy = Enemy_model(50, 50, 1, 5, (255, 0, 0), 30, self.player_base.get_center())
        
        
    def change_view(self, state):
        self.current_view = self.VIEW_STATES[state](self)
    
    def main(self) -> None:
        font = pygame.font.Font(None, 36) # This will be removed later
        while self.running:
            self.event_handler.handle_event()
            self.screen.fill((255, 255, 255))
            self.current_view.draw()
            self.update()
            
            #Debug FPS
            fps = self.clock.get_fps()
            fps_text = font.render(f"FPS: {fps:.2f}", True, (0, 0, 255))
            self.screen.blit(fps_text, (10, 10))
            
            pygame.display.update()
            
            self.frame_time = self.clock.tick(60)
            
            
    
    def update(self):
        if isinstance(self.current_view, Game_view):
            self.enemy.update()
            self.player_ship.update(self.frame_time, pygame.mouse.get_pos())
            # Here do the check collision from projectiles and for ennemies
            self.current_view.draw_player_base(self.player_base.x, self.player_base.y, self.player_base.color)
            self.current_view.draw_player_ship(self.player_ship.x, self.player_ship.y, self.player_ship.canons)
            self.current_view.draw_enemy(self.enemy.x, self.enemy.y)
            self.check_collision()
            
    def check_collision(self):
        self.check_borders(self.player_ship)
        self.check_borders(self.enemy)
        self.check_collision_projectile(self.enemy)
    
    def check_borders(self, entity):
        if entity.x < 0:
            entity.x = 0
        elif entity.x + entity.width > self.screen.get_width():
            entity.x = self.screen.get_width() - entity.width

        if entity.y < 0:
            entity.y = 0
        elif entity.y + entity.height > self.screen.get_height():
            entity.y = self.screen.get_height() - entity.height
    
    def check_collision_projectile(self, entity):
        # for projectile in self.player_shipcanon.projectiles:
        #     if entity.x - entity.width // 2 < projectile.x < entity.x + entity.width // 2 and entity.y - entity.height // 2 < projectile.y < entity.y + entity.height // 2:
        #         self.canon.projectiles.remove(projectile)
        #         entity.take_damage(10)
        #         print(entity.get_health(), "health")
        pass
            
    def run(self) -> None:
        self.main()
        pygame.quit()
        
    def stop(self) -> None:
        self.running = False