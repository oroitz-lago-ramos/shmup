from model.Entity_model import Entity_model

class Moving_entity (Entity_model):
    """A class that represents a moving entity in the game. It inherits from the Entity_model class.
    arg: x, y, width, height, speed, image
    attributes: x, y, width, height, speed, image, direction
    """
    def __init__(self, x, y, width, height, speed, color):
        super().__init__(color, x , y, width, height)
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = speed

    def move_up(self):
        self.y -= self.speed
        self.velocity_y = -self.speed
        self.velocity_x = 0
    
    def move_down(self):
        self.y += self.speed
        self.velocity_y = self.speed
        self.velocity_x = 0
    
    def move_left(self):
        self.x -= self.speed
        self.velocity_x = -self.speed
        self.velocity_y = 0
    
    def move_right(self):
        self.x += self.speed
        self.velocity_x = self.speed
        self.velocity_y = 0

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def update(self):
        self.move()


    def get_direction(self):
        return self.direction
    
    def set_direction(self, direction):
        self.direction = direction