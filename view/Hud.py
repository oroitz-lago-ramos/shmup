import pygame
from .Text import Text
class Hud:
    def __init__(self,game) -> None:
        self.game = game
        self.text = Text()
        self.current_wave = None
        self.timer = None
        self.current_health = 0
        self.stats_bar_img = pygame.image.load("assets\\images\\sprites\\stats_bar.png")
        self.stats_surface = pygame.Surface((self.stats_bar_img.get_width(), self.stats_bar_img.get_height()-14), pygame.SRCALPHA)
        self.level_text = self.text.draw_text(self.stats_surface, f"Wave : {self.current_wave}", 17, (self.stats_surface.get_height()/4), 12, "stats_font", (0,255,0))
        self.timer_text = self.text.draw_text(self.stats_surface, f"Timer : {self.timer}", 17+ self.stats_surface.get_width()/3, (self.stats_surface.get_height()/4), 12, "stats_font", (0,255,0)) 
        self.score_text = self.text.draw_text(self.stats_surface, f"Level : {self.game.current_level}", 17+ 2*self.stats_surface.get_width()/3, (self.stats_surface.get_height()/4), 12, "stats_font", (0,255,0))
        self.hp_bar_img = pygame.image.load("assets\\images\\sprites\\Health_Bar_Table.png")
        self.hp_bar_img = pygame.transform.scale(self.hp_bar_img, (158, 27))
        self.hp_bar_surface = pygame.Surface((133, 25), pygame.SRCALPHA)
        self.hp_dot_img = pygame.image.load("assets\\images\\sprites\\Health_Dot.png")
        self.hp_dot_img = pygame.transform.scale(self.hp_dot_img, (133, 21))
        self.special_dot_img = pygame.image.load("assets\\images\\sprites\\Bonus_BTN_01.png")
        self.special_dot_img = pygame.transform.scale(self.special_dot_img, (47, 45))
        self.special_dot_surface = pygame.Surface((47, 45), pygame.SRCALPHA)
        self.special_dot_surface.fill((0,255,0,128))
        self.clock_icon_img = pygame.image.load("assets\\images\\sprites\\Clock_Icon.png")
        self.clock_icon_img = pygame.transform.scale(self.clock_icon_img, (25, 26))
        self.clock_icon_rect = self.clock_icon_img.get_rect(center=(self.special_dot_surface.get_width()/2, self.special_dot_surface.get_height()/2))
    
    def set_current_level(self, wave):
        self.current_wave = wave
    
    def set_current_timer(self, timer):
        self.timer = timer

    def set_current_hp(self, health):
        self.current_health = health
    
    def scale_health(self):
        print("current health", self.current_health)
        print("scale", (self.current_health/100) * 133)
        self.hp_dot_img_resized =pygame.transform.scale(self.hp_dot_img, (int((self.current_health/100) * 133), 21))
        self.hp_bar_surface.fill((0, 0, 255, 0))
        self.hp_bar_surface.blit(self.hp_dot_img_resized, (3,3))
        print("hp dot img", self.hp_dot_img)

    def draw_hud(self):
        self.game.screen.blit(self.stats_bar_img, ((self.game.screen.get_width()-self.stats_bar_img.get_width())/2, 0))
        self.game.screen.blit(self.stats_surface, ((self.game.screen.get_width()-self.stats_bar_img.get_width())/2, 7))
        self.game.screen.blit(self.hp_bar_img, ((self.game.screen.get_width()-self.hp_bar_img.get_width())/2.5, self.game.screen.get_height()-self.hp_bar_img.get_height()))
        self.game.screen.blit(self.hp_bar_surface, ((self.game.screen.get_width()-self.hp_bar_img.get_width())/2.5, self.game.screen.get_height()-self.hp_bar_img.get_height()))   
        self.hp_bar_surface.blit(self.hp_dot_img, (3,3)) # mettre le scale ici pour le dot en fonction de la vie du joueur
        self.game.screen.blit(self.special_dot_img, ((self.game.screen.get_width()-self.special_dot_img.get_width())/2, self.game.screen.get_height()-self.special_dot_img.get_height()))
        self.game.screen.blit(self.special_dot_surface, ((self.game.screen.get_width()-self.special_dot_img.get_width())/2, self.game.screen.get_height()-self.special_dot_img.get_height()))
        self.clock_icon_rect = self.clock_icon_img.get_rect(center=(self.special_dot_surface.get_width()/2, self.special_dot_surface.get_height()/2))
        self.special_dot_surface.blit(self.clock_icon_img, self.clock_icon_rect)
        print("clock icon rect", self.clock_icon_rect)

    def update(self):
        # self.hp_bar_surface.fill((0, 0, 255, 128))
        self.stats_surface.fill((255,0,0,0))
        # self.special_dot_surface.fill((0,255,0,128))
        self.level_text = self.text.draw_text(self.stats_surface, f"Wave : {self.current_wave}", 17, (self.stats_surface.get_height()/4), 12, "stats_font", (0,255,0))
        self.timer_text = self.text.draw_text(self.stats_surface, f"Timer : {self.timer}", 17+ self.stats_surface.get_width()/3, (self.stats_surface.get_height()/4), 12, "stats_font", (0,255,0)) 
        self.score_text = self.text.draw_text(self.stats_surface, f"Level : {self.game.current_level}", 17+ 2*self.stats_surface.get_width()/3, (self.stats_surface.get_height()/4), 12, "stats_font", (0,255,0))
        
        self.draw_hud()
        self.scale_health()