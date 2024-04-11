import pygame
from view_model import View_state, Event_handler
from view import Start_menu_view, Main_menu_view, Game_view, End_menu_view, Text, Settings_view, Bonus_view
from model import Player_ship_model, Player_base_model, Level_wave_model
from view_model.Sound_manager import Sound_manager

class Game:
    VIEW_STATES = {
        View_state.START_MENU: Start_menu_view,
        View_state.MAIN_MENU: Main_menu_view,
        View_state.GAME: Game_view,
        View_state.END_MENU: End_menu_view,
        View_state.SETTINGS: Settings_view,
        View_state.CHOOSE_BONUS: Bonus_view
    }    
    def __init__(self) -> None:
        pygame.init()
        self.text = Text()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.running = True
        self.sound_manager = Sound_manager(self)
        self.event_handler = Event_handler(self)
        self.change_view(View_state.START_MENU)
        
        
        self.player_ship = Player_ship_model(self.screen.get_width()/2, self.screen.get_height()/2, 39, 95, 1, 10,(255, 0, 0))
        self.player_base = Player_base_model((0,255,0), self.screen.get_width()/2, self.screen.get_height()/2, 77, 65, 1000)
        self.level = Level_wave_model(self.screen.get_width(), self.screen.get_height())        
        
    def change_view(self, state):
        self.current_view = self.VIEW_STATES[state](self)
        self.sound_manager.play_music()
    
    def main(self) -> None:
        """Main loop of the game"""
        while self.running:
            self.event_handler.handle_event()
            
            self.screen.fill((255, 255, 255))
            self.current_view.draw()
            self.update()
            
            #Printing the fps
            fps = self.clock.get_fps()
            self.text.draw_fps(self.screen, fps)
            
            pygame.display.update()
            
            self.frame_time = self.clock.tick(60)
            
            
    
    def update(self):
        if isinstance(self.current_view, Game_view):
            #Update models
            self.level.update(self.frame_time, 5, 5, self.player_base.get_center())
            self.player_ship.update(self.frame_time, pygame.mouse.get_pos())
            self.player_base.update()
            #Update views
            self.current_view.draw_player_base(self.player_base.x, self.player_base.y, self.player_base.planet_radius)
            self.current_view.draw_enemy(self.level.current_ennemy)
            self.current_view.draw_player_ship(self.player_ship.x, self.player_ship.y, self.player_ship.canons)
            #Verify for collisions
            self.check_collision()
#~======================Collisions functions======================~#          
    def check_collision(self):
        self.check_borders(self.player_ship)
        self.check_border_projectile()
        self.check_collision_base()
        self.check_collision_projectile()
        #Fonction qui va check si enemy dans planete
    def check_border_projectile(self):
        """Check if the projectile is out of the screen and remove it from the canon's list of projectile if it is the case"""
        for canon in self.player_ship.canons:
            for projectile in canon.projectiles:
                if projectile.x < 0 or projectile.x > self.screen.get_width() or projectile.y < 0 or projectile.y > self.screen.get_height():
                    canon.projectiles.remove(projectile)
    def check_borders(self, entity):
        """Check if the entity is out of the screen and put it back in the screen if it is the case"""
        if entity.x - entity.width // 2 < 0:
            entity.x = 0 + entity.width // 2
        elif entity.x + entity.width // 2 > self.screen.get_width():
            entity.x = self.screen.get_width() - entity.width // 2

        if entity.y - entity.height // 2 < 0:
            entity.y = 0 + entity.height // 2
        elif entity.y + entity.height // 2 > self.screen.get_height():
            entity.y = self.screen.get_height() - entity.height // 2
            
    def check_collision_projectile(self):
        """
        Check if the enemy hit the player base and remove the enemy and do damage to the player's base life.
        Itereate over all the current enemy in the level
        If the enemy is in the second phase, check if the player base is in the enemy's hitbox
        If the enemy is not in the second phase, check if the enemy is in the planet's hitbox and change the enemy to the second phase
        """
        for enemy in self.level.current_ennemy:
            self.check_collision_projectile_enemy(enemy)
            
    def check_collision_base(self):
        for enemy in self.level.current_ennemy:
            if enemy.second_phase:
                if enemy.x - enemy.width // 2 < self.player_base.x < enemy.x + enemy.width // 2 and enemy.y - enemy.height // 2 < self.player_base.y < enemy.y + enemy.height // 2:
                    self.player_base.take_damage(10)
                    self.level.current_ennemy.remove(enemy)
            else:
                x_distance = enemy.x + enemy.width // 2 - self.player_base.x if enemy.x > self.player_base.x else enemy.x - self.player_base.x
                y_distance = enemy.y - self.player_base.y
                distance = (x_distance ** 2 + y_distance ** 2) ** 0.5
                if distance < enemy.width // 2 + self.player_base.planet_radius and not enemy.second_phase:
                    enemy.second_phase = True
                    enemy.width = 30
                    enemy.height = 30
                    enemy.color = (255, 0, 255)
                    
    
            
    def check_collision_projectile_enemy(self, entity):
        """Function that check if the projectile hit the entity and remove the projectile and do damage to the entity if it is the case"""
        entity_rect = pygame.Rect(entity.x, entity.y, entity.width, entity.height)
        for canon in self.player_ship.canons:
            for projectile in canon.projectiles:
                projectile_rect = pygame.Rect(projectile.x, projectile.y, projectile.radius * 2, projectile.radius * 2)
                if entity_rect.colliderect(projectile_rect):
                    entity.take_damage(10)
                    canon.projectiles.remove(projectile)
                    
#===========================Logic verification===========================#
    def verify_ended_level(self):
        if self.level.end:
            self.change_view(View_state.END_MENU)
            # self.level = Level_wave_model(self.screen.get_width(), self.screen.get_height())
            # self.player_base.life = 1000
            # self.player_ship = Player_ship_model(self.screen.get_width()/2, self.screen.get_height()/2, 39, 95, 1, 10,(255, 0, 0))
            # self.sound_manager.play_music()
    def verify_lost(self):
        if self.player_base.death:
            self.change_view(View_state.END_MENU)
            
            
    def run(self) -> None:
        self.main()
        pygame.quit()
        
    def stop(self) -> None:
        self.running = False