from screen_parameters import screen,font_scale,screen_vals,screen_w,screen_h
import pygame, Button, game_clock,Joshumon
def select_screen(background):
    # Define variables
    running = True
    mouse_state = False
    result = None
    current_selecting_button = None
    mons_showing = False

    # create fonts
    minor_font = pygame.font.SysFont('Arial', font_scale(30))

    # create buttons
    select1 = Button.selectButton(screen_w(500/1920),screen_h(900/1080),(screen_w(100/1920),screen_h(100/1080)))
    select2 = Button.selectButton(screen_w(650/1920),screen_h(900/1080),(screen_w(100/1920),screen_h(100/1080)))
    select3 = Button.selectButton(screen_w(800/1920),screen_h(900/1080),(screen_w(100/1920),screen_h(100/1080)))
    select4 = Button.selectButton(screen_w(950/1920),screen_h(900/1080),(screen_w(100/1920),screen_h(100/1080)))
    select5 = Button.selectButton(screen_w(1100/1920),screen_h(900/1080),(screen_w(100/1920),screen_h(100/1080)))
    select6 = Button.selectButton(screen_w(1250/1920),screen_h(900/1080),(screen_w(100/1920),screen_h(100/1080)))
    select_buttons = [select1,select2,select3,select4,select5,select6]
    buttons = select_buttons[:]

    mon_button_width = [300,310,1610]
    mon_button_height = [99,200,800]
    mon_buttons = []
    mons = Joshumon.Joshumons.__subclasses__()
    length = len(mons)
    button_x = mon_button_width[1]
    button_y = mon_button_height[1]
    for mon in mons:
        mon_buttons.append(Button.monButton(button_x,button_y,(mon_button_width[0],mon_button_height[0]),minor_font,mon,((0,0,0),1)))
        button_y += mon_button_height[0] + 1
        if button_y == mon_button_height[2]:
            button_y = mon_button_height[1]
            button_x += mon_button_width[0] +1




    # initialize textures
    background.scale((screen_vals.width + 100, screen_vals.height + 100))

    while running:
        screen.fill((0, 240, 240))

        background.paste((-100,-100))
        Button.paste_buttons(buttons)
        if mons_showing:
            Button.paste_buttons(mon_buttons)
        pygame.display.update()
        if mons_showing:
            Button.button_hovers(mon_buttons)
        Button.button_hovers(buttons)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_state = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in select_buttons:
                    if button in buttons and button.is_clicked() and pygame.time.get_ticks() - button.last_click >= 200 and not mouse_state:
                        if current_selecting_button != None:
                            current_selecting_button.outline.fill((0,0,0))
                        if current_selecting_button == button:
                            current_selecting_button = None
                            mons_showing = False
                        else:
                            button.outline.fill((255,255,255))
                            current_selecting_button = button
                            mons_showing = True
                if mons_showing:
                    for button in mon_buttons:
                        if button.is_clicked() and pygame.time.get_ticks() - button.last_click >= 200 and not mouse_state:
                            current_selecting_button.change_image(button.mon)





        game_clock.clock.tick(game_clock.FPS)
    return result