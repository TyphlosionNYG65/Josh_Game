import pygame

import Button
import Text
import Textures
import Trainer
import game_clock
from screen_parameters import screen, screen_vals, screen_w, screen_h, font_scale


def Battle(User, Opponent):
    """
    :param User: User Trainer controlled by Player
    :param Opponent: Opponent Trainer controlled by AI
    :return: None
     # runs battles
    """
    global running
    assert type(User) == Trainer.Player

    # Initialize Trainers
    User.start_battle()  # Initializes Player
    Opponent.start_battle()  # Initializes AI

    # Initialize textures
    fight_background = Textures.Fight_Background1 # variable for animated fight background
    fight_background.scale((screen_vals.width, screen_vals.height)) # scale background to screen

    # Initial variables
    mouse_state = False  # Controller for whether mouse as been clicked
    running = True  # While True battle is running
    buttons = [] # list containing all on-screen buttons
    current_user_mon = User.current_mon

    # Create Fonts
    attack_font = pygame.font.SysFont('Bahnschrift', font_scale(18))
    swap_font = pygame.font.SysFont('Bahnschrift', font_scale(15))
    text_font = pygame.font.SysFont('arial', font_scale(15))
    win_font = pygame.font.SysFont('Bahnschrift', font_scale(30))

    # Create text boxes
    somethin = Text.textBox((screen_w(850 / 1920), screen_h(1000 / 1080)), screen_w(200 / 1920), 2, text_font, 1000)

    # Create buttons
    attack = Button.rectangleButton(screen_w(.8), screen_h(.8), (screen_w(100 / 1920), screen_h(50 / 1080)),
                                    (255, 0, 0), 'Attack', attack_font,
                                    ((0, 0, 0), 2))
    swap = Button.rectangleButton(screen_w(.86), screen_h(.8), (screen_w(150 / 1920), screen_h(50 / 1080)), (0, 255, 0),
                                  'Swap Joshumon', attack_font,
                                  ((0, 0, 0), 2))
    size = User.current_mon.battle_sprite_right.get_size()
    moves = Button.create_move_buttons(User.current_mon.moveset, attack_font,
                                       850 + size[0])
    monButtons = Button.create_mon_buttons(
        [Joshumon for Joshumon in User.Joshumons if Joshumon != User.current_mon and Joshumon.fainted == False],
        attack_font)
    back = Button.rectangleButton(screen_w(.8), screen_h(.8), (screen_w(100 / 1920), screen_h(50 / 1080)),
                                  (255, 0, 0), 'Back', attack_font,
                                  ((0, 0, 0), 2))

    class turn:
        def __init__(self, User, Opponent, textbox):
            # preTurn   start of a turn
            #         turnStart   Choosing action for next turn
            #        firstMove    Start first trainers action is happening
            #       firstMove
            #      lastMoveStart second trainers action is happening
            #     lastMove
            #    turn end   end of turn
            self.first = None  # Trainer moving first in turn
            self.last = None  # Trainer moving second in turn
            self.phase = 'preTurn'
            self.User = User
            self.Opponent = Opponent
            self.textbox = textbox
            self.fainted = []
            self.mon_select = False

        def activePhase(self, buttons, turn_list, attack):
            """
            :param buttons: Edits the button list depending on input and phase
            :param turn_list: Uses most recent turn in list
            :param attack: alters attack button use
            :return:
            """
            move_responses = { # response dictionary dependent on effectiveness of move
                'Supereffective': 'Nice move, king',
                'Noteffective': 'Kinda lame move bro',
                'None': 'That move was shit and you should feel bad'
            }
            if self.mon_select: # Currently in selection for new mon. Skips turn phgases
                return

            if self.phase == 'preTurn':# Move selection at beginning of turn
                buttons += [attack, swap]
                self.phase = 'None'
                return

            elif self.phase == 'turnStart': # Determines action priority for turn
                if self.User.current_mon.SD >= self.Opponent.current_mon.SD:
                    self.first = self.User

                    self.last = self.Opponent
                else:
                    self.first = self.Opponent

                    self.last = self.User

                self.phase = 'firstMoveStart'
                return

            elif self.phase == 'firstMoveStart': # Calculates action for first prioirty action
                if self.first.action[0] == 'attack':
                    self.textbox.text.append(
                        self.first.current_mon.name + ' ' + self.first.action[
                            1].text + ' ' + self.last.current_mon.name)
                    damage, variant = self.first.current_mon.attack(self.last.current_mon, self.first.action[1])
                    if variant != None:
                        self.textbox.text.append(move_responses[variant])
                    self.last.current_mon.recalc_HP(damage)
                    self.last.current_mon.HP_Bar.change()
                    self.fainted = self.faintCheck()
                    if self.fainted != []:
                        for trainer in self.fainted:
                            self.textbox.text.append(trainer.current_mon.name + ' fainted!')
                    self.textbox.render_text()
                    self.phase = 'firstMove'
                    return
                elif self.first.action[0] == 'swap':

                    self.textbox.text.append(self.first.current_mon.name + ', come back you worthless piece of shit!')
                    self.textbox.render_text()
                    self.phase = 'firstMove'
                    return

            elif self.phase == 'firstMove': # Waits for end of animations for first priority action
                if self.continueCheck():
                    if self.first.action[0] == 'attack':
                        if self.fainted != []:
                            self.phase = 'turnEnd'
                            return
                    elif self.first.action[0] == 'swap':
                        self.first.current_mon = self.first.action[1]
                        self.textbox.text.append(self.first.current_mon.name + ', do somnething!')
                        self.textbox.render_text()
                    self.phase = 'lastMoveStart'
                    return
                return

            elif self.phase == 'lastMoveStart': # calculates actions for last priority action
                if self.continueCheck():
                    if self.last.action[0] == 'attack':
                        self.textbox.text.append(
                            self.last.current_mon.name + ' ' + self.last.action[
                                1].text + ' ' + self.first.current_mon.name)
                        damage, variant = self.last.current_mon.attack(self.first.current_mon, self.last.action[1])
                        if variant != None:
                            self.textbox.text.append(move_responses[variant])
                        self.textbox.render_text()
                        self.first.current_mon.recalc_HP(damage)
                        self.first.current_mon.HP_Bar.change()
                        self.phase = 'lastMove'
                        self.fainted = self.faintCheck()
                        if self.fainted != []:
                            for trainer in self.fainted:
                                self.textbox.text.append(trainer.current_mon.name + ' fainted!')
                        self.textbox.render_text()
                        return
                    elif self.last.action[0] == 'swap':
                        self.textbox.text.append(
                            self.first.current_mon.name + ', come back you worthless piece of shit!')
                        self.phase = 'firstMove'
                        return

            elif self.phase == 'lastMove': # Waits for animations for last priority action
                if self.continueCheck():
                    if self.last.action[0] == 'attack':
                        if self.fainted != []:
                            self.phase = 'turnEnd'
                            return
                    elif self.last.action[0] == 'swap':
                        self.last.current_mon = self.last.action[1]
                        self.textbox.text.append(self.first.current_mon.name + ', do somnething!')
                        self.textbox.render_text()

                    self.phase = 'turnEnd'
                return

            elif self.phase == 'turnEnd':
                if self.continueCheck():
                    if self.fainted != []:
                        for trainer in self.fainted:
                            trainer.current_mon = None
                            if not trainer.check_mons():
                                self.phase = 'battleOver'
                                return
                            else:
                                trainer.start_battle()

                    turn_list.append(turn(self.User, self.Opponent, self.textbox))
                    return

                return

            elif self.phase == 'battleOver':
                if self.textbox.text_lines == []:
                    if self.first.current_mon == None:
                        battleEnd(self.last)
                    elif self.last.current_mon == None:
                        battleEnd(self.first)

        def faintCheck(self): # Checks if either mon is fainted and returns True if that is the case
            fainted = []
            if self.User.current_mon.fainted:
                fainted += [User]
            if self.Opponent.current_mon.fainted:
                fainted += [Opponent]
            return fainted

        def continueCheck(self):
            """
            Checks if all animations have ceased in order to proceed forward in turn
            :return:
            """
            if self.textbox.text_lines == [] and self.first.current_mon.HP_Bar.motion == False and self.last.current_mon.HP_Bar.motion == False:
                return True
            return False

    def battleEnd(Winner):
        """
        :param Winner:
        :return:
        Ends battle and declares winner
        """
        global running
        winBox = Text.textBox((screen_w(500 / 1920), screen_h(500 / 1080)), 600, 1, win_font, 3000)
        winBox.text.append(Winner.name + ' Wins!')
        winBox.render_text()
        winBox.paste_textBox()
        pygame.display.update()
        pygame.time.delay(winBox.delay)
        running = False

    # turn list
    turn_list = [turn(User, Opponent, somethin)]

    while running:
        # Create Background
        screen.fill((0, 240, 240))
        fight_background.paste((0, 0))
        screen.blit(attack_font.render(
            str(pygame.mouse.get_pos()),
            False, (0, 0, 0)), (0, 0))

        # Paste Sprites
        if User.current_mon != None:
            User.current_mon.paste(screen_w(450 / 1920), screen_h(900 / 1080), 'ground',
                                   User.current_mon.battle_sprite_right, True)
        if Opponent.current_mon is not None:
            Opponent.current_mon.paste(screen_w(1250 / 1920), screen_h(900 / 1080), 'ground',
                                       Opponent.current_mon.battle_sprite_left, True)

        # Paste Text Box
        somethin.paste_textBox()

        # Paste Buttons
        Button.paste_buttons(buttons)
        Button.button_hovers(buttons)

        # Update Screen
        pygame.display.update()

        # Control Turn
        turn_list[-1].activePhase(buttons, turn_list, attack)

        if current_user_mon != User.current_mon:
            moves = Button.create_move_buttons(User.current_mon.moveset, attack_font,
                                               850 + size[0])
            monButtons = Button.create_mon_buttons(
                [Joshumon for Joshumon in User.Joshumons if Joshumon != User.current_mon and Joshumon.fainted == False],
                attack_font)
            current_user_mon = User.current_mon

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
                if attack in buttons and attack.is_clicked() and pygame.time.get_ticks() - attack.last_click >= 200 and not mouse_state:
                    buttons = moves
                    buttons.append(back)
                    attack.last_click = pygame.time.get_ticks()
                    mouse_state = True

                if swap in buttons and swap.is_clicked() and pygame.time.get_ticks() - swap.last_click >= 200 and not mouse_state:
                    buttons = monButtons
                    buttons.append(back)
                    swap.last_click = pygame.time.get_ticks()
                    mouse_state = True
                    turn_list[-1].mon_select = True

                if back in buttons and back.is_clicked() and pygame.time.get_ticks() - swap.last_click >= 200 and not mouse_state:
                    buttons = [attack, swap]
                    swap.last_click = pygame.time.get_ticks()
                    turn_list[-1].mon_select = False
                    mouse_state = True

                for x in moves:
                    if x in buttons and x.is_clicked() and pygame.time.get_ticks() - x.last_click >= 200 and mouse_state == False:
                        buttons = []
                        User.action = ['attack', x.move]
                        Opponent.action = Opponent.AI_Move()
                        turn_list[-1].phase = 'turnStart'
                        x.last_click = pygame.time.get_ticks()
                        mouse_state = True

                for x in monButtons:
                    if x in buttons and x.is_clicked() and pygame.time.get_ticks() - x.last_click >= 200 and mouse_state == False:
                        buttons = []
                        User.action = ['swap', x.mon]
                        Opponent.action = Opponent.AI_Move()
                        turn_list[-1].phase = 'turnStart'
                        mouse_state = True
                        turn_list[-1].mon_select = False
                        x.last_click = pygame.time.get_ticks()
        game_clock.clock.tick(game_clock.FPS)
