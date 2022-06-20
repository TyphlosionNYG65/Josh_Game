import pygame

import Joshumon
import Trainer
import game_clock
from asset_handling import Textures
from gui_elements import Button, Text
from screen_parameters import screen, font_scale, screen_vals, screen_w, screen_h


def select_screen(background):
    # Define variables
    running = True
    mouse_state = False
    mons_showing = False
    result = None
    current_selecting_button = None
    current_page = 0
    player = Trainer.Player('Josh', [])

    # create fonts
    minor_font = pygame.font.SysFont('Arial', font_scale(30))
    major_font = pygame.font.SysFont('Bahnschrift', font_scale(40))
    gay_font = pygame.font.SysFont('Arial', font_scale(20))

    # create Text
    move_title = Text.Text(major_font, 'Current Moves', (255, 255, 255))
    # create buttons
        # select buttons
    select1 = Button.selectButton(screen_w(360 / 1920), screen_h(800 / 1080),
                                  (screen_w(150 / 1920), screen_h(150 / 1080)), [player, 0], Textures.plus)
    select2 = Button.selectButton(screen_w(560 / 1920), screen_h(800 / 1080),
                                  (screen_w(150 / 1920), screen_h(150 / 1080)), [player, 1], Textures.plus)
    select3 = Button.selectButton(screen_w(760 / 1920), screen_h(800 / 1080),
                                  (screen_w(150 / 1920), screen_h(150 / 1080)), [player, 2], Textures.plus)
    select4 = Button.selectButton(screen_w(960 / 1920), screen_h(800 / 1080),
                                  (screen_w(150 / 1920), screen_h(150 / 1080)), [player, 3], Textures.plus)
    select5 = Button.selectButton(screen_w(1160 / 1920), screen_h(800 / 1080),
                                  (screen_w(150 / 1920), screen_h(150 / 1080)), [player, 4], Textures.plus)
    select6 = Button.selectButton(screen_w(1360 / 1920), screen_h(800 / 1080),
                                  (screen_w(150 / 1920), screen_h(150 / 1080)), [player, 5], Textures.plus)

    select_buttons = [select1, select2, select3, select4, select5, select6]

        # Navigational buttons

    downButton = Button.imageButton(screen_w(1550 / 1920), screen_h(500 / 1080),
                                     (screen_w(40 / 1920), screen_h(40 / 1080)), Textures.down,(0,0,0))
    upButton = Button.imageButton(screen_w(1550 / 1920), screen_h(450 / 1080),
                                   (screen_w(40 / 1920), screen_h(40 / 1080)), Textures.up,(0,0,0))
    back_button_text = Text.Text(minor_font,'BACK',(0,0,0))
    backButton = Button.textButton(back_button_text,(screen_w(1550 / 1920), screen_h(850 / 1080)),True,(200,200,200) )
    navigational = []

    mon_button_width = [600, 310, 1610]
    mon_button_height = [99, 200, 800]
    mon_buttons = [[]]
    move_buttons = [[]]
    mons = Joshumon.Joshumons.__subclasses__()
    length = len(mons)
    button_x = mon_button_width[1]
    button_y = mon_button_height[1]
    page = 0
    for mon in mons:
        mon_buttons[page].append(
            Button.monButton(button_x, button_y, (mon_button_width[0], mon_button_height[0]), minor_font, mon,
                             ))
        button_y += mon_button_height[0] + 1
        if button_y == mon_button_height[2]:
            button_y = mon_button_height[1]
            button_x += mon_button_width[0] + 1
        if button_x >= mon_button_width[2] - 100:
            button_x = mon_button_width[1]
            button_y = mon_button_height[1]
            mon_buttons.append([])
            page += 1

    # initialize textures
    background.scale((screen_vals.width + 100, screen_vals.height + 100))

    # functions
    def create_move_buttons(mon, mon_button_width, mon_button_height):
        temp_page = 0
        '''Creates move buttons for selected mon'''
        move_buttons_temp = [[]]
        button_x = mon_button_width[1]
        button_y = mon_button_height[1]
        for move in mon.moveset:
            move_buttons_temp[temp_page].append(
                Button.moveButton(button_x, button_y, (mon_button_width[0], mon_button_height[0]), minor_font, move,))
            button_y += mon_button_height[0] + 1
            if button_y == mon_button_height[2]:
                button_y = mon_button_height[1]
                button_x += mon_button_width[0] + 1
            if button_x >= mon_button_width[2] - 100:
                button_x = mon_button_width[1]
                button_y = mon_button_height[1]
                move_buttons_temp.append([])
                temp_page += 1
        return move_buttons_temp

    while running:
        # Handle what is shown on screen
        screen.fill((0, 240, 240))
        background.paste((-100, -100))
        Button.paste_buttons(select_buttons)
        Button.paste_buttons(navigational)
        if mons_showing:
            Button.paste_buttons(mon_buttons[current_page])
        elif current_selecting_button is not None and current_selecting_button.moves_showing:
            Button.paste_buttons(move_buttons[current_page])
            if backButton not in navigational:
                navigational.append(backButton)
        if current_selecting_button is not None and current_selecting_button.mon is not None:
            move_title.paste((1700, 300), 'center')
            Button.paste_buttons(current_selecting_button.mon_moves)
        pygame.display.update()

        # Handle Button hovering
        if mons_showing:
            Button.button_hovers(mon_buttons[current_page])
        elif current_selecting_button is not None and current_selecting_button.moves_showing:
            Button.button_hovers(move_buttons[current_page])
        Button.button_hovers(select_buttons)
        Button.button_hovers(navigational)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_state = False

            # Handle button actions
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in select_buttons:
                    if button.is_clicked() and pygame.time.get_ticks() - button.last_click >= 200 and not mouse_state:
                        # A select button is pressed
                        mouse_state = True
                        if current_selecting_button is not None:
                            """
                            If a selecting button is currently in use resets that button
                            """
                            current_selecting_button.moves_showing = False
                            current_selecting_button.outline_color = (0, 0, 0)

                        if current_selecting_button == button:
                            """
                            If the button pressed is the button currently in use then the button
                            resets so there is no selecting button
                            """
                            current_selecting_button = None
                            mons_showing = False

                        else:
                            """
                            Sets the new current selecting button
                            """
                            button.outline_color = (255, 255, 255)
                            current_selecting_button = button
                            if button.mon is not None:
                                """
                                If the button already has a selected Joshumon it goes straigt to move selection
                                """
                                mons_showing = False
                                button.moves_showing = True
                                navigational = [downButton, backButton]
                            else:
                                """
                                If no Joshumon has been selected for the button yet then it goes to Joshumon selection screen
                                """
                                mons_showing = True
                                navigational = [downButton]
                        current_page = 0
                        break
                # downButton is pressed
                if downButton in navigational and downButton.is_clicked() and pygame.time.get_ticks() - downButton.last_click >= 200 and not mouse_state:
                    mouse_state = True
                    if current_page < len(mon_buttons) - 2:
                        current_page += 1
                        if current_page == len(mon_buttons) - 2:
                            navigational.remove(downButton)
                        if upButton not in navigational:
                            navigational.append(upButton)

                # upButton is pressed
                if upButton in navigational and upButton.is_clicked() and pygame.time.get_ticks() - upButton.last_click >= 200 and not mouse_state:
                    mouse_state = True
                    if current_page > 0:
                        current_page -= 1
                        if current_page == 0:
                            navigational.remove(upButton)
                        if downButton not in navigational:
                            navigational.append(downButton)

                # backButton is pressed
                if backButton in navigational and backButton.is_clicked() and pygame.time.get_ticks() - backButton.last_click >= 200 and not mouse_state:
                    mouse_state = True
                    if current_selecting_button.moves_showing:
                        """
                        If backButton is pressed while on move selection it goes back to Joshumon selection
                        """
                        current_selecting_button.moves_showing = False
                        mons_showing = True
                        current_page = 0
                        navigational.remove(backButton)
                    # Joshumon Selection Showing
                if mons_showing:
                    for button in mon_buttons[current_page]:
                        if button.is_clicked() and pygame.time.get_ticks() - button.last_click >= 200 and not mouse_state:
                            current_selecting_button.change_image(button.mon)
                            current_page = 0
                            current_selecting_button.moves_showing = True
                            mons_showing = False
                            move_buttons = create_move_buttons(current_selecting_button.mon, mon_button_width,mon_button_height)
                            mouse_state = True
                            break
                # Move Selection Showing
                if current_selecting_button is not None and current_selecting_button.moves_showing:
                    for button in move_buttons[current_page]:
                        if button.is_clicked() and pygame.time.get_ticks() - button.last_click >= 200 and not mouse_state:
                            if current_selecting_button.add_move(button.move):
                                current_selecting_button.mon_moves.append(
                                    Button.moveButton(1600, 325 + len(current_selecting_button.mon_moves) * 75,(150, 75), gay_font, button.move))
                            current_page = 0
                            mouse_state = True
                            break

        game_clock.clock.tick(game_clock.FPS)
    return result
