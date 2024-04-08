import pygame
from view.Canon_display import Canon_display

class Player_ship_display:
    def __init__(self, player_ship):
        self.player_ship = player_ship
        self.canon_display = Canon_display(self.player_ship.canons[0])

    def draw_on_center(self, screen, x , y):
        pygame.draw.rect(screen, (255, 0, 0), (x - 10, y - 10, 39, 95))
        self.canon_display.draw_on_center(screen, x, y)
        