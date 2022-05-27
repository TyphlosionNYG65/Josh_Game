import pygame,random

class Player:
    def __init__(self,name,Joshumons):
        self.Joshumons = Joshumons
        self.current_mon = None
        self.name = name

    def start_battle(self):
        for mon in self.Joshumons:
            if mon.fainted == False:
                self.current_mon = mon
                return
        self.current_mon = None


class AI_Trainer(Player):
    def __init__(self,name,Joshumons):
        super().__init__(name,Joshumons)

    def AI_Move(self):
        return random.choices(self.current_mon.moveset)[0]

















