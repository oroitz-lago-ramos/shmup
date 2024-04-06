from model.Moving_entity import Moving_entity

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
        self.canons = []

    def decelerate(self):
        if self.velocity.length() > 0:
            if self.velocity.length() > self.deceleration:
                self.velocity.scale_to_length(max(0, self.velocity.length() - self.deceleration))
                print(self.velocity.length())
            else:
                super().stop()
        