from view_model import View_state
from .View_interface import View_interface
import pygame
from .Text import Text
from .Player_ship_display import Player_ship_display
from .Player_base_display import Player_base_display
from .Projectile_display import Projectile_display
from .Enemy_display import Enemy_display
from .Hud import Hud

class Game_view(View_interface):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.text = Text()
        self.hud = Hud(self.game)
        self.player_ship_display = Player_ship_display()
        self.player_base_display = Player_base_display()
        self.enemy_display = Enemy_display()
        self.background_img = pygame.image.load("assets\\images\\background\\Space_Background.png")  
        self.background_img = pygame.transform.scale( self.background_img, (self.game.screen.get_width(),self.game.screen.get_height()))  
        

 
        
        pass
    
    def draw(self):
        self.game.screen.blit(self.background_img, (0, 0))
        self.hud.update()
    def draw_player_ship(self, x, y, canons):
        self.player_ship_display.update(self.game.screen, x, y, canons)
    def draw_player_base(self,x,y, radius):
        self.player_base_display.update(self.game.screen, x, y, radius)
    def draw_enemy(self, enemies):
        for enemy in enemies:
            x, y = enemy.get_center()
            self.enemy_display.update(self.game.screen, x, y, enemy.width, enemy.height, enemy.second_phase)
    
        
    
    def get_player_ship_rect(self):
        return self.player_ship_display.get_rect()
    def get_player_base_rect(self):
        return self.player_base_display.get_rect()
    
    def handle_event(self, event):
        pass