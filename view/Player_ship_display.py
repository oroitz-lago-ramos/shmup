import pygame

class Player_ship_display:
    def __init__(self, player_ship):
        self.player_ship = player_ship

    def draw_on_center(self, screen, x , y):
        pygame.draw.rect(screen, (255, 0, 0), (x - 10, y - 10, 39, 95))
        