from pygame import math
class Entity_model:
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
#==================================Getters and Setters==================================#
        #==================Setters==================#
    def set_color(self, color):
        self.color = color
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height

        #==================Getters==================#
    def get_color(self):
        return self.color
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def get_center(self):
        return math.Vector2(self.x + self.width // 2, self.y + self.height // 2)

        