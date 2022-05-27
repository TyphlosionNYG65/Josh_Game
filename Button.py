import pygame,Text,Joshumon
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
    def __init__(self, text):
        self.text = text
        self.size = self.text.size
        self.width = self.size[0] / 2
        self.height = self.size[1] / 2
        self.x = self.text.center[0]
        self.y = self.text.center[1]
        self.center_x = self.x + self.width
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
    def __init__(self, x, y, size,color,text = None,font = None,outline = None):
        self.x = x
        self.y = y
        self.width = size[0] / 2
        self.height = size[1] / 2
        self.center_x = self.x + self.width
        self.center_y = self.y + self.height
        self.color = color
        self.inverse_color = (255 - self.color[0], 255 - self.color[1], 255 - self.color[2])
        self.rectangle = pygame.Surface((size[0],size[1]))
        self.rectangle.fill(color)
        self.active_color = True
        self.hovering = False
        self.last_click = 0
        if text != None:
            self.font = font
            self.words = text
            self.text = Text.Text(self.font,self.words,(self.center_x,self.center_y),self.inverse_color,'center')
        else:
            self.text = None
        if outline != None:
            self.outline_color = outline[0]
            self.outline_thick = outline[1]
            self.outline = pygame.Surface((size[0]+(self.outline_thick*2),size[1]+(self.outline_thick*2)))
            self.outline.fill(self.outline_color)
        else:
            self.outline = None
    def flip_color(self):
        if self.active_color:
            self.rectangle.fill(self.inverse_color)
            self.active_color = False
            if self.text != None:
                self.text = Text.Text(self.font,self.words,(self.center_x,self.center_y),self.color,'center')
        elif not self.active_color:
            self.rectangle.fill(self.color)
            self.active_color = True
            if self.text != None:
                self.text = Text.Text(self.font,self.words,(self.center_x,self.center_y),self.inverse_color,'center')

    def is_hovering(self):
        """
        Detects if left mouse button is hovering over button\n
        :return: boolean
        """
        if self.center_x - self.width <= pygame.mouse.get_pos()[0] <= self.center_x + self.width and self.center_y - self.height <= \
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
    def __init__(self,x,y, size, font, move,outline=None):
        super().__init__(x,y, size,move.type.color,None ,font,outline)
        self.move = move
        self.counter = 0
        self.type = move.type
        self.color = self.type.color
        self.inverse_color = self.type.alt_color
        self.font = font
        self.words = self.move.name
        self.text = Text.Text(self.font, self.words, (self.center_x, self.center_y), self.inverse_color, 'center')




def button_hovers(buttons):
    for button in buttons:
        button.is_hovering()


def paste_buttons(buttons):
    moves = 0
    for button in buttons:
        if type(button) == textButton:
            screen.blit(button.text.render, button.text.position)
        if type(button) == rectangleButton:
            if button.outline != None:
                screen.blit(button.outline, (button.x-button.outline_thick, button.y-button.outline_thick))
            screen.blit(button.rectangle, (button.x,button.y))
            if button.text != None:
                screen.blit(button.text.render, button.text.position)

        if type(button) == moveButton:
            moves += 1

            screen.blit(button.outline, (button.x - button.outline_thick, button.y - button.outline_thick))
            screen.blit(button.rectangle, (button.x, button.y))
            screen.blit(button.text.render, button.text.position)

def create_move_buttons(moves,font):
    total = []
    move_count = 0
    for i in moves:
        x = 1000 + move_count * 200
        y = 900
        move_count += 1
        total.append(moveButton(x, y, (200, 100), font, i, ((0, 0, 0), 2)))
    return total










