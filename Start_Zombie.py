import pygame
from screen_parameters import screen_vals
from game_clock import clock
class Start_Zombie:
    def __init__(self, x, y, pic, x_dim, y_dim, velocity, side):
        self.x = x
        self.y = y
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.pic_name = pic
        self.pic = pic
        self.pic = pygame.transform.scale(self.pic, (self.x_dim, self.y_dim))
        self.x_velocity = velocity[0]
        self.y_velocity = velocity[1]
        self.side = side

    def update_position(self):
        delta = clock.get_time()
        self.x += (delta / 1000) * self.x_velocity
        self.y += (delta / 1000) * self.y_velocity

    def out_of_screen(self):
        if -30 > self.x and self.side == 'right':
            del self
            return True
        elif self.x > screen_vals.width and self.side == 'left':
            del self
            return True
        return False