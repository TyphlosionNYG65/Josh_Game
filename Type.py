import pygame
import screen_parameters


class Gay:
    name = 'Gay'
    multipliers = {'Racism': 2,
                   'Lean': 1,
                   'Gay': 1,
                   'Weeb': 1,
                   'Gainz': 1,
                   'Sex': .5,
                   'Gamer': 2,
                   'Furry': 2,
                   'Virgin': 1,
                   'Retard': 2,
                   'Nerd': 1}
    color = (255, 192, 203)  # Trans pink
    alt_color = (255, 255, 255)
    Indicator = pygame.Surface((screen_parameters.screen_w(20 / 1920), screen_parameters.screen_h(10 / 1080)))
    Indicator.fill(color)


class Lean:
    name = 'Lean'
    multipliers = {'Racism': 1,
                   'Lean': .5,
                   'Gay': 1,
                   'Weeb': .5,
                   'Gainz': 2,
                   'Sex': 2,
                   'Gamer': .5,
                   'Furry': 2,
                   'Virgin': .5,
                   'Retard': .5,
                   'Nerd': 2}
    color = (138, 43, 226)  # purple
    alt_color = (255, 255, 255)
    Indicator = pygame.Surface((screen_parameters.screen_w(20 / 1920), screen_parameters.screen_h(10 / 1080)))
    Indicator.fill(color)


class Racism:
    name = 'Racism'
    multipliers = {'Racism': .5,
                   'Lean': 1,
                   'Gay': .5,
                   'Weeb': 2,
                   'Gainz': .5,
                   'Sex': .5,
                   'Gamer': 2,
                   'Furry': .5,
                   'Virgin': 1,
                   'Retard': .5,
                   'Nerd': .5}
    color = (0, 0, 0)  # White
    alt_color = (255, 255, 255)
    Indicator = pygame.Surface((screen_parameters.screen_w(20 / 1920), screen_parameters.screen_h(10 / 1080)))
    Indicator.fill(color)


class Weeb:
    name = 'Weeb'
    multipliers = {'Racism': .5,
                   'Lean': 1,
                   'Gay': .5,
                   'Weeb': 1,
                   'Gainz': 2,
                   'Sex': 0,
                   'Gamer': 1,
                   'Furry': 1,
                   'Virgin': 2,
                   'Retard': 1,
                   'Nerd': .5}
    color = (135, 206, 235)  # Super Saiyan Blue
    alt_color = (255, 255, 255)
    Indicator = pygame.Surface((screen_parameters.screen_w(20 / 1920), screen_parameters.screen_h(10 / 1080)))
    Indicator.fill(color)


class Gainz:
    name = 'Gainz'
    multipliers = {'Racism': 2,
                   'Lean': 2,
                   'Gay': 1,
                   'Weeb': .5,
                   'Gainz': .5,
                   'Sex': 1,
                   'Gamer': .5,
                   'Furry': .5,
                   'Virgin': 0,
                   'Retard': 1,
                   'Nerd': 2}
    color = (192, 192, 192)  # Silver
    alt_color = (255, 255, 255)
    Indicator = pygame.Surface((screen_parameters.screen_w(20 / 1920), screen_parameters.screen_h(10 / 1080)))
    Indicator.fill(color)


class Sex:
    name = 'Sex'
    multipliers = {'Racism': .5,
                   'Lean': .5,
                   'Gay': 1,
                   'Weeb': 2,
                   'Gainz': 2,
                   'Sex': 1,
                   'Gamer': .5,
                   'Furry': 2,
                   'Virgin': 0,
                   'Retard': .5,
                   'Nerd': .5}
    color = (144, 44, 62)  # Velvet
    alt_color = (255, 255, 255)
    Indicator = pygame.Surface((screen_parameters.screen_w(20 / 1920), screen_parameters.screen_h(10 / 1080)))
    Indicator.fill(color)


class Gamer:
    name = 'Gamer'
    multipliers = {'Racism': 1,
                   'Lean': 2,
                   'Gay': .5,
                   'Weeb': .5,
                   'Gainz': 2,
                   'Sex': 0,
                   'Gamer': 1,
                   'Furry': 1,
                   'Virgin': 2,
                   'Retard': 1,
                   'Nerd': 2}
    color = (30, 144, 255)  # Piss Yellow
    alt_color = (225, 225, 20)
    Indicator = pygame.Surface((screen_parameters.screen_w(20 / 1920), screen_parameters.screen_h(10 / 1080)))
    Indicator.fill(color)


class Furry:
    name = 'Furry'
    multipliers = {'Racism': 2,
                   'Lean': 1,
                   'Gay': 1,
                   'Weeb': 2,
                   'Gainz': 1,
                   'Sex': .5,
                   'Gamer': 2,
                   'Furry': 1,
                   'Virgin': 1,
                   'Retard': 2,
                   'Nerd': 1}
    color = (139, 69, 19)  # Brown
    alt_color = (255, 255, 255)
    Indicator = pygame.Surface((screen_parameters.screen_w(20 / 1920), screen_parameters.screen_h(10 / 1080)))
    Indicator.fill(color)


class Virgin:
    name = 'Virgin'
    multipliers = {'Racism': 1,
                   'Lean': 2,
                   'Gay': 2,
                   'Weeb': .5,
                   'Gainz': .5,
                   'Sex': 2,
                   'Gamer': .5,
                   'Furry': 1,
                   'Virgin': 1,
                   'Retard': 2,
                   'Nerd': 1}
    color = (34, 139, 34)
    alt_color = (255, 255, 255)
    Indicator = pygame.Surface((screen_parameters.screen_w(20 / 1920), screen_parameters.screen_h(10 / 1080)))
    Indicator.fill(color)


class Retard:
    name = 'Retard'
    multipliers = {'Racism': 1,
                   'Lean': .5,
                   'Gay': 1,
                   'Weeb': 1,
                   'Gainz': .5,
                   'Sex': 2,
                   'Gamer': 1,
                   'Furry': .5,
                   'Virgin': .5,
                   'Retard': 1,
                   'Nerd': 2}
    color = (255, 140, 0)  # Orange
    alt_color = (255, 255, 255)
    Indicator = pygame.Surface((screen_parameters.screen_w(20 / 1920), screen_parameters.screen_h(10 / 1080)))
    Indicator.fill(color)


class Nerd:
    name = 'Nerd'
    multipliers = {'Racism': 1,
                   'Lean': .5,
                   'Gay': 1,
                   'Weeb': 1,
                   'Gainz': 2,
                   'Sex': 2,
                   'Gamer': .5,
                   'Furry': 1,
                   'Virgin': .5,
                   'Retard': 2,
                   'Nerd': 1}
    color = (32, 42, 68)  # Navy Blue
    alt_color = (255, 255, 255)
    Indicator = pygame.Surface((screen_parameters.screen_w(20 / 1920), screen_parameters.screen_h(10 / 1080)))
    Indicator.fill(color)


def paste_indicator(type, position):
    screen_parameters.screen.blit(type.Indicator, position)


Types = [Gay, Lean, Racism, Weeb, Gainz, Sex, Gamer, Furry, Virgin, Retard, Nerd]
print(Types)
