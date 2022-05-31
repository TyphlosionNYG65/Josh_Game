import Text
import pygame

from screen_parameters import screen, screen_w, screen_h


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
                self.hovering = False
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

    def __init__(self, text, position):
        self.text = text
        self.size = self.text.size
        self.width = self.size[0] / 2
        self.height = self.size[1] / 2
        self.x = position[0]
        self.y = position[1]
        self.center_x = self.x
        self.center_y = self.y - self.height
        self.hovering = False

    def is_hovering(self):
        """
        Detects if left mouse button is hovering over button\n
        :return: boolean
        """
        if self.x - self.width <= pygame.mouse.get_pos()[0] <= self.x + self.width and self.center_y - self.height <= \
                pygame.mouse.get_pos()[1] <= self.center_y + self.height:
            if not self.hovering:
                self.hovering = True
                self.text.new_render()
            return True
        else:
            if self.hovering:
                self.hovering = False
                self.text.new_render()
            return False


class rectangleButton(Button):
    def __init__(self, x, y, size, color, text=None, font=None, outline=None):
        self.x = x
        self.y = y
        self.width = size[0] / 2
        self.height = size[1] / 2
        self.center_x = self.x + self.width
        self.center_y = self.y + self.height
        self.color = color
        self.inverse_color = (255 - self.color[0], 255 - self.color[1], 255 - self.color[2])
        self.rectangle = pygame.Surface((size[0], size[1]))
        self.rectangle.fill(color)
        self.active_color = True
        self.hovering = False
        self.last_click = 0
        if text is not None:
            self.font = font
            self.words = text
            self.text = Text.Text(self.font, self.words, self.inverse_color)

            while self.text.size[0] >= self.width*2:
                self.font.size
        else:
            self.text = None
        if outline is not None:
            self.outline_color = outline[0]
            self.outline_thick = outline[1]
            self.outline = pygame.Surface((size[0] + (self.outline_thick * 2), size[1] + (self.outline_thick * 2)))
            self.outline.fill(self.outline_color)
        else:
            self.outline = None

    def flip_color(self):
        if self.active_color:
            self.rectangle.fill(self.inverse_color)
            self.active_color = False
            if self.text is not None:
                self.text = Text.Text(self.font, self.words, self.color)
        elif not self.active_color:
            self.rectangle.fill(self.color)
            self.active_color = True
            if self.text is not None:
                self.text = Text.Text(self.font, self.words, self.inverse_color, )

    def is_hovering(self):
        """
        Detects if left mouse button is hovering over button\n
        :return: boolean
        """
        if self.center_x - self.width <= pygame.mouse.get_pos()[
            0] <= self.center_x + self.width and self.center_y - self.height <= \
                pygame.mouse.get_pos()[1] <= self.center_y + self.height:
            if not self.hovering:
                self.hovering = True
                self.flip_color()
            return True
        else:

            if self.hovering:
                self.hovering = False
                self.flip_color()
            return False


class moveButton(rectangleButton):
    def __init__(self, x, y, size, font, move, outline=None):
        super().__init__(x, y, size, move.type.color, None, font, outline)
        self.move = move
        self.counter = 0
        self.type = move.type
        self.color = self.type.color
        self.inverse_color = self.type.alt_color
        self.font = font
        self.words = self.move.name
        self.text = Text.Text(self.font, self.words, self.inverse_color)

class monButton(rectangleButton):
    def __init__(self, x, y, size, font, mon, outline=None):
        super().__init__(x, y, size, mon.type1.color, None, font, outline)
        self.mon = mon
        self.counter = 0
        self.color = self.mon.type1.color
        if mon.type2 is not None:
            self.inverse_color = self.mon.type2.color
        else:
            self.inverse_color = self.mon.type1.alt_color
        self.font = font
        self.words = self.mon.name
        self.sprite = self.mon.scale(self.mon.Left_pic,50)
        self.text = Text.Text(self.font, self.words, self.inverse_color)



def button_hovers(buttons):
    for button in buttons:
        button.is_hovering()


def paste_buttons(buttons):
    moves = 0
    for button in buttons:
        if type(button) == textButton:
            button.text.paste((button.center_x, button.center_y), 'center')
        if type(button) == rectangleButton:
            if button.outline is not None:
                screen.blit(button.outline, (button.x - button.outline_thick, button.y - button.outline_thick))
            screen.blit(button.rectangle, (button.x, button.y))
            if button.text is not None:
                button.text.paste((button.center_x, button.center_y), 'center')

        if type(button) == moveButton:
            moves += 1
            screen.blit(button.outline, (button.x - button.outline_thick, button.y - button.outline_thick))
            screen.blit(button.rectangle, (button.x, button.y))
            button.text.paste((button.center_x, button.center_y), 'center')

        if type(button) == monButton:
             screen.blit(button.outline, (button.x - button.outline_thick, button.y - button.outline_thick))
             screen.blit(button.rectangle, (button.x, button.y))
             button.text.paste((button.center_x, button.center_y), 'center')



def create_move_buttons(moves, font):
    total = []
    move_count = 0
    for i in moves:
        x = screen_w(1500 / 1920) + move_count * screen_w(100 / 1920)
        y = screen_h(1000 / 1080)
        move_count += 1
        total.append(moveButton(x, y, (screen_w(100 / 1920), screen_h(50 / 1080)), font, i, ((0, 0, 0), 2)))
    return total

def create_mon_buttons(mons, font):
    total = []
    move_count = 0
    for i in mons:
        x = screen_w(1500 / 1920) + move_count * screen_w(100 / 1920)
        y = screen_h(1000 / 1080)
        move_count += 1
        total.append(monButton(x, y, (screen_w(100 / 1920), screen_h(50 / 1080)), font, i, ((0, 0, 0), 2)))
    return total
