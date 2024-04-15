from view.Text import Text
import pygame

class Hall_of_fame_view:
    def __init__(self, game):
        self.game = game
        self.text = Text()
        
        self.list = []
        self.last_score = None
                
        self.background = pygame.image.load("assets/images/background/hall_of_fame.png")
        self.background = pygame.transform.scale(self.background, (self.game.screen.get_width(), self.game.screen.get_height()))
        
        self.frame = pygame.image.load("assets/images/background/frame_hall_of_fame.png")
        self.frame = pygame.transform.scale(self.frame, (int(self.game.screen.get_width() * 0.6), self.game.screen.get_height()))
        
        self.little_frame = pygame.image.load("assets/images/background/little_frame_hall_of_fame.png")
        self.little_frame = pygame.transform.scale(self.little_frame, (int(self.frame.get_width() * 0.5), int(self.frame.get_height() * 0.74)))
        
        self.rectangle = pygame.image.load("assets/images/rectangle.png")
        self.rectangle = pygame.transform.scale(self.rectangle, (int(self.rectangle.get_width() * 0.9), int(self.rectangle.get_height() * 0.9)))
        
        self.gold_star = pygame.image.load("assets/images/sprites/gold_star.png")
        self.silver_star = pygame.image.load("assets/images/sprites/silver_star.png")
        self.empty_star = pygame.image.load("assets/images/sprites/empty_star.png")
        
        self.x_button = pygame.image.load("assets/images/sprites/x_button.png")
        self.x_button = pygame.transform.scale(self.x_button, (int(self.x_button.get_width() * 0.5), int(self.x_button.get_height() * 0.5)))
        
        self.replay_button = pygame.image.load("assets/images/sprites/replay_button.png")
        self.replay_button = pygame.transform.scale(self.replay_button, (int(self.replay_button.get_width() * 0.5), int(self.replay_button.get_height() * 0.5)))
        
    def draw(self):
        self.game.screen.blit(self.background, (0,0))
        self.game.screen.blit(self.frame, (self.game.screen.get_width() //2 - self.frame.get_width() // 2, 0))
        self.game.screen.blit(self.little_frame, (self.game.screen.get_width() //2 - self.little_frame.get_width() // 2, int(self.game.screen.get_height() * 0.21)))
        
        for i, score in enumerate(self.list):
            self.game.screen.blit(self.rectangle, (self.game.screen.get_width() //2 - self.rectangle.get_width() // 2, int(self.game.screen.get_height() * 0.23) + i* int(self.game.screen.get_height() * 0.14)))
            self.text.draw_text(self.game.screen, f"{score['user_name']} - {int(score['score'])}", self.game.screen.get_width()//2 - int(self.game.screen.get_width() * 0.07), int(self.game.screen.get_height() * 0.26) + i* int(self.game.screen.get_height() * 0.14), int(self.game.screen.get_width() * 0.1), "score_font", (255,255,255))
            
            if i == 0:
                self.game.screen.blit(self.gold_star, (self.game.screen.get_width() //2 - self.gold_star.get_width() - int(self.game.screen.get_width() * 0.1), int(self.game.screen.get_height() * 0.2) + i* int(self.game.screen.get_height() * 0.1)))
            elif i == 1:
                self.game.screen.blit(self.silver_star, (self.game.screen.get_width() //2 - self.silver_star.get_width() - int(self.game.screen.get_width() * 0.1), int(self.game.screen.get_height() * 0.2) + i* int(self.game.screen.get_height() * 0.1)))
            elif i == 2:
                self.game.screen.blit(self.empty_star, (self.game.screen.get_width() //2 - self.empty_star.get_width() - int(self.game.screen.get_width() * 0.1), int(self.game.screen.get_height() * 0.2) + i* int(self.game.screen.get_height() * 0.1)))
                
        if self.last_score:
            self.text.draw_text(self.game.screen, f"LAST SCORE : {self.last_score['user_name']} - {int(self.last_score['score'])}", self.game.screen.get_width()//2 - int(self.game.screen.get_width() * 0.4), int(self.game.screen.get_height() * 0.05), int(self.game.screen.get_width() * 0.2), "last_score_font", (255,255,255))
            
        self.game.screen.blit(self.x_button, (self.game.screen.get_width() //2 + self.x_button.get_width() * 4 - int(self.game.screen.get_width() * 0.03), self.game.screen.get_height() - self.x_button.get_height() - int(self.game.screen.get_height() * 0.05)))
        if self.game.score != None:
            self.game.screen.blit(self.replay_button, (self.game.screen.get_width() //2 + self.replay_button.get_width() * 5 + int(self.game.screen.get_width() * 0.01), self.game.screen.get_height() - self.replay_button.get_height() - int(self.game.screen.get_height() * 0.05)))    
    
    def update(self, list, last_score):
        self.list = list
        self.last_score = last_score
        print(self.last_score)