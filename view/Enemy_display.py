import pygame
class Enemy_display:
    def __init__(self) -> None:
        pass
    def update(self, screen, x, y):
        pygame.draw.rect(screen, (255, 0, 0), (x - 25, y - 25, 50, 50))