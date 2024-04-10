from view_model import View_state
from .View_interface import View_interface
import pygame
from .Text import Text

class Main_menu_view(View_interface):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.text = Text()
        self.player_name = ""

    def draw_input_field(self):
        transparent_menu = pygame.Surface((500, 250), pygame.SRCALPHA)
        transparent_menu.set_alpha(128)

        # Dessiner le contour avec des coins arrondis
        pygame.draw.rect(transparent_menu, (255, 255, 255), (0, 0, 390, 235), border_radius=15)

        # Dessiner un rectangle rempli pour le fond blanc avec des coins arrondis
        pygame.draw.rect(transparent_menu, (255, 255, 255), (5, 5, 380, 235), border_radius=15, width=20)

        self.game.screen.blit(transparent_menu, (self.game.screen.get_width()//2 - 180, self.game.screen.get_height()//3 - 25))




        #Draw the input field
        transparent_surface = pygame.Surface((200, 50), pygame.SRCALPHA)
        transparent_surface.set_alpha(220)
        pygame.draw.rect(transparent_surface, (150, 170, 255), (0, 0, 200, 50))
        self.game.screen.blit(transparent_surface, (self.game.screen.get_width()//2 - 80, self.game.screen.get_height()//3 + 20))
        
        #Draw the player name
        real_name_font = Text.FONTS["name_font"]
        max_text_width = 200 - 10  
        if real_name_font.size(self.player_name)[0] > max_text_width:
            while real_name_font.size(self.player_name)[0] > max_text_width and len(self.player_name) > 0:
                self.player_name = self.player_name[:-1]

        text_x = self.game.screen.get_width()//2 - 80 + (200 - real_name_font.size(self.player_name)[0])//2
        self.text.draw_text(self.game.screen, self.player_name, text_x, self.game.screen.get_height()//3 + 24, 30, "name_font", (127, 255, 155))


        event = pygame.event.wait()  # Wait for a single event

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                # Remove the last character from player_name
                self.player_name = self.player_name[:-1]
            elif event.unicode.isalnum() or event.unicode == " ":
                # Append the pressed character to player_name
                self.player_name += event.unicode

        pygame.time.delay(10)


    def draw(self):
        #Picture for the main menu
        background_main_menu = pygame.image.load("./assets/images/main_menu.png")
        background_main_menu = pygame.transform.scale(background_main_menu, (self.game.screen.get_width(), self.game.screen.get_height()))
        self.game.screen.blit(background_main_menu, (0, 0))
        
        
        self.draw_input_field()
        #Button play for the main menu
        button_play = pygame.image.load("./assets/images/button_play.png")
        button_play = pygame.transform.scale(button_play, (200, 50))
        self.game.screen.blit(button_play, (self.game.screen.get_width()//2 - 80, self.game.screen.get_height()//3 + 90))
        self.text.draw_text(self.game.screen, "Play", self.game.screen.get_width()//2 - 15 , self.game.screen.get_height()//3 + 95, 30, "menu_font", (127, 218, 95))
       
        #Button parameter for the main menu
        button_parameter = pygame.image.load("./assets/images/button_parameter.png")
        button_parameter = pygame.transform.scale(button_parameter, (200, 50))
        self.game.screen.blit(button_parameter, (self.game.screen.get_width()//2 - 80, self.game.screen.get_height()//3 + 160))
        self.text.draw_text(self.game.screen, "Parameter", self.game.screen.get_width()//2 - 60 , self.game.screen.get_height()//3 + 165, 30, "menu_font", (127, 218, 95))
        
        #Player name
        self.text.draw_text(self.game.screen, "Player name: ", self.game.screen.get_width()//2 - 160, self.game.screen.get_height()//3 - 25, 30, "player_name", (127, 218, 95))
        
