import pygame
import math

class Projectile_model:
    class Projectile:
        def __init__(self, x, y, angle, speed):
            self.x = x
            self.y = y
            self.angle = angle
            self.speed = speed
            self.radius = 5  # Rayon du projectile

        def update(self):
            self.x += self.speed * math.cos(self.angle)
            self.y += self.speed * math.sin(self.angle)

    def __init__(self, width, height):
        self.projectiles = []
        self.time_since_last_shot = 0
        self.screen_width = width
        self.screen_height = height
        
    def update_time(self, dt, ship_x, ship_y):
        self.time_since_last_shot += dt

        if self.time_since_last_shot >= 100:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            angle = math.atan2(mouse_y - ship_y, mouse_x - ship_x)
            new_projectile = self.Projectile(ship_x, ship_y, angle, 5)
            self.projectiles.append(new_projectile)
            self.time_since_last_shot = 0  # Réinitialiser le temps écoulé


        # Mise à jour des projectiles
        for projectile in self.projectiles:
            projectile.update()

        # Suppression des projectiles hors de l'écran
        self.projectiles = [projectile for projectile in self.projectiles if
                            0 <= projectile.x <= self.screen_width and 0 <= projectile.y <= self.screen_height]#remplacer les valeur par celle de l'écran 