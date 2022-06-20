import pygame
pygame.init()
from Start_Screen import Start
from asset_handling.Textures import SelectScreen1
from battle_sim_selection import select_screen
from Battle import Battle,Trainer
import Joshumon, Moves
import game_clock
# TODO: Pre-battle Joshumon selection screen

def main():
    running = True
    current_screen = 'start'
    Trainer1 = Trainer.Player('Josh',[Joshumon.Armin(50,[Moves.pH1,Moves.pH2])])
    Trainer2 = Trainer.AI_Trainer('e',[Joshumon.Clamantha(50,[Moves.pH1,Moves.pH2])])
    while running:
        if current_screen == 'start':
            current_screen = Start()

        elif current_screen == 'battle_select':
            current_screen = select_screen(SelectScreen1)

        else:
            running = False


if __name__ == "__main__":
    main()