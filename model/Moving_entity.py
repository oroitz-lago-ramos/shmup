from model.Entity_model import Entity_model

from pygame import math
class Moving_entity (Entity_model):
    """A class that represents a moving entity in the game. It inherits from the Entity_model class.
    arg: x, y, width, height, acceleration, max_speed, color
    attributes: x, y, width, height, direction, acceleration, max_speed, deceleration
    """
    def __init__(self, x, y, width, height,acceleration, max_speed, color):
        super().__init__(color, x , y, width, height)
        self.direction = math.Vector2(0, 0)
        self.velocity = math.Vector2(0, 0)
        self.acceleration = acceleration
        self.max_speed = max_speed
        self.timer_decelerate = 0

    def set_direction_velocity(self, direction):
        self.direction = direction.normalize()
        self.velocity = self.direction * self.velocity.length()

    def get_direction(self):     
        return self.direction
    
    #==================================BASIC VECTOR MOUVEMENT FOR ENTITY==================================#

    def move_up(self):
        direction = math.Vector2(0, -1)
        self.set_direction(direction)
    
    def move_down(self):
        direction = math.Vector2(0, 1)
        self.set_direction(direction)
    
    def move_left(self):
        direction = math.Vector2(-1, 0)
        self.set_direction(direction)
    
    def move_right(self):
        direction = math.Vector2(1, 0)
        self.set_direction(direction)

    def accelerate(self):
        print(" direction length ", self.direction.length())
        if self.direction.length() > 0:
            self.velocity += self.direction * self.acceleration
            if self.velocity.length() != 0:
                self.velocity.scale_to_length(min(self.max_speed, self.velocity.length()))

    def stop(self): 
        self.velocity = math.Vector2(0, 0)
    
    def move(self):
        self.x += self.velocity.x
        self.y += self.velocity.y
    
    def update(self):
        self.accelerate()
        self.move()


    def get_direction(self):
        return self.direction
    
    def set_direction(self, direction):
        self.direction = direction