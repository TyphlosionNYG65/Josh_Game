import Button
import Interactives
import Text
import Textures
import Trainer
import pygame
import game_clock
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

        def activePhase(self, buttons, turn_list, attack):
            print(self.phase)
            move_responses = {
                'Supereffective': 'Nice move, king',
                'Noteffective': 'Kinda lame move bro',
                'None': 'That move was shit and you should feel bad'
            }
            if self.phase == 'preTurn':
                buttons.append(attack)
                self.phase = 'None'
                return


            elif self.phase == 'turnStart':
                if self.User.current_mon.SD >= self.Opponent.current_mon.SD:
                    self.first = self.User

                    self.last = self.Opponent
                else:
                    self.first = self.Opponent

                    self.last = self.User
                self.phase = 'firstMoveStart'
                return

            elif self.phase == 'firstMoveStart':
                self.textbox.text.append(
                    self.first.current_mon.name + ' ' + self.first.action.text + ' ' + self.last.current_mon.name)
                damage, variant = self.first.current_mon.attack(self.last.current_mon, self.first.action)
                if variant != None:
                    self.textbox.text.append(move_responses[variant])
                self.last.current_mon.recalc_HP(damage)
                self.last.current_mon.HP_Bar.calc_Bar()
                self.phase = 'firstMove'
                self.fainted = self.faintCheck()
                if self.fainted != []:
                    for trainer in self.fainted:
                        self.textbox.text.append(trainer.current_mon.name + ' fainted!')
                        trainer.current_mon = None
                self.textbox.render_text()
                return

            elif self.phase == 'firstMove':
                if self.textbox.text_lines == []:
                    if self.fainted != []:
                        self.phase = 'turnEnd'
                        return
                    self.phase = 'lastMoveStart'
                    return
                return


            elif self.phase == 'lastMoveStart':
                self.textbox.text.append(
                    self.last.current_mon.name + ' ' + self.last.action.text + ' ' + self.first.current_mon.name)
                damage, variant = self.last.current_mon.attack(self.first.current_mon, self.last.action)
                if variant != None:
                    self.textbox.text.append(move_responses[variant])
                self.textbox.render_text()
                self.first.current_mon.recalc_HP(damage)
                self.first.current_mon.HP_Bar.calc_Bar()
                self.phase = 'lastMove'
                self.fainted = self.faintCheck()
                if self.fainted != []:
                    for trainer in self.fainted:
                        self.textbox.text.append(trainer.current_mon.name + ' fainted!')
                        trainer.current_mon = None
                self.textbox.render_text()
                return

            elif self.phase == 'lastMove':
                if self.textbox.text_lines == []:
                    self.phase = 'turnEnd'
                    return
                return


            elif self.phase == 'turnEnd':
                if self.textbox.text_lines == []:
                    if self.fainted != []:
                        for trainer in self.fainted:
                            if not trainer.check_mons():
                                self.phase = 'battleOver'
                                return
                            else:
                                trainer.start_battle()

                    turn_list.append(turn(self.User, self.Opponent, self.textbox))

                return

            elif self.phase == 'battleOver':
                if self.textbox.text_lines == []:
                    if self.first.current_mon == None:
                        battleEnd(self.last)
                    elif self.last.current_mon == None:
                        battleEnd(self.first)

        def faintCheck(self):
            fainted = []
            if self.User.current_mon.fainted :
                fainted += [User]
            if self.Opponent.current_mon.fainted:
                fainted += [Opponent]
            return fainted

    def showHP(Trainer):
        Trainer.current_mon.HP_Bar.calc_Bar()
        if Trainer == User:
            Trainer.current_mon.HP_Bar.paste(400, 950)
        elif Trainer == Opponent:
            Trainer.current_mon.HP_Bar.paste(1100, 700)

    def battleEnd(Winner):
        global running
        winBox = Text.textBox((500, 500), 600, 1, win_font, 3000)
        winBox.text.append(Winner.name + ' Wins!')
        winBox.render_text()
        winBox.paste_textBox()
        pygame.display.update()
        pygame.time.delay(winBox.delay)
        running = False

    # Initialize Trainers
    User.start_battle()  # Initializes Player
    Opponent.start_battle()  # Initializes AI

    # Initialize textures
    fight_background = pygame.transform.scale(Textures.Fight_Background, (screen_vals.width, screen_vals.height))

    # Initial variables
    mouse_state = False  # Controller for whether mouse as been clicked
    running = True  # While True battle is running

    user_move_selection = None
    buttons = []
    # Create Fonts
    attack_font = pygame.font.SysFont('Bahnschrift', 30)
    text_font = pygame.font.SysFont('arial', 15)
    win_font = pygame.font.SysFont('Bahnschrift', 30)

    # Create text boxes
    somethin = Text.textBox((500, 500), 200, 2, text_font, 1000)

    # Create buttons
    moves = Button.create_move_buttons(User.current_mon.moveset, attack_font)
    attack = Button.rectangleButton(screen_w(.8), screen_h(.8), (200, 100), (255, 0, 0), 'Attack', attack_font,
                                    ((0, 0, 0), 2))
    # turn list
    turn_list = [ turn(User, Opponent, somethin)]

    while running:
        # Create Background
        screen.fill((0, 240, 240))
        screen.blit(fight_background, (0, 0))

        # Paste Sprites
        if User.current_mon != None:
            screen.blit(User.current_mon.user_sprite, (450, 600))
            showHP(User)

        if Opponent.current_mon != None:
            screen.blit(Opponent.current_mon.opp_sprite, (1100, 450))
            showHP(Opponent)


        # Paste Text Box
        somethin.paste_textBox()

        # Paste Buttons
        Button.paste_buttons(buttons)
        Button.button_hovers(buttons)

        # Update Screen
        pygame.display.update()
        # Control Turn
        turn_list[-1].activePhase(buttons,turn_list,attack)

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
                    print('clicked')
                for x in moves:
                    if x in buttons and x.is_clicked() and pygame.time.get_ticks() - x.last_click >= 200 and mouse_state == False:
                        buttons = []
                        User.action = x.move
                        Opponent.action = Opponent.AI_Move()
                        turn_list[-1].phase = 'turnStart'
                        attack.last_click = pygame.time.get_ticks()
                        mouse_state = True
        game_clock.clock.tick(game_clock.FPS)
