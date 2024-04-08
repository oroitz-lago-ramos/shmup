from view_model import View_state
from .View_interface import View_interface
import pygame
from .Text import Text
from .Player_ship_display import Player_ship_display
from .Player_base_display import Player_base_display
from .Projectile_display import Projectile_display
from .Enemy_display import Enemy_display

class Game_view(View_interface):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.text = Text()
        self.player_ship_display = Player_ship_display()
        self.player_base_display = Player_base_display()
        self.enemy_display = Enemy_display()
        self.projectile_display = Projectile_display()
    
    def draw(self):
        self.game.screen.fill((0, 0, 0))
    def draw_player_ship(self, x, y):
        self.player_ship_display.update(self.game.screen, x, y)
    def draw_player_base(self,x,y, color):
        self.player_base_display.update(self.game.screen, x, y, color)
    def draw_enemy(self, x, y):
        self.enemy_display.update(self.game.screen, x, y)
    def draw_projectiles(self, list):
        for projectile in list:
            self.projectile_display.draw(projectile.x, projectile.y, 5, self.game.screen)
    
        
    
    def get_player_ship_rect(self):
        return self.player_ship_display.get_rect()
    def get_player_base_rect(self):
        return self.player_base_display.get_rect()
    
    def handle_event(self, event):
        pass