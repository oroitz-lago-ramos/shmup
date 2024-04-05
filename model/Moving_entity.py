from model.Entity_model import Entity_model

class Moving_entity (Entity_model):
    """A class that represents a moving entity in the game. It inherits from the Entity_model class.
    arg: x, y, width, height, speed, image
    attributes: x, y, width, height, speed, image, direction
    """
    def __init__(self, x, y, width, height, speed, color):
        super().__init__(color, x , y, width, height)
        self.speed = speed
        self.direction = 1

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

    def move(self):
        if self.direction == 1:
            self.move_up()
        elif self.direction == 2:
            self.move_down()
        elif self.direction == 3:
            self.move_left()
        elif self.direction == 4:
            self.move_right()

    def update(self):
        self.move()


    def get_direction(self):
        return self.direction
    
    def set_direction(self, direction):
        self.direction = direction