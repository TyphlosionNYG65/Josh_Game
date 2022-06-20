from asset_handling import Textures
import pygame
import random

from game_clock import clock
from screen_parameters import screen_vals, screen


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


def update_velocities(Entities):
    for i in Entities:
        if type(i) == list:
            update_velocities(i)
        else:
            i.update_velocity()


def paste_entities(Entities):
    for i in Entities:
        if type(i) == list:
            paste_entities(i)
        else:
            screen.blit(i.pic, (i.x, i.y))


def spawner(Zombies):
    spawn = random.choices([True, False], weights=(.005, .99))
    if spawn[0] == True:
        side = random.randrange(0, 2)
        speed = random.randrange(100, 300)
        height = random.randrange(50, screen_vals.height - 50)
        image = random.choices([Textures.Josh_Texture])[0]
        if side == 0:
            return Start_Zombie(-30, height, image, 43, 64, (speed, 0), 'left')
        elif side == 1:
            return Start_Zombie(screen_vals.width + 30, height, image, 43, 64, (-1 * speed, 0), 'right')


def update(zombies):
    if zombies == []:
        return
    for i in zombies:
        if i == None:
            return
        i.update_position()
        if i.out_of_screen():
            zombies.remove(i)
        screen.blit(i.pic, (i.x, i.y))
