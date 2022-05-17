from screen_parameters import *
from Character import *
import Textures
import math
from PIL import Image
def update_positions(Entities,Enemies,Player,base = True,):
    for i in Entities:
        if type(i) == list:
            update_positions(i,Enemies,Player,False)
        else:
            i.update_position()
    if base:
        for i in Enemies:
            if Player.contact(i):
                i.x = 50
                i.y = 50


def update_velocities(Entities):
    for i in Entities:
        if type(i) == list:
            update_velocities(i)
        else:
            i.update_velocity()

def paste_entities(Entities):
    for i in Entities:
        if type(i) == list:
            paste_entities(i)
        else:
            screen.blit(i.pic,(i.x,i.y))


def main():
    pygame.init()
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 20)
    text_surface = my_font.render(f'W-Up\nS-Down\nA-Left\nD-Right\nQ-Quit', False, (0, 0, 0))
    pygame.display.update()
    #Create Entities
    J_man = Player(450, 150, Textures.Josh_Texture,32,64)
    Enemies = [Enemy(500,500, Textures.sus_Texture,50,60,J_man,0.8)]
    Entities = [J_man,Enemies]
    #Initializing Variables
    running = True
    screen_images = []
    moves = {pygame.K_w: (0, -1),
             pygame.K_s: (0, 1),
             pygame.K_a: (-1, 0),
             pygame.K_d: (1, 0)}
    # main loop
    while running:
        update_positions(Entities,Enemies,J_man)


        screen.fill((240,240,240))
        screen.blit(text_surface, (0, 0))

        paste_entities(Entities)
        pygame.display.update()
        pressed = pygame.key.get_pressed()
        movement = [moves[key] for key in moves if pressed[key]]
        J_man.update_velocity(movement)
        update_velocities(Enemies)
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False











# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()

