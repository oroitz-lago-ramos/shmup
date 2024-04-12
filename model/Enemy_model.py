from model.Moving_entity import Moving_entity
import random
from pygame import math


class Enemy_model(Moving_entity):
    def __init__(self, width, height, acceleration, max_speed, color, max_health, player_base_position,x , y):
        super().__init__(x, y, width, height, acceleration, max_speed, color)
        self.velocity = math.Vector2(1, 1)
        self.max_health = max_health
        self.health = max_health
        self.player_base_position = player_base_position
        self.second_phase = False
        self.determine_direction()
        self.death = False
    
    def get_health(self):
        return self.health
    def take_damage(self, damage):
        self.health -= damage
    def get_phase(self):
        return self.second_phase
    def set_second_phase(self):
        self.second_phase = True
        self.acceleration = 0.5
        self.max_speed = 2
        
    def update(self):
        self.move()
        self.check_if_alive()
    
    def determine_direction(self):
        # Calculate the direction of the enemy
        # The direction is calculated by the difference between the player_base position and the enemy's position
        direction = self.player_base_position - self.get_center()
        self.set_direction_velocity(direction)
    
    def check_if_alive(self):
        if self.health <= 0:
            self.death = True
    def kill(self):
        self.death = True
    
    
    
    
    