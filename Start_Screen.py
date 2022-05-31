import pygame,Text,Button,Textures,sys,game_clock,Joshumon,random
from screen_parameters import *
from Start_Zombie import update,spawner
def Start():
    """
    Runs start screen
    """
    running = True
    pygame.mixer.music.load('Lost in Paradise.mp3')
    pygame.mixer.music.play(1,0,2000)
    # Create Fonts
    minor_font = pygame.font.SysFont('Bahnschrift', font_scale(30))

    # Create zombies
    zombies = []
    # Create Buttons
    buttons = []
    exit_text = Text.Text(minor_font, 'Exit',  (50, 50, 50))
    exit_button = Button.textButton(exit_text,(screen_w(.5),  screen_h(.75)))
    buttons.append(exit_button)

    start_text = Text.Text(minor_font, 'Start', (50, 50, 50))
    start_button = Button.textButton(start_text,(screen_w(.5), screen_h(.69420)))
    buttons.append(start_button)
    start_screen = pygame.transform.smoothscale(Textures.Start_screen, (screen_w(1), screen_h(1)))
    while running:
        screen.fill((0, 240, 240))
        screen.blit(start_screen, (0, 0))

        zombies.append(spawner(zombies))
        if zombies[-1] == None:
            zombies = zombies[:-1]
        update(zombies)
        start_title = Textures.start_title
        start_title = pygame.transform.scale(start_title,(screen_w(.5),screen_h(.19)))
        screen.blit(start_title,(screen_w(.25),screen_h(.19)))
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

        game_clock.clock.tick(FPS)
    pygame.mixer.music.fadeout(200)
    pygame.mixer.music.unload()
