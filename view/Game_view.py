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
        self.background_img = pygame.image.load("assets\\images\\background\\Space_Background.png")  
        self.background_img = pygame.transform.scale( self.background_img, (self.game.screen.get_width(),self.game.screen.get_height()))  
        self.stats_bar_img = pygame.image.load("assets\\images\\sprites\\stats_bar.png")
        self.hp_bar_img = pygame.image.load("assets\\images\\sprites\\Health_Bar_Table.png")
        self.hp_bar_img = pygame.transform.scale(self.hp_bar_img, (158, 27))
        self.hp_bar_surface = pygame.Surface((155, 25), pygame.SRCALPHA)
        self.hp_bar_surface.fill((255,0,0,0))
        self.hp_dot_img = pygame.image.load("assets\\images\\sprites\\Health_Dot.png")
        self.hp_dot_img = pygame.transform.scale(self.hp_dot_img, (22, 21))
        self.special_dot_img = pygame.image.load("assets\\images\\sprites\\Bonus_BTN_01.png")

    def draw_hud(self,wave_level, player_health, player_score):
        self.game.screen.blit(self.stats_bar_img, ((self.game.screen.get_width()-self.stats_bar_img.get_width())/2, 0))
        self.game.screen.blit(self.hp_bar_img, ((self.game.screen.get_width()-self.hp_bar_img.get_width())/3, self.game.screen.get_height()-self.hp_bar_img.get_height()))
        self.game.screen.blit(self.hp_bar_surface, ((self.game.screen.get_width()-self.hp_bar_img.get_width())/3, self.game.screen.get_height()-self.hp_bar_img.get_height()))
        self.hp_bar_surface.blit(self.hp_dot_img, (3,3)) # mettre le scale ici pour le dot en fonction de la vie du joueur
        pass
    
    def draw(self):
        self.game.screen.blit( self.background_img, (0, 0))
        self.draw_hud(1, 100, 1000)
    def draw_player_ship(self, x, y, canons):
        self.player_ship_display.update(self.game.screen, x, y, canons)
    def draw_player_base(self,x,y, radius):
        self.player_base_display.update(self.game.screen, x, y, radius)
    def draw_enemy(self, enemies):
        for enemy in enemies:
            x, y = enemy.get_center()
            self.enemy_display.update(self.game.screen, x, y, enemy.width, enemy.height, enemy.color)
    
        
    
    def get_player_ship_rect(self):
        return self.player_ship_display.get_rect()
    def get_player_base_rect(self):
        return self.player_base_display.get_rect()
    
    def handle_event(self, event):
        pass