from model.Moving_entity import Moving_entity
class Player_ship_model(Moving_entity):
    """A class that represents the player ship in the game. It inherits from the Moving_entity class.
    arg: x, y, width, height, speed
    attributes: x, y, width, height, speed, canons
    """
    def __init__(self, x, y, width, height, speed):
        super().__init__(x, y, width, height, speed, color=(255, 255, 255))
        self.canons = []

    def move_up(self):
        self.y -= self.speed
        self.direction = 1
    def move_down(self):
        self.y += self.speed
        self.direction = 2
    def move_left(self):
        self.x -= self.speed
        self.direction = 3
    def move_right(self):
        self.x += self.speed
        self.direction = 4        
