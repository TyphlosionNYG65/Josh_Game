import pygame
from screen_parameters import screen

class Button:
    """
    Initial Parameters\n
    1. x: X coordinate of button\n
    2. y: y coordinate of button\n
    3. size: width and height of button\n

    Attributes\n
    1. width: Horizontal distance of edge of button from center
    2. height: Vertical distance of edge of button from center
    3. x: Equivalent to initial parameter x
    4. y equivalent to initial parameter y

    Methods\n
    1. is_clicked(self): Detects if left mouse button is clicked while mouse hovers over the button\n
    2. is_hovering(self): Detects if left mouse button is hovering over button\n
    """
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.width = size[0] / 2
        self.height = size[1] / 2

    def is_clicked(self):
        """
        Detects if left mouse button is clicked while mouse hovers over the button
        """
        if pygame.mouse.get_pressed()[0]:
            if self.is_hovering():
                return True
        else:
            return False

    def is_hovering(self):
        """
        Detects if left mouse button is hovering over button\n
        :return:
        """
        if self.x - self.width <= pygame.mouse.get_pos()[0] <= self.x + self.width and self.y - self.height <= \
                pygame.mouse.get_pos()[1] <= self.y + self.height:
            return True


class textButton(Button):
    """
        Initial Parameters\n
        1. text: Text object representing text of the textButton

        Attributes\n
        1. width: Horizontal distance of edge of button from center
        2. height: Vertical distance of edge of button from center
        3. x: Horizontal position of center of text
        4. y: Vertical position of center of text
        5. text: equivalent to initial parameter text
        6. hovering: True if mouse is hovering over button

        Methods\n
        1. is_clicked(self): Detects if left mouse button is clicked while mouse hovers over the button\n
        2. is_hovering(self): Detects if left mouse button is hovering over button\n
        """
    def __init__(self, text):
        self.text = text
        self.size = self.text.size
        self.width = self.size[0] / 2
        self.height = self.size[1] / 2
        self.x = self.text.center[0]
        self.y = self.text.center[1]
        self.hovering = False

    def is_hovering(self):
        """
        Detects if left mouse button is hovering over button\n
        :return: boolean
        """
        if self.x - self.width <= pygame.mouse.get_pos()[0] <= self.x + self.width and self.y - self.height <= \
                pygame.mouse.get_pos()[1] <= self.y + self.height:
            if not self.hovering:
                self.hovering = True
                self.text.new_render()
            return True
        else:
            if self.hovering:
                self.hovering = False
                self.text.new_render()
            return False


def button_hovers(buttons):
    for button in buttons:
        button.is_hovering()


def paste_buttons(buttons):
    for button in buttons:
        screen.blit(button.text.render, button.text.position)


