import pygame
import math

class ProjectileModel:
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

    def __init__(self):
        self.projectiles = []
        self.time_since_last_shot = 0

    def update_time(self, dt):
        self.time_since_last_shot += dt

        # Créer un nouveau projectile toutes les 500 millisecondes (0.5 seconde)
        if self.time_since_last_shot >= 500:
            angle = math.atan2(pygame.mouse.get_pos()[1] - 300, pygame.mouse.get_pos()[0] - 400)#400 et 300 à remplacer par width /2 et height /2
            new_projectile = self.Projectile(400, 300, angle, 5)
            self.projectiles.append(new_projectile)
            self.time_since_last_shot = 0  # Réinitialiser le temps écoulé

        # Mise à jour des projectiles
        for projectile in self.projectiles:
            projectile.update()

        # Suppression des projectiles hors de l'écran
        self.projectiles = [projectile for projectile in self.projectiles if
                            0 <= projectile.x <= 800 and 0 <= projectile.y <= 600]#remplacer les valeur par celle de l'écran 