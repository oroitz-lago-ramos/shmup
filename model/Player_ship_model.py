from model.Moving_entity import Moving_entity
from model.Canon_model import Canon_model

class Player_ship_model(Moving_entity):
    """A class that represents the player ship in the game. It inherits from the Moving_entity class.
    arg: x, y, width, height, acceleration, max_speed, color
    attributes: x, y, width, height, direction, acceleration, max_speed, deceleration, health, canons
    """

    def __init__(self, x, y, width, height, acceleration, max_speed, color):
        super().__init__(x, y, width, height, acceleration, max_speed, color)
        self.timer_decelerate = 0
        self.deceleration = 2
        self.health = 100
        self.canons = [Canon_model(self.x, self.y, 5, 5, (0, 0, 255), (0, 1))]

    def decelerate(self):
        if self.velocity.length() > 0:
            if self.velocity.length() > self.deceleration:
                self.velocity.scale_to_length(max(0, self.velocity.length() - self.deceleration))
                print(self.velocity.length())
            else:
                super().stop()
            
    def update_canons(self):
        for canon in self.canons:
            canon.update(self.x,self.y)
        