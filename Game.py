import pygame
pygame.init()
from screen_parameters import *
from Start_Screen import Start
from Battle import Battle,Trainer
import Joshumon, Moves
# TODO: Pre-battle Joshumon selection screen

def main():
    running = True
    while running:
        Start()
        pygame.mixer.music.pause
        Battle(Trainer.Player('Josh pinsky',[Joshumon.Durple(50,[Moves.Bite,Moves.Bark]),Joshumon.Muscle_Man(50,[Moves.Punch,Moves.Kick])]),Trainer.AI_Trainer('Drio',[Joshumon.The_Coon(50,[Moves.Coon_Claws,Moves.Coon_Pounce])]))

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
