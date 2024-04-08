import pygame
import math
import sys

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

        def draw(self, screen):
            pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), self.radius)

    def __init__(self):
        self.projectiles = []
        self.time_since_last_shot = 0

    def update_time(self, dt):
        self.time_since_last_shot += dt

        # Créer un nouveau projectile toutes les 500 millisecondes (0.5 seconde)
        if self.time_since_last_shot >= 200:
            angle = math.atan2(pygame.mouse.get_pos()[1] - 300, pygame.mouse.get_pos()[0] - 400)
            new_projectile = self.Projectile(400, 300, angle, 5)
            self.projectiles.append(new_projectile)
            self.time_since_last_shot = 0  # Réinitialiser le temps écoulé

        # Mise à jour des projectiles
        for projectile in self.projectiles:
            projectile.update()

        # Suppression des projectiles hors de l'écran
        self.projectiles = [projectile for projectile in self.projectiles if
                            0 <= projectile.x <= 800 and 0 <= projectile.y <= 600]

class ProjectileView:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.projectile_model = ProjectileModel()

    def run(self):
        running = True
        while running:
            dt = self.clock.tick(60)  # dt représente le temps écoulé depuis la dernière frame, en millisecondes
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.projectile_model.update_time(dt)
            self.draw()

            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def draw(self):
        for projectile in self.projectile_model.projectiles:
            projectile.draw(self.screen)

if __name__ == "__main__":
    projectile_view = ProjectileView()
    projectile_view.run()
