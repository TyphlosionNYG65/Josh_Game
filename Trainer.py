import pygame

class Player:
    def __init__(self,Joshumons,):
        self.Joshumons = Joshumons
        self.current_mon = None

    def start_battle(self):
        self.current_mon = self.Joshumons[0]


class AI_Trainer(Player):
    def __init__(self):
        super().__init__(self)

















