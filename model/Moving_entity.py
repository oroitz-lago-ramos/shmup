from model.Entity_model import Entity_model

class Moving_entity (Entity_model):
    def __init__(self, x, y, width, height, image, speed):
        super().__init__(x, y, width, height, image)
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

    def update(self):
        self.move()
        self.rect.topleft = (self.x, self.y)

    def get_direction(self):
        return self.direction
    
    def set_direction(self, direction):
        self.direction = direction