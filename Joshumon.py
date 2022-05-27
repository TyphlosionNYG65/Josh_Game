import Textures, Type,pygame


class Joshumons:
    def __init__(self,lvl,moves):
        self.lvl = lvl
        self.moveset = moves
        self.fainted = False

    def calc_stats(self):
        self.HP = self.base_HP + self.lvl
        self.AT = int(self.base_Attack + self.lvl/2)
        self.SD = int(self.base_Speed + self.lvl/2)
        self.D = int(self.base_Defense + self.lvl/2)

    def lvl_up(self):
        self.lvl += 1
        self.calc_stats()

    def attack(self,target,move):
        damage = (self.AT/target.D) * move.power
        type_mult = 1
        type_mult *= target.type1.multipliers[move.type.name]
        if target.type2 != None:
            type_mult *= target.type1.multipliers[move.type.name]
        if type_mult == 1:
            variant = None
        elif type_mult > 1:
            variant = 'Supereffective'
        elif 1> type_mult > 0:
            variant = 'Noteffective'
        elif type_mult == 0:
            variant = 'None'

        return damage * type_mult, variant




    def recalc_HP(self,damage):
        self.current_HP -= damage
        if self.current_HP <= 0:
            self.current_HP = 0
            self.fainted = True


class Durple(Joshumons):
    def __init__(self,lvl,moves):
        super().__init__(lvl,moves)
        self.type1 = Type.Lean
        self.type2 = Type.Furry
        self.front_pic = Textures.Durple_Front
        self.back_pic = Textures.Durple_Back
        self.user_sprite = pygame.transform.smoothscale(self.back_pic,(232,340))
        self.base_HP = 100
        self.base_Defense = 50
        self.base_Attack = 80
        self.base_Speed = 120
        self.calc_stats()
        self.current_HP = self.HP
        self.name = 'Durple'


class The_Coon(Joshumons):
    def __init__(self,lvl,moves):
        super().__init__(lvl,moves)
        self.type1 = Type.Racism
        self.type2 = Type.Virgin
        self.front_pic = Textures.Coon_Front
        self.back_pic = Textures.Coon_Back
        self.opp_sprite = pygame.transform.smoothscale(self.front_pic,(260,200))
        self.base_HP = 150
        self.base_Defense = 50
        self.base_Attack = 120
        self.base_Speed = 30
        self.calc_stats()
        self.current_HP = self.HP
        self.name = 'The Coon'



