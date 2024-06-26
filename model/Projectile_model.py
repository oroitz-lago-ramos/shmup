import pygame
import math
from pygame import mixer

class Projectile_model:
    """A class that represents a projectile in the game"""
    def __init__(self, x, y, angle, speed):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.radius = 5  # Rayon du projectile
        
        mixer.init()
        self.shoot_sound = mixer.Sound("./assets/vfx/sounds/laser-gun-shot.mp3")
        self.shoot_sound.set_volume(0.05)
        self.shoot_sound.play()

    def update(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

    
       
        
    