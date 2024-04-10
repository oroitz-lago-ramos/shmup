from model.Entity_model import Entity_model
from model.Projectile_model import Projectile_model
from pygame.math import Vector2 
import math

class Canon_model(Entity_model):
    """A class that represents a canon in the game. It inherits from the Entity_model class.
    arg: x, y, width, height, color, direction
    attributes: x, y, width, height, color, direction, projectiles_list"""
    def __init__(self, x, y, width, height, color, direction):
        super().__init__(color, x, y, width, height)
        self.direction = Vector2(direction)
        
        self.projectiles = []
        self.time_since_last_shot = 0
        self.screen_width = width
        self.screen_height = height
    
    def update_direction(self, direction):
        self.direction = direction
    
    def calcule_angle(self, direction):
        self.update_direction(self.direction)
        return self.direction.angle_to(Vector2(direction))
    
    def set_projectiles_list(self, projectiles_list):
        """Set the projectiles list of the canon
        arg: projectiles_list
        appends the projectiles_list to the canon's projectiles_list"""
        self.projectiles_list.append(projectiles_list)
    
    def get_projectiles_list(self):
        return self.projectiles_list

    def set_direction(self, direction):
        self.direction = direction.normalize()

    def get_direction(self):
        return self.direction
    
    def get_position(self):
        return self.x, self.y
    
    def shoot(self):
        pass

    def update(self, x, y, dt, mouse):
        self.x = x
        self.y = y
        self.update_projectiles(dt, x, y, mouse)
        

    def update_projectiles(self, dt, ship_x, ship_y, mouse):
        self.time_since_last_shot += dt

        if self.time_since_last_shot >= 300:
            mouse_x, mouse_y = mouse
            angle = math.atan2(mouse_y - ship_y, mouse_x - ship_x)
            new_projectile = Projectile_model(ship_x, ship_y, angle, 25)
            self.projectiles.append(new_projectile)
            self.time_since_last_shot = 0  # Réinitialiser le temps écoulé


        # Mise à jour des projectiles
        for projectile in self.projectiles:
            projectile.update()

        # Suppression des projectiles hors de l'écran
        # self.projectiles = [projectile for projectile in self.projectiles if
        #                     0 <= projectile.x <= self.screen_width and 0 <= projectile.y <= self.screen_height]#remplacer les valeur par celle de l'écran 
        
