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
        self.frame = pygame.transform.scale(self.frame, (self.game.screen.get_width() * 0.6, self.game.screen.get_height()))
        self.little_frame = pygame.image.load("assets/images/background/little_frame_hall_of_fame.png")
        self.little_frame = pygame.transform.scale(self.little_frame, (self.frame.get_width() * 0.5, self.frame.get_height() * 0.74))
        self.rectangle = pygame.image.load("assets/images/rectangle.png")
        self.rectangle = pygame.transform.scale(self.rectangle, (self.rectangle.get_width() - 5, self.rectangle.get_height() - 10))
        
        self.gold_star = pygame.image.load("assets/images/sprites/gold_star.png")
        self.silver_star = pygame.image.load("assets/images/sprites/silver_star.png")
        self.empty_star = pygame.image.load("assets/images/sprites/empty_star.png")
        
        self.x_button = pygame.image.load("assets/images/sprites/x_button.png")
        self.x_button = pygame.transform.scale(self.x_button, (self.x_button.get_width() // 2, self.x_button.get_height() // 2))
        self.replay_button = pygame.image.load("assets/images/sprites/replay_button.png")
        self.replay_button = pygame.transform.scale(self.replay_button, (self.replay_button.get_width() // 2, self.replay_button.get_height() // 2))
        
    
        
    def draw(self):
        self.game.screen.blit(self.background, (0,0))
        self.game.screen.blit(self.frame, (self.game.screen.get_width() //2 - self.frame.get_width() // 2, 0))
        self.game.screen.blit(self.little_frame, (self.game.screen.get_width() //2 - self.little_frame.get_width() // 2, self.game.screen.get_height() // 2 - self.little_frame.get_height() // 3 - 41))
        
        for i, score in enumerate(self.list):
            self.game.screen.blit(self.rectangle, (self.game.screen.get_width() //2 - self.rectangle.get_width() // 2, 220 + i* 125))
            self.text.draw_text(self.game.screen, f"{score['user_name']} - {int(score['score'])}", self.game.screen.get_width()//2 - 105, 250 + i* 125, 140, "score_font", (255,255,255))
            if i == 0:
                self.game.screen.blit(self.gold_star, (self.game.screen.get_width() //2 - self.gold_star.get_width() - 115, 232 + i* 125))
            elif i == 1:
                self.game.screen.blit(self.silver_star, (self.game.screen.get_width() //2 - self.silver_star.get_width() - 115, 235 + i* 125))
            elif i == 2:
                self.game.screen.blit(self.empty_star, (self.game.screen.get_width() //2 - self.empty_star.get_width() - 120, 232 + i* 130))
                
        if self.last_score:
            self.text.draw_text(self.game.screen, f"LAST SCORE : {self.last_score['user_name']} - {int(self.last_score['score'])}", self.game.screen.get_width()//2 - 430, 60, 250, "last_score_font", (255,255,255))
            
        self.game.screen.blit(self.x_button, (self.game.screen.get_width() //2 + self.x_button.get_width() * 4 - 30, self.game.screen.get_height() - self.x_button.get_height() - 60))
        if self.game.score != None:
            self.game.screen.blit(self.replay_button, (self.game.screen.get_width() //2 + self.replay_button.get_width() * 5 + 10, self.game.screen.get_height() - self.replay_button.get_height() - 60))    
      
    
    def update(self, list, last_score):
        self.list = list
        self.last_score = last_score
        print(self.last_score)