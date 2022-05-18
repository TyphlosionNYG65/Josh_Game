import Textures, Type


class Joshumon:
    def __init__(self,lvl,moves):
        self.lvl = lvl
        self.moveset = moves

    def calc_stats(self):
        self.HP = self.base_HP + self.lvl
        self.AT = int(self.base_Attack + self.lvl/2)
        self.SD = int(self.base_Speed + self.lvl/2)

    def lvl_up(self):
        self.lvl += 1
        self.calc_stats()


class Durple(Joshumon):
    def __init__(self,lvl,moves):
        super().__init__(self,lvl,moves)
        self.type1 = Type.Lean
        self.type2 = Type.Furry
        self.front_pic = Textures.Durple_Front
        self.back_pic = Textures.Durple_Back
        self.base_HP = 100
        self.base_Attack = 80
        self.base_Speed = 120
        self.calc_stats()


class The_Coon(Joshumon):
    def __init__(self,lvl,moves):
        super().__init__(self,lvl,moves)
        self.type1 = Type.Racism
        self.type2 = Type.Virgin
        self.front_pic = Textures.Coon_Front
        self.back_pic = Textures.Coon_Back
        self.base_HP = 150
        self.base_Attack = 120
        self.base_Speed = 30
        self.calc_stats()



