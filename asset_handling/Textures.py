import os
import pygame
import shelve

from screen_parameters import screen

def load(Image):
    """
    Takes as input a file name - Image from the Image Folder in assets and returns a pygame image
    """
    try:
        path = os.path.join(os.getcwd(), 'assets\Images', Image)
        return pygame.image.load(path)
    except FileNotFoundError:
        game_directory = os.path.normpath(os.getcwd() + os.sep + os.pardir)
        path = os.path.join(game_directory, 'assets\Images',Image)
    return pygame.image.load(path)

Josh_Texture = load('Josh.png')
Start_screen = load('Start screen.jpg')
start_title = load('inkpx-word-art.png')
Durple = load('Durple_Front.png')
Coon = load('The Coon Front.png')
MuscleMan = load('MuscleMan.png')
HamHelp = load('Hamburger Helper.png')
FatFuck = load('CptFatFuck.png')
Drip = load('Drip.png')
Lorax = load('lorax.png')
Duck = load('Duck.png')
JeffFisher = load('Jeff Fisher.png')
NikoCado = load('NikoCado.png')
armin = load('armin.png')
KKK = load('KKK.png')
Schnitzel = load('Schnitzel.png')
Mort = load('Mort.png')
teddy = load('Teddy.png')
johnny = load('johnny.png')
Garfield = load('Garfield.png')
John = load('John Darksouls.png')
Priest = load('priest.png')
Otter = load('otter.png')
Strapichu = load('Strapichu.png')
Clamantha = load('clamantha.png')
Yaoyorozu = load('Yaoyorozu.png')
smokey = load('smokey.png')
HP_High = load('HP_High.png')
HP_Low = load('HP_low.png')
HP_Back = load('HP_Back.png')
HP_Border = load('HP_border.png')
plus = load('plus.png')
down = load('arrow.png')
up = pygame.transform.flip(down, False, True)


class gif:
    def __init__(self, gif):
        directory = os.path.join(os.getcwd(), 'assets\\gifs', gif)
        directory2 = os.listdir(directory)
        self.frames = [pygame.image.load(os.path.join(directory, filename)) for filename in directory2]
        self.frame_size = len(self.frames)
        self.current_frame = [self.frames[0], 0]
        self.start_time = 0

    def paste(self, position):
        if pygame.time.get_ticks() - self.start_time >= 1000 / self.frame_size:
            self.start_time = pygame.time.get_ticks()

            if self.current_frame[1] == self.frame_size:
                self.current_frame[1] = 0
            self.current_frame[0] = self.frames[self.current_frame[1]]
            self.current_frame[1] += 1
        screen.blit(self.current_frame[0], position)

    def scale(self, size):
        for num in range(self.frame_size):
            self.frames[num] = pygame.transform.scale(self.frames[num], size)


Fight_Background1 = gif('FightBackground1-gif')
SelectScreen1 = gif('SelectScreen1')
