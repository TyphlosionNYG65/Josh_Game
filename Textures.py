import os,pygame
def load(Image):
    path = os.path.join(os.getcwd(),'Images',Image)
    return pygame.image.load(path)
Josh_Texture = load('Josh.png')
Start_screen = load('Start screen.jpg')
start_title = load('inkpx-word-art.png')
Durple = load('Durple_Front.png')
Coon = load('The Coon Front.png')
MuscleMan = load('MuscleMan.png')
HamHelp = load('Hamburger Helper.png')
Fight_Background = load('Fight background.jpg')
Fight_Background2 = load('background battle 2.gif')
HP_High = load('HP_High.png')
HP_Low =  load('HP_low.png')
HP_Back = load('HP_Back.png')
HP_Border = load('HP_border.png')

