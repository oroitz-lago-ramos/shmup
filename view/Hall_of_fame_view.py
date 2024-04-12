from view.Text import Text

class Hall_of_fame_view:
    def __init__(self, game):
        self.game = game
        self.text = Text()
        self.list = []
    def draw(self):
        self.text.draw_text(self.game.screen, "Hall of fame", self.game.screen.get_width()/2, 50, 60, "none_font", (0,0,0))
        self.text.draw_text(self.game.screen, "Press ESC to go back to the main menu", self.game.screen.get_width()/2 - 200, 100 , 40, "none_font", (0,0,0))
        self.text.draw_text(self.game.screen, "Press R to reset the hall of fame", self.game.screen.get_width()/2 + 200, 100, 40, "none_font", (0,0,0))
        
        for i, score in enumerate(self.list):
            # print(i, score)
            self.text.draw_text(self.game.screen, f"{score['user_name']} : {score['score']}", self.game.screen.get_width()/2, 200 + i*50, 40, "none_font", (0,0,0))
    
    def update(self, list):
        self.list = list
