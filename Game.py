from screen_parameters import *
from game_clock import clock
from StartScreen import Start

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
            screen.blit(i.pic, (i.x, i.y))

def main():
    pygame.init()
    Start()
    pygame.display.update()


    # Initializing Variables
    running = True
    screen_images = []

    # main loop
    while running:
        my_font = pygame.font.SysFont('Comic Sans MS', 20)
        pygame.mouse.set_visible(True)
        screen.fill((0, 240, 240))

        pygame.display.update()

        pressed = pygame.key.get_pressed()

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

        # Update clock
        clock.tick(FPS)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
