import pygame
import sys
from model import ProjectileModel






class ProjectileView:
    def __init__(self,project_screen):
        self.clock = pygame.time.Clock()
        self.projectile_model = ProjectileModel()
        self.project_screen = project_screen

    def run(self):
        running = True
        while running:
            dt = self.clock.tick(60)  # dt représente le temps écoulé depuis la dernière frame, en millisecondes
            self.project_screen.fill((0, 0, 0))

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
            projectile.draw(self.project_screen)

    def handle_event(self, event):
        pass


