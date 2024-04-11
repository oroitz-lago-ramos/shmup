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
        self.level_surface = pygame.Surface((self.stats_bar_img.get_width(), self.stats_bar_img.get_height()-14), pygame.SRCALPHA)
        self.level_surface.fill((255,0,0,128))
        self.level_text = self.text.draw_text(self.level_surface, "Level :", 17, (self.level_surface.get_height()/4), 12, "stats_font", (0,255,0))
        self.timer_text = self.text.draw_text(self.level_surface, "Timer :", 17+ self.level_surface.get_width()/3, (self.level_surface.get_height()/4), 12, "stats_font", (0,255,0)) 
        self.score_text = self.text.draw_text(self.level_surface, "Score :", 17+ 2*self.level_surface.get_width()/3, (self.level_surface.get_height()/4), 12, "stats_font", (0,255,0))

        self.hp_bar_img = pygame.image.load("assets\\images\\sprites\\Health_Bar_Table.png")
        self.hp_bar_img = pygame.transform.scale(self.hp_bar_img, (158, 27))
        self.hp_bar_surface = pygame.Surface((133, 25), pygame.SRCALPHA)
        self.hp_bar_surface.fill((255,0,0,128))# à enlever pour clean code
        self.hp_dot_img = pygame.image.load("assets\\images\\sprites\\Health_Dot.png")
        self.hp_dot_img = pygame.transform.scale(self.hp_dot_img, (22, 21))
        self.special_dot_img = pygame.image.load("assets\\images\\sprites\\Bonus_BTN_01.png")
        self.special_dot_img = pygame.transform.scale(self.special_dot_img, (47, 45))
        self.special_dot_surface = pygame.Surface((47, 45), pygame.SRCALPHA)
        self.special_dot_surface.fill((255,0,0,128))# à enlever pour clean code
        self.clock_icon_img = pygame.image.load("assets\\images\\sprites\\Clock_Icon.png")
        self.clock_icon_img = pygame.transform.scale(self.clock_icon_img, (25, 26))
        self.clock_icon_rect = self.clock_icon_img.get_rect(center=(self.special_dot_surface.get_width()/2, self.special_dot_surface.get_height()/2))

    def draw_hud(self,wave_level, player_health, player_score):
        self.game.screen.blit(self.stats_bar_img, ((self.game.screen.get_width()-self.stats_bar_img.get_width())/2, 0))
        self.game.screen.blit(self.level_surface, ((self.game.screen.get_width()-self.stats_bar_img.get_width())/2, 7))
        self.game.screen.blit(self.hp_bar_img, ((self.game.screen.get_width()-self.hp_bar_img.get_width())/2.5, self.game.screen.get_height()-self.hp_bar_img.get_height()))
        self.game.screen.blit(self.hp_bar_surface, ((self.game.screen.get_width()-self.hp_bar_img.get_width())/2.5, self.game.screen.get_height()-self.hp_bar_img.get_height()))
        self.hp_bar_surface.blit(self.hp_dot_img, (3,3)) # mettre le scale ici pour le dot en fonction de la vie du joueur
        self.game.screen.blit(self.special_dot_img, ((self.game.screen.get_width()-self.special_dot_img.get_width())/2, self.game.screen.get_height()-self.special_dot_img.get_height()))
        self.game.screen.blit(self.special_dot_surface, ((self.game.screen.get_width()-self.special_dot_img.get_width())/2, self.game.screen.get_height()-self.special_dot_img.get_height()))
        self.special_dot_surface.blit(self.clock_icon_img, self.clock_icon_rect)
        
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