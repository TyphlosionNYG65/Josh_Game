import os,pygame
def load(Image):
    path = os.path.join(os.getcwd(),'Images',Image)
    return pygame.image.load(path)
Josh_Texture = load('Josh.png')
Start_screen = load('Start screen.jpg')
start_title = load('inkpx-word-art.png')
Durple_Front = load('Durple_Front.png')
Durple_Back = load('Durple_Back.png')
Coon_Front = load('The Coon Front.png')
Coon_Back = load('The Coon Back.png')
Fight_Background = load('Fight background.jpg')
HP_High = load('HP_High.png')
HP_Low =  load('HP_low.png')
HP_Back = load('HP_Back.png')
HP_Border = load('HP_border.png')
print(HP_High)

