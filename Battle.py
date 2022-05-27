import Button
import Interactives
import Text
import Textures
import Trainer
import pygame
from screen_parameters import screen, screen_vals, screen_w, screen_h

attack_font = pygame.font.SysFont('Bahnschrift', 30)
attack = Button.rectangleButton(screen_w(.8), screen_h(.8), (200, 100), (255, 0, 0), 'Attack', attack_font,
                                ((0, 0, 0), 2))


def Battle(User, Opponent):
    """
    :param User: User Trainer controlled by Player
    :param Opponent: Opponent Trainer controlled by AI
    :return: None
    """
    global running
    assert type(User) == Trainer.Player

    move_responses = {
                    'Supereffective': 'Nice move, king',
                    'Noteffective' : 'Kinda lame move bro',
                    'None' : 'That move was shit and you should feel bad'
    }
    def user_move(move):
        somethin.text.append(User.current_mon.name + ' ' + move.text + ' ' + Opponent.current_mon.name)
        somethin.render_text()
        somethin.paste_textBox()
        pygame.display.update()
        pygame.time.delay(somethin.delay)
        damage, variant = User.current_mon.attack(Opponent.current_mon,move)
        Opponent.current_mon.recalc_HP(damage)
        Opp_HP.calc_Bar()
        showHP()
        if variant != None:
            somethin.text.append(move_responses[variant])
            somethin.render_text()
            somethin.paste_textBox()
        pygame.display.update()
        pygame.time.delay(somethin.delay)


    def opp_move(move):
        somethin.text.append(Opponent.current_mon.name + ' ' + move.text + ' ' + User.current_mon.name)
        somethin.render_text()
        somethin.paste_textBox()
        pygame.display.update()
        damage, variant = Opponent.current_mon.attack(User.current_mon, move)
        User.current_mon.recalc_HP(damage)
        User_HP.calc_Bar()
        showHP()
        pygame.time.delay(somethin.delay)
        if variant != None:
            somethin.text.append(move_responses[variant])
            somethin.render_text()
            somethin.paste_textBox()

        pygame.display.update()
        pygame.time.delay(somethin.delay)



    def faintCheck(playerCheck):
        if playerCheck:
            if User.current_mon.fainted == True:
                User.start_battle()
                return True
        else:
            if Opponent.current_mon.fainted == True:
                Opponent.start_battle()
                return True

    def showHP():
        User_HP.calc_Bar()
        Opp_HP.calc_Bar()
        User_HP.paste()
        Opp_HP.paste()


    def battleEnd(Winner):
        global running
        winBox = Text.textBox((500, 500), 600, 1, win_font,3000)
        winBox.text.append( Winner.name + ' Wins!')
        winBox.render_text()
        winBox.paste_textBox()
        pygame.display.update()
        pygame.time.delay(4000)
        running = False



    # Initial variables
    mouse_state = False  # Controller for whether mouse as been clicked
    running = True  # While True battle is running
    turn = False
    turn_start = False
    user_move_selection = None
    buttons = []

    # Initialize Trainers
    User.start_battle()  # Initializes Player
    Opponent.start_battle()  # Initializes AI

    # Initialize textures
    fight_background = pygame.transform.scale(Textures.Fight_Background, (screen_vals.width, screen_vals.height))
    User_HP = Interactives.hpBar((400, 950), (200, 25))
    User_HP.new_joshumon(User.current_mon)
    Opp_HP = Interactives.hpBar((1100, 700), (200, 25))
    Opp_HP.new_joshumon(Opponent.current_mon)

    # Create Fonts
    attack_font = pygame.font.SysFont('Bahnschrift', 30)
    text_font = pygame.font.SysFont('arial', 15)
    win_font = pygame.font.SysFont('Bahnschrift', 30)

    # Create text boxes
    somethin = Text.textBox((500, 500), 200, 2, text_font,1100)

    # Create buttons
    moves = Button.create_move_buttons(User.current_mon.moveset, attack_font)
    attack = Button.rectangleButton(screen_w(.8), screen_h(.8), (200, 100), (255, 0, 0), 'Attack', attack_font,
                                    ((0, 0, 0), 2))
    while running:
        # Create Background
        screen.fill((0, 240, 240))
        screen.blit(fight_background, (0, 0))
        showHP()

        # Paste Sprites
        if User.current_mon != None:
            screen.blit(User.current_mon.user_sprite, (450, 600))
        if Opponent.current_mon != None:
            screen.blit(Opponent.current_mon.opp_sprite, (1100, 450))

        # Paste Text Box
        somethin.paste_textBox()

        # Paste Buttons
        Button.paste_buttons(buttons)
        Button.button_hovers(buttons)

        # Update Screen
        pygame.display.update()

        # Control Turn
        if turn_start == False:
            buttons.append(attack)
            turn_start = True

        if turn == True:
            if User.current_mon.SD >= Opponent.current_mon.SD:
                user_move(user_move_selection)
                if faintCheck(False):
                    if Opponent.current_mon == None:
                        battleEnd(User)
                    continue
                pygame.time.delay(500)
                pygame.display.update()

                opp_move(Opponent.AI_Move())
                if faintCheck(True):
                    if User.current_mon == None:
                        battleEnd(Opponent)

                    continue

            else:
                opp_move(Opponent.AI_Move())
                if faintCheck(True):
                    if User.current_mon == None:
                        battleEnd(Opponent)
                    continue
                pygame.time.delay(500)
                pygame.display.update()
                user_move(user_move_selection)
                if faintCheck(False):
                    if Opponent.current_mon == None:
                        battleEnd(User)

                    continue
            turn = False
            turn_start= False

        # User Actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_state = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if attack in buttons and attack.is_clicked() and pygame.time.get_ticks() - attack.last_click >= 200 and mouse_state == False:
                    buttons = []
                    buttons += moves
                    attack.last_click = pygame.time.get_ticks()
                    mouse_state = True
                for x in moves:
                    if x in buttons and x.is_clicked() and pygame.time.get_ticks() - x.last_click >= 200 and mouse_state == False:
                        buttons = []
                        user_move_selection = x.move
                        turn = True
                        attack.last_click = pygame.time.get_ticks()
                        mouse_state = True
