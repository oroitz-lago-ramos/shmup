class Player_ship_model:
    def __init__(self):
        self.x = 500
        self.y = 500
        

        
        
    def move(self, direction):
        pass
    
    def move_up(self):
        self.y -= 20
    def move_down(self):
        self.y += 20
    def move_left(self):
        self.x -= 20
    def move_right(self):
        self.x += 20
        
