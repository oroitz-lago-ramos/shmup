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
        self.gold_star = pygame.transform.scale(self.gold_star, (int(self.gold_star.get_width() * 0.8), int(self.gold_star.get_height() * 0.8)))
        self.silver_star = pygame.transform.scale(self.silver_star, (int(self.silver_star.get_width() * 0.8), int(self.silver_star.get_height() * 0.8)))
        self.empty_star = pygame.transform.scale(self.empty_star, (int(self.empty_star.get_width() * 0.8), int(self.empty_star.get_height() * 0.8)))
        
        self.x_button = pygame.image.load("assets/images/sprites/x_button.png")
        self.x_button = pygame.transform.scale(self.x_button, (int(self.x_button.get_width() * 0.5), int(self.x_button.get_height() * 0.5)))
        
        self.replay_button = pygame.image.load("assets/images/sprites/replay_button.png")
        self.replay_button = pygame.transform.scale(self.replay_button, (int(self.replay_button.get_width() * 0.5), int(self.replay_button.get_height() * 0.5)))
        
    def draw(self):
        self.game.screen.blit(self.background, (0,0))
        self.game.screen.blit(self.frame, (self.game.screen.get_width() //2 - self.frame.get_width() // 2, 0))
        self.game.screen.blit(self.little_frame, (self.game.screen.get_width() //2 - self.little_frame.get_width() // 2, int(self.game.screen.get_height() * 0.205)))
        
        for i, score in enumerate(self.list):
            if self.last_score and score['score'] == self.last_score['score'] and score['user_name'] == self.last_score['user_name']:
                color = (0,255,0)
            else:
                color = (255,255,255)
            if i == 0:
                self.game.screen.blit(self.rectangle, (self.game.screen.get_width() //2 - self.rectangle.get_width() // 2, int(self.game.screen.get_height() * 0.23) + i* int(self.game.screen.get_height() * 0.14)))
                self.text.draw_text(self.game.screen, f"{score['user_name']} - {int(score['score'])}", self.game.screen.get_width()//2 - int(self.game.screen.get_width() * 0.07), int(self.game.screen.get_height() * 0.26) + i* int(self.game.screen.get_height() * 0.14), int(self.game.screen.get_width() * 0.1), "score_font", color)
                self.game.screen.blit(self.gold_star, (self.game.screen.get_width() //2 - self.gold_star.get_width() - int(self.game.screen.get_width() * 0.075), int(self.game.screen.get_height() * 0.25) + i* int(self.game.screen.get_height() * 0.15)))
            elif i == 1:
                self.game.screen.blit(self.rectangle, (self.game.screen.get_width() //2 - self.rectangle.get_width() // 2, int(self.game.screen.get_height() * 0.23) + i* int(self.game.screen.get_height() * 0.14)))
                self.text.draw_text(self.game.screen, f"{score['user_name']} - {int(score['score'])}", self.game.screen.get_width()//2 - int(self.game.screen.get_width() * 0.07), int(self.game.screen.get_height() * 0.26) + i* int(self.game.screen.get_height() * 0.14), int(self.game.screen.get_width() * 0.1), "score_font", color)
                self.game.screen.blit(self.silver_star, (self.game.screen.get_width() //2 - self.silver_star.get_width() - int(self.game.screen.get_width() * 0.075), int(self.game.screen.get_height() * 0.245) + i* int(self.game.screen.get_height() * 0.15)))
            elif i == 2:
                self.game.screen.blit(self.rectangle, (self.game.screen.get_width() //2 - self.rectangle.get_width() // 2, int(self.game.screen.get_height() * 0.23) + i* int(self.game.screen.get_height() * 0.14)))
                self.text.draw_text(self.game.screen, f"{score['user_name']} - {int(score['score'])}", self.game.screen.get_width()//2 - int(self.game.screen.get_width() * 0.07), int(self.game.screen.get_height() * 0.26) + i* int(self.game.screen.get_height() * 0.14), int(self.game.screen.get_width() * 0.1), "score_font", color)
                self.game.screen.blit(self.empty_star, (self.game.screen.get_width() //2 - self.empty_star.get_width() - int(self.game.screen.get_width() * 0.077), int(self.game.screen.get_height() * 0.24) + i* int(self.game.screen.get_height() * 0.15)))
            elif i == 4:
                if self.game.score != None and self.last_score:
                    self.game.screen.blit(self.rectangle, (self.game.screen.get_width() //2 - self.rectangle.get_width() // 2, int(self.game.screen.get_height() * 0.23) + i* int(self.game.screen.get_height() * 0.14)))
                    self.text.draw_text(self.game.screen, f"{self.last_score['user_name']} - {int(self.last_score['score'])}", self.game.screen.get_width()//2 - int(self.game.screen.get_width() * 0.07), int(self.game.screen.get_height() * 0.26) + i* int(self.game.screen.get_height() * 0.14), int(self.game.screen.get_width() * 0.1), "score_font", (0,255,0))
                else:
                    self.game.screen.blit(self.rectangle, (self.game.screen.get_width() //2 - self.rectangle.get_width() // 2, int(self.game.screen.get_height() * 0.23) + i* int(self.game.screen.get_height() * 0.14)))
                    self.text.draw_text(self.game.screen, f"{score['user_name']} - {int(score['score'])}", self.game.screen.get_width()//2 - int(self.game.screen.get_width() * 0.07), int(self.game.screen.get_height() * 0.26) + i* int(self.game.screen.get_height() * 0.14), int(self.game.screen.get_width() * 0.1), "score_font", color)
            else:
                self.game.screen.blit(self.rectangle, (self.game.screen.get_width() //2 - self.rectangle.get_width() // 2, int(self.game.screen.get_height() * 0.23) + i* int(self.game.screen.get_height() * 0.14)))
                self.text.draw_text(self.game.screen, f"{score['user_name']} - {int(score['score'])}", self.game.screen.get_width()//2 - int(self.game.screen.get_width() * 0.07), int(self.game.screen.get_height() * 0.26) + i* int(self.game.screen.get_height() * 0.14), int(self.game.screen.get_width() * 0.1), "score_font", color)
            
        
        self.game.screen.blit(self.x_button, (self.game.screen.get_width() //2 + self.x_button.get_width() * 4 - int(self.game.screen.get_width() * 0.025), self.game.screen.get_height() - self.x_button.get_height() - int(self.game.screen.get_height() * 0.05)))
        if self.game.score != None:
            self.game.screen.blit(self.replay_button, (self.game.screen.get_width() //2 + self.replay_button.get_width() * 4.8, self.game.screen.get_height() - self.replay_button.get_height() - int(self.game.screen.get_height() * 0.05)))
            self.text.draw_text(self.game.screen, f"GAME ENDED!", self.game.screen.get_width()//2 - int(self.game.screen.get_width() * 0.15), int(self.game.screen.get_height() * 0.05), int(self.game.screen.get_width() * 0.2), "last_score_font", (255,255,255))
        else:
            self.text.draw_text(self.game.screen, f"SCOREBOARD", self.game.screen.get_width()//2 - int(self.game.screen.get_width() * 0.15), int(self.game.screen.get_height() * 0.05), int(self.game.screen.get_width() * 0.2), "last_score_font", (255,255,255))
            
    
    def update(self, list, last_score):
        self.list = list
        self.last_score = last_score
    