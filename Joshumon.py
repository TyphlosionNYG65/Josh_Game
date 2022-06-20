import pygame
from gui_elements import Interactives
from gui_elements import Text
from asset_handling import Textures
import Type
import Moves
from screen_parameters import screen_w, screen_h, screen, font_scale

pygame.init()

nametag_font = pygame.font.SysFont('arial', font_scale(20))


class Joshumons:

    def __init__(self, lvl=1, moves=[], right=None, left=None, ):
        # Joshumon class never needs to actually be created, just is used aa a superclass for all Joshumons, therefore variables referenced dont need to be defined in the superclass
        self.lvl = lvl
        self.moves = moves
        self.fainted = False
        self.nametag = None
        self.width = 0
        self.battle_sprite_right = self.scale(type(self).Right_pic, 40000)
        self.battle_sprite_left = self.scale(type(self).Left_pic, 40000)
        self.calc_stats()
        self.current_HP = self.HP
        self.HP_Bar = Interactives.hpBar(self, (Joshumons.HP_width, Joshumons.HP_height))
        self.nametag = Text.Text(nametag_font, (self.name + '  lvl ' + str(self.lvl)), (0, 0, 0))

    # create battle tag for name,type,hp,level,etc
    HP_width = screen_w(196 / 1920)
    HP_height = screen_h(25 / 1080)
    tag_width = screen_w(200 / 1920)
    tag_height = screen_h(50 / 1080)
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
        width = (area / self.size_ratio) ** (1 / 2)

        height = width * self.size_ratio

        width, height = screen_w(width / 1920), screen_h(height / 1080)

        return pygame.transform.smoothscale(sprite, (width, height))

    def paste(self, x, y, orientation, sprite, nametag=False):
        if orientation == 'ground':
            width, height = sprite.get_rect().size
            screen.blit(sprite, (x, y - height / 2))
        if nametag:
            tag_x = x - Joshumons.HP_width / 2 + width / 2
            tag_y = y + height / 2
            screen.blit(Joshumons.tag_outline, (x - Joshumons.HP_width / 2 - 1 + width / 2, y + height / 2 - 1))
            screen.blit(Joshumons.tag, (tag_x, tag_y))
            self.nametag.paste((tag_x + self.nametag.size[0] / 2 + 2, tag_y + self.nametag.size[1] / 2), 'center')
            self.HP_Bar.paste(tag_x + 2, tag_y - Joshumons.HP_height + Joshumons.tag_height - 2)

    def recalc_HP(self, damage):
        self.current_HP -= damage
        if self.current_HP <= 0:
            self.current_HP = 0
            self.fainted = True


class Armin(Joshumons):
    type1 = Type.Nerd
    type2 = Type.Weeb
    name = 'Armin'
    Left_pic = Textures.armin
    Right_pic = pygame.transform.flip(Left_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 50
    base_Defense = 40
    base_Attack = 130
    base_Speed = 120
    moveset = [Moves.pH1, Moves.pH2
    ]


class CatholicPriest(Joshumons):
    type1 = Type.Gay
    type2 = Type.Sex
    name = 'Catholic Priest'
    Left_pic = Textures.Priest
    Right_pic = pygame.transform.flip(Left_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 50
    base_Defense = 40
    base_Attack = 130
    base_Speed = 120
    moveset = [Moves.pH1, Moves.pH2
               ]


class Clamantha(Joshumons):
    type1 = Type.Lean
    type2 = Type.Retard
    name = 'Clamantha'
    Left_pic = Textures.Clamantha
    Right_pic = pygame.transform.flip(Left_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 100
    base_Defense = 90
    base_Attack = 110
    base_Speed = 15
    moveset = [Moves.pH1, Moves.pH2
               ]


class CptFatFuck(Joshumons):
    type1 = Type.Racism
    type2 = Type.Sex
    name = 'Captain. Fat Fuck'
    Left_pic = Textures.FatFuck
    Right_pic = pygame.transform.flip(Left_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 100
    base_Defense = 90
    base_Attack = 110
    base_Speed = 15
    moveset = [Moves.pH1, Moves.pH2
               ]


class Drip(Joshumons):
    type1 = Type.Sex
    type2 = None
    name = 'Drip'
    Left_pic = Textures.Drip
    Right_pic = pygame.transform.flip(Left_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 50
    base_Defense = 40
    base_Attack = 130
    base_Speed = 120
    moveset = [Moves.pH1, Moves.pH2
               ]


class Duck(Joshumons):
    type1 = Type.Furry
    type2 = Type.Sex
    name = 'Duck'
    Right_pic = Textures.Duck
    Left_pic = pygame.transform.flip(Right_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 50
    base_Defense = 40
    base_Attack = 130
    base_Speed = 120
    moveset = [Moves.pH1, Moves.pH2
               ]

class Durple(Joshumons):
    type1 = Type.Lean
    type2 = Type.Furry
    name = 'Durple'
    Right_pic = Textures.Durple
    Left_pic = pygame.transform.flip(Right_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 50
    base_Defense = 50
    base_Attack = 80
    base_Speed = 120
    moveset = [Moves.pH1, Moves.pH2
               ]

class Garfield(Joshumons):
    type1 = Type.Furry
    type2 = None
    name = 'Garfield'
    Left_pic = Textures.Garfield
    Right_pic = pygame.transform.flip(Left_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 100
    base_Defense = 50
    base_Attack = 150
    base_Speed = 50
    moveset = [Moves.pH1, Moves.pH2
               ]

class GayOtter(Joshumons):
    type1 = Type.Gay
    type2 = Type.Furry
    name = 'GayOtter'
    Left_pic = Textures.Otter
    Right_pic = pygame.transform.flip(Left_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 50
    base_Defense = 50
    base_Attack = 80
    base_Speed = 120
    moveset = [Moves.pH1, Moves.pH2
               ]

class Hamburger_Helper(Joshumons):
    type1 = Type.Gay
    type2 = None
    name = 'Hamburger Helper'
    Left_pic = Textures.HamHelp
    Right_pic = pygame.transform.flip(Left_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 100
    base_Defense = 50
    base_Attack = 150
    base_Speed = 50
    moveset = [Moves.pH1, Moves.pH2
               ]

class JeffFisher(Joshumons):
    type1 = Type.Gainz
    type2 = None
    name = 'Jeff Fisher'
    Left_pic = Textures.JeffFisher
    Right_pic = pygame.transform.flip(Left_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 50
    base_Defense = 40
    base_Attack = 130
    base_Speed = 120
    moveset = [Moves.pH1, Moves.pH2
               ]

class JohnDarkSouls(Joshumons):
    type1 = Type.Gamer
    type2 = Type.Gainz
    name = 'John Dark Souls'
    Right_pic = Textures.John
    Left_pic = pygame.transform.flip(Right_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 50
    base_Defense = 40
    base_Attack = 130
    base_Speed = 120
    moveset = [Moves.pH1, Moves.pH2
               ]

class JohnnySins(Joshumons):
    type1 = Type.Sex
    type2 = None
    name = 'Johnny Sins'
    Right_pic = Textures.johnny
    Left_pic = pygame.transform.flip(Right_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 50
    base_Defense = 40
    base_Attack = 130
    base_Speed = 120
    moveset = [Moves.pH1, Moves.pH2
               ]

class KKK(Joshumons):
    type1 = Type.Racism
    type2 = Type.Retard
    name = 'KKK'
    Left_pic = Textures.KKK
    Right_pic = pygame.transform.flip(Left_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 50
    base_Defense = 40
    base_Attack = 130
    base_Speed = 120
    moveset = [Moves.pH1, Moves.pH2
               ]

class Lorax(Joshumons):
    type1 = Type.Furry
    type2 = None
    name = 'Marine Lorax'
    Left_pic = Textures.Lorax
    Right_pic = pygame.transform.flip(Left_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 50
    base_Defense = 40
    base_Attack = 130
    base_Speed = 120
    moveset = [Moves.pH1, Moves.pH2
               ]

class Mort(Joshumons):
    type1 = Type.Gay
    type2 = Type.Virgin
    name = 'Mort'
    Left_pic = Textures.Mort
    Right_pic = pygame.transform.flip(Left_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 50
    base_Defense = 40
    base_Attack = 130
    base_Speed = 120
    moveset = [Moves.pH1, Moves.pH2
               ]

class Muscle_Man(Joshumons):
    type1 = Type.Gainz
    type2 = Type.Lean
    name = 'Muscle Man'
    Left_pic = Textures.MuscleMan
    Right_pic = pygame.transform.flip(Left_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 100
    base_Defense = 50
    base_Attack = 150
    base_Speed = 50
    moveset = [Moves.pH1, Moves.pH2
               ]

class NikoCado(Joshumons):
    type1 = Type.Gay
    type2 = None
    name = 'Nikocado'
    Right_pic = Textures.NikoCado
    Left_pic = pygame.transform.flip(Right_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 50
    base_Defense = 40
    base_Attack = 130
    base_Speed = 120
    moveset = [Moves.pH1, Moves.pH2
               ]

class Schnitzel(Joshumons):
    type1 = Type.Gainz
    type2 = Type.Weeb
    name = 'Schnitzel'
    Left_pic = Textures.Schnitzel
    Right_pic = pygame.transform.flip(Left_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 50
    base_Defense = 40
    base_Attack = 130
    base_Speed = 120
    moveset = [Moves.pH1, Moves.pH2
               ]

class Smokey(Joshumons):
    type1 = Type.Furry
    type2 = Type.Gainz
    name = 'Smokey The Bear'
    Left_pic = Textures.smokey
    Right_pic = pygame.transform.flip(Left_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 50
    base_Defense = 40
    base_Attack = 130
    base_Speed = 120
    moveset = [Moves.pH1, Moves.pH2
               ]

class Strapichu(Joshumons):
    type1 = Type.Gamer
    type2 = Type.Weeb
    name = 'Strapichu'
    Right_pic = Textures.Strapichu
    Left_pic = pygame.transform.flip(Right_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 50
    base_Defense = 40
    base_Attack = 130
    base_Speed = 120
    moveset = [Moves.pH1, Moves.pH2
               ]

class Teddy(Joshumons):
    type1 = Type.Gainz
    type2 = None
    name = 'Teddy Roosovelt'
    Left_pic = Textures.teddy
    Right_pic = pygame.transform.flip(Left_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 150
    base_Defense = 50
    base_Attack = 120
    base_Speed = 30
    moveset = [Moves.pH1, Moves.pH2
               ]

class The_Coon(Joshumons):
    type1 = Type.Racism
    type2 = Type.Virgin
    name = 'The Coon'
    Left_pic = Textures.Coon
    Right_pic = pygame.transform.flip(Left_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 150
    base_Defense = 50
    base_Attack = 120
    base_Speed = 30
    moveset = [Moves.pH1, Moves.pH2
               ]

class Yaoyorozu(Joshumons):
    type1 = Type.Weeb
    type2 = Type.Nerd
    name = 'Yaoyorozu'
    Left_pic = Textures.Yaoyorozu
    Right_pic = pygame.transform.flip(Left_pic, True, False)
    width, height = Right_pic.get_rect().size
    size_ratio = height / width
    base_HP = 150
    base_Defense = 50
    base_Attack = 120
    base_Speed = 30
    moveset = [Moves.pH1, Moves.pH2
               ]
if __name__ == '__main__':
    replist = []
    replist = [[typer] for typer in Type.Types]
    for typer in replist:
        typer.append(0)

    for mon in Joshumons.__subclasses__():
        for typer in replist:
            if typer[0] == mon.type1:
                typer[1] += 1
            elif typer[0] == mon.type2:
                typer[1] += 1

    for typer in replist:
        print(typer[0].name + ': ' + str(type[1]))
