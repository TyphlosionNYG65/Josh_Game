import Button
import Text
import Textures
import game_clock
import sys
from Start_Zombie import update, spawner
from screen_parameters import *


def Start():
    """
    Runs start screen
    """
    running = True
    mouse_state = False
    mode_selection = None
    pygame.mixer.music.load('Lost in Paradise.mp3')
    pygame.mixer.music.play(1, 0, 2000)
    # Create Fonts
    minor_font = pygame.font.SysFont('Bahnschrift', font_scale(30))

    # Create zombies
    zombies = []
    # Create Buttons
    buttons = []
    previous = []

    start_text = Text.Text(minor_font, 'Start', (50, 50, 50))
    start_button = Button.textButton(start_text, (screen_w(.5), screen_h(.69420)))
    buttons.append(start_button)

    exit_text = Text.Text(minor_font, 'Exit', (50, 50, 50))
    exit_button = Button.textButton(exit_text, (screen_w(.5), screen_h(.75)))
    buttons.append(exit_button)

    select_text = Text.Text(minor_font, 'Select Mode', (50, 50, 50))
    select_button = Button.textButton(select_text, (screen_w(.5), screen_h(.69420)))

    back_text = Text.Text(minor_font, 'Back', (50, 50, 50))
    back_button = Button.textButton(back_text, (screen_w(.5), screen_h(.75)))

    battle_simulator_text = Text.Text(minor_font, 'Battle Simulator', (50, 50, 50))
    battle_simulator_button = Button.textButton(battle_simulator_text, (screen_w(.5), screen_h(0)))
    modeButtons = [battle_simulator_button]
    mod_dict = {battle_simulator_button: 'battle'}

    start_screen = pygame.transform.smoothscale(Textures.Start_screen, (screen_w(1), screen_h(1)))

    # define functions
    def reorder():
        for i in range(len(buttons)):
            buttons[i].y = screen_h(.6 + i * .06)
            buttons[i].center_y = buttons[i].y - buttons[i].height

    reorder()
    while running:
        screen.fill((0, 240, 240))
        screen.blit(start_screen, (0, 0))

        zombies.append(spawner(zombies))
        if zombies[-1] == None:
            zombies = zombies[:-1]
        update(zombies)
        start_title = Textures.start_title
        start_title = pygame.transform.scale(start_title, (screen_w(.5), screen_h(.19)))
        screen.blit(start_title, (screen_w(.25), screen_h(.19)))
        Button.paste_buttons(buttons)
        pygame.display.update()
        Button.button_hovers(buttons)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_state = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button in buttons and start_button.is_clicked() and pygame.time.get_ticks() - start_button.last_click >= 200 and not mouse_state:

                    mouse_state = True
                    buttons = [select_button, back_button]
                    reorder()
                if exit_button in buttons and exit_button.is_clicked() and pygame.time.get_ticks() - exit_button.last_click >= 200 and not mouse_state:

                    sys.exit()

                if back_button in buttons and back_button.is_clicked() and pygame.time.get_ticks() - back_button.last_click >= 200 and not mouse_state:
                    mouse_state = True
                    if select_button in buttons:
                        buttons = [start_button, exit_button]
                    else:
                        buttons = [select_button, back_button]
                    reorder()
                if select_button in buttons and select_button.is_clicked() and pygame.time.get_ticks() - select_button.last_click >= 200 and not mouse_state:
                    mouse_state = True
                    buttons = modeButtons
                    buttons.append(back_button)
                    reorder()
                for b in modeButtons:
                    if b in buttons and b.is_clicked() and pygame.time.get_ticks() - b.last_click >= 200 and not mouse_state:
                        running = False
                        mode_selection = mod_dict[b]

        game_clock.clock.tick(FPS)
    pygame.mixer.music.fadeout(200)
    pygame.mixer.music.unload()
    return mode_selection
