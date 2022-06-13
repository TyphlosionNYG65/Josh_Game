
import pygame
pygame.init()
from screen_parameters import *
from Start_Screen import Start
from Textures import SelectScreen1
from battle_sim_selection import select_screen
from Battle import Battle,Trainer
import Joshumon, Moves
# TODO: Pre-battle Joshumon selection screen

def main():
    running = True
    current_screen = 'start'
    while running:
        if current_screen == 'start':
            current_screen = Start()

        elif current_screen == 'battle':
            current_screen = select_screen(SelectScreen1)

        else:
            running = False


if __name__ == "__main__":
    main()