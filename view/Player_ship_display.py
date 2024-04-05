import pygame

class Player_ship_display:
    def __init__(self, player_ship):
        self.player_ship = player_ship
    def draw_on_center(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.player_ship.x - 10, self.player_ship.y - 10, 20, 20))