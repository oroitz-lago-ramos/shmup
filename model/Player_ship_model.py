from model.Moving_entity import Moving_entity
class Player_ship_model(Moving_entity):
    def __init__(self, x, y, width, height, speed):
        super().__init__(x, y, width, height, speed)
        self.direction = 1
        self.canons = []
        
    def move(self, direction):
        pass
    
    def move_up(self):
        self.y -= self.speed
    def move_down(self):
        self.y += self.speed
    def move_left(self):
        self.x -= self.speed
    def move_right(self):
        self.x += self.speed
        
