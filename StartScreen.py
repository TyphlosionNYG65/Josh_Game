import pygame
import Textures
from screen_parameters import screen, screen_vals
import Text
import Button
from game_clock import clock, FPS
import sys


def Start():
    """
    Runs start screen
    """
    running = True
    # Create Fonts
    title_font = pygame.font.SysFont('Comic Sans MS', 40)
    minor_font = pygame.font.SysFont('Comic Sans MS', 30)

    # Create Static Text
    title_text = Text.Text(title_font, 'Untitled Josh Pinsky Themed Pokemon Ripoff', (screen_vals.width / 2, 200),
                           (50, 50, 50), 'center')

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
        mouse = pygame.mouse.get_pos()
        mouse = title_font.render(str(mouse), False, (0, 0, 0))
        start_screen = pygame.transform.scale(pygame.image.load(Textures.Start_screen),(screen_vals.width, screen_vals.height))
        screen.blit(start_screen, (0, 0))
        screen.blit(mouse, (0, 0))
        screen.blit(title_text.render, title_text.position)
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
