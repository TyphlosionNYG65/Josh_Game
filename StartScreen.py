import pygame, Textures, Button, sys, random, Text
from Start_Zombie import Start_Zombie
from screen_parameters import screen, screen_vals
from game_clock import clock, FPS

def spawner(Zombies):
    spawn = random.choices([True,False], weights = (.005,.99))
    if spawn[0] == True:
        side = random.randrange(0,2)
        speed = random.randrange(100,300)
        height = random.randrange(50,screen_vals.height-50)
        image= random.choices([Textures.Josh_Texture])[0]
        if side == 0:
            return Start_Zombie(-30,height,image,43,64,(speed,0),'left')
        elif side == 1:
            return Start_Zombie(screen_vals.width+30,height,image,43,64,(-1*speed,0),'right')

def update(zombies):
    if zombies == []:
        return
    for i in zombies:
        if i == None:
            return
        i.update_position()
        if i.out_of_screen():
            zombies.remove(i)
        screen.blit(i.pic,(i.x,i.y))



def Start():
    """
    Runs start screen
    """
    running = True
    # Create Fonts
    title_font = pygame.font.SysFont('Comic Sans MS', 40)
    minor_font = pygame.font.SysFont('Comic Sans MS', 30)

    # Create zombies
    zombies = []
    # Create Buttons
    buttons = []
    exit_text = Text.Text(minor_font, 'Exit', (screen_vals.width / 2, 800), (50, 50, 50), 'center')
    exit_button = Button.textButton(exit_text)
    buttons.append(exit_button)

    start_text = Text.Text(minor_font, 'Start', (screen_vals.width / 2, 750), (50, 50, 50), 'center')
    start_button = Button.textButton(start_text)
    buttons.append(start_button)

    while running:
        screen.fill((0, 240, 240))
        start_screen = pygame.transform.scale(Textures.Start_screen,(screen_vals.width, screen_vals.height))
        screen.blit(start_screen, (0, 0))
        screen.blit(pygame.transform.scale(Textures.Durple_Front,(58,85)),(1200,800))
        screen.blit(pygame.transform.scale(Textures.Coon_Front, (65, 50)), (1300, 800))
        zombies.append(spawner(zombies))
        if zombies[-1] == None:
            zombies = zombies[:-1]
        update(zombies)
        start_title = Textures.start_title
        start_title = pygame.transform.scale(start_title,(screen_vals.width/2,200))
        screen.blit(start_title,(screen_vals.width/4,200))
        Button.paste_buttons(buttons)
        pygame.display.update()
        Button.button_hovers(buttons)
        if exit_button.is_clicked():
            sys.exit()
            
        if start_button.is_clicked():
            running = False

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    running = False
        clock.tick(FPS)
