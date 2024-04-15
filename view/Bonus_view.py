from view.View_interface import View_interface
from view.Text import Text
import pygame
import random

class Bonus_view(View_interface):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.text = Text()
        self.boost1 = "Boost 1"
        self.boost2 = "Boost 2"
        self.bg = pygame.image.load("assets\\images\\background\\space_shmup.jpg")
        self.bg = pygame.transform.scale( self.bg, (self.game.screen.get_width(),self.game.screen.get_height()))  
        self.list_bonus_img = ["assets\\images\\sprites\\slice25.png","assets\\images\\sprites\\slice26.png","assets\\images\\sprites\\slice27.png","assets\\images\\sprites\\slice28.png","assets\\images\\sprites\\slice29.png","assets\\images\\sprites\\slice30.png","assets\\images\\sprites\\slice31.png","assets\\images\\sprites\\slice32.png","assets\\images\\sprites\\slice33.png","assets\\images\\sprites\\slice34.png","assets\\images\\sprites\\slice35.png","assets\\images\\sprites\\slice36.png","assets\\images\\sprites\\slice37.png","assets\\images\\sprites\\slice38.png","assets\\images\\sprites\\slice39.png","assets\\images\\sprites\\slice40.png","assets\\images\\sprites\\slice41.png","assets\\images\\sprites\\slice42.png","assets\\images\\sprites\\slice43.png","assets\\images\\sprites\\slice44.png","assets\\images\\sprites\\slice45.png","assets\\images\\sprites\\slice46.png""assets\\images\\sprites\\slice47.png"] #random le choice puis le blit sous les nom des choix
        self.choice1 = random.choice(self.list_bonus_img)
        self.choice2= random.choice(self.list_bonus_img)
        self.bonus1 = pygame.image.load(self.choice1)
        self.bonus2 = pygame.image.load(self.choice2)
    
    def draw(self) -> None:
        self.game.screen.blit(self.bg, (0, 0))
        self.text.draw_text(self.game.screen, "Choose a bonus", 50, 50, 50, "none_font", (255, 255, 255))  # Draw the title
        self.text.draw_text(self.game.screen, "Boost 1", 100, 250, 50, "none_font", (255, 255, 255))
        self.text.draw_text(self.game.screen, "Boost 2", 500, 250, 50, "none_font", (255, 255, 255))
        self.game.screen.blit(self.bonus1, (100, 300))
        self.game.screen.blit(self.bonus2, (500, 300))