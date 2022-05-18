import pygame


class screen_size:
    def __init__(self):
        self.width = 0
        self.height = 0


screen_vals = screen_size()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_vals.width, screen_vals.height = screen.get_size()
FPS = 120
