import Interactives
import Textures
import Type
import pygame
import Text
from screen_parameters import screen_w, screen_h, screen

nametag_font = pygame.font.SysFont('arial', 20)
class Joshumons:

    def __init__(self, lvl=1, moves=[]):
        self.lvl = lvl
        self.moveset = moves
        self.fainted = False
        self.size_ratio = 1
        self.nametag = None
        self.width = 0

    # create battle tag for name,type,hp,level,etc
    HP_width = screen_w(196/1920)
    HP_height = screen_h(25/1080)
    tag_width = screen_w(200/1920)
    tag_height = screen_h(50/1080)
    tag = pygame.Surface((int(screen_w(tag_width / 1920)), int(screen_h(tag_height / 1080))))
    tag_outline = pygame.Surface((int(screen_w(tag_width / 1920) + 2), int(screen_h(tag_height / 1080) + 2)))
    tag.fill((255, 255, 255))
    tag_outline.fill((0, 0, 0))

    def calc_stats(self):
        self.HP = self.base_HP + self.lvl
        self.AT = int(self.base_Attack + self.lvl / 2)
        self.SD = int(self.base_Speed + self.lvl / 2)
        self.D = int(self.base_Defense + self.lvl / 2)

    def lvl_up(self):
        self.lvl += 1
        self.calc_stats()

    def attack(self, target, move):
        damage = (self.AT / target.D) * move.power
        type_mult = 1
        type_mult *= target.type1.multipliers[move.type.name]
        if target.type2 != None:
            type_mult *= target.type1.multipliers[move.type.name]
        if type_mult == 1:
            variant = None
        elif type_mult > 1:
            variant = 'Supereffective'
        elif 1 > type_mult > 0:
            variant = 'Noteffective'
        elif type_mult == 0:
            variant = 'None'

        return damage * type_mult, variant

    def scale(self, sprite, area):
        width = (area / self.size_ratio) ** 1 / 2
        height = width * self.size_ratio
        width, height = screen_w(width / 1920), screen_h(height / 1080)
        return pygame.transform.smoothscale(sprite, (width, height))

    def paste(self, x, y, orientation, sprite,nametag = False):
        if orientation == 'ground':
            width, height = sprite.get_rect().size
            screen.blit(sprite, (x, y - height / 2))
        if nametag:
            tag_x = x-Joshumons.HP_width/2 +width/2
            tag_y = y+height/2
            screen.blit(Joshumons.tag_outline, (x - Joshumons.HP_width/2 -1 + width / 2, y + height / 2 - 1))
            screen.blit(Joshumons.tag,(tag_x,tag_y))
            self.nametag.paste((tag_x + self.nametag.size[0]/2 +2,tag_y + self.nametag.size[1]/2),'center')
            self.HP_Bar.paste(tag_x +2,tag_y -Joshumons.HP_height + Joshumons.tag_height- 2)


    def recalc_HP(self, damage):
        self.current_HP -= damage
        if self.current_HP <= 0:
            self.current_HP = 0
            self.fainted = True

class Durple(Joshumons):
    def __init__(self, lvl=1, moves=[]):
        super().__init__(lvl, moves)
        self.type1 = Type.Lean
        self.type2 = Type.Furry
        self.Left_pic = Textures.Durple
        self.Right_pic = pygame.transform.flip(self.Left_pic, True, False)
        self.width, self.height = self.Right_pic.get_rect().size
        self.size_ratio = self.height / self.width
        self.base_HP = 50
        self.base_Defense = 50
        self.base_Attack = 80
        self.base_Speed = 120
        self.calc_stats()
        self.current_HP = self.HP
        self.name = 'Durple'
        self.HP_Bar = Interactives.hpBar(self, (Joshumons.HP_width,Joshumons.HP_height))
        self.nametag = Text.Text(nametag_font,(self.name + '  lvl '+str(self.lvl)),(0,0,0))


class The_Coon(Joshumons):
    def __init__(self, lvl=1, moves=[]):
        super().__init__(lvl, moves)
        self.type1 = Type.Racism
        self.type2 = Type.Virgin
        self.Left_pic = Textures.Coon
        self.Right_pic = pygame.transform.flip(self.Left_pic, True, False)
        self.width, self.height = self.Right_pic.get_rect().size
        self.size_ratio = self.height / self.width
        self.base_HP = 150
        self.base_Defense = 50
        self.base_Attack = 120
        self.base_Speed = 30
        self.calc_stats()
        self.current_HP = self.HP
        self.name = 'The Coon'
        self.HP_Bar = Interactives.hpBar(self, (Joshumons.HP_width,Joshumons.HP_height))
        self.nametag = Text.Text(nametag_font,(self.name + '  lvl '+str(self.lvl)),(0,0,0))


class Muscle_Man(Joshumons):
    def __init__(self, lvl=1, moves=[]):
        super().__init__(lvl, moves)
        self.type1 = Type.Gainz
        self.type2 = Type.Lean
        self.Left_pic = Textures.MuscleMan
        self.Right_pic = pygame.transform.flip(self.Left_pic, True, False)
        self.width, self.height = self.Right_pic.get_rect().size
        self.size_ratio = self.height / self.width
        self.base_HP = 100
        self.base_Defense = 50
        self.base_Attack = 150
        self.base_Speed = 50
        self.calc_stats()
        self.current_HP = self.HP
        self.name = 'Muscle Man'
        self.HP_Bar = Interactives.hpBar(self, (Joshumons.HP_width,Joshumons.HP_height))
        self.nametag = Text.Text(nametag_font,(self.name + '  lvl '+str(self.lvl)),(0,0,0))

class Hamburger_Helper(Joshumons):
    def __init__(self, lvl=1, moves=[]):
        super().__init__(lvl, moves)
        self.type1 = Type.Gay
        self.type2 = None
        self.Left_pic = Textures.HamHelp
        self.Right_pic = pygame.transform.flip(self.Left_pic, True, False)
        self.width, self.height = self.Right_pic.get_rect().size
        self.size_ratio = self.height / self.width
        self.base_HP = 100
        self.base_Defense = 50
        self.base_Attack = 150
        self.base_Speed = 50
        self.calc_stats()
        self.current_HP = self.HP
        self.name = 'Muscle Man'
        self.HP_Bar = Interactives.hpBar(self, (Joshumons.HP_width,Joshumons.HP_height))
        self.nametag = Text.Text(nametag_font,(self.name + '  lvl '+str(self.lvl)),(0,0,0))
