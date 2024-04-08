from model.Moving_entity import Moving_entity
import random
from pygame import math


class Enemy_model(Moving_entity):
    def __init__(self, width, height, acceleration, max_speed, color, max_health, player_base_position):
        self.x, self.y = random.randint(0, 800), random.randint(0, 600)
        super().__init__(self.x, self.y, width, height, acceleration, max_speed, color)
        self.velocity = math.Vector2(1, 1)
        self.max_health = max_health
        self.health = max_health
        self.player_base_position = player_base_position
        self.determine_direction()
    
    def get_health(self):
        return self.health
    def take_damage(self, damage):
        self.health -= damage
        
    def update(self):
        self.move()
    
    def determine_direction(self):
        # Calculate the direction of the enemy
        # The direction is calculated by the difference between the player_base position and the enemy's position
        direction = self.player_base_position - self.get_center()
        self.set_direction_velocity(direction)
    
    
    