import pygame

import Text
import Textures
import Joshumon
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

    def __init__(self, text, position=(0, 0)):
        self.text = text
        self.size = self.text.size
        self.width = self.size[0] / 2
        self.height = self.size[1] / 2
        self.x = position[0]
        self.y = position[1]
        self.center_x = self.x
        self.center_y = self.y - self.height
        self.last_click = 0

    def is_hovering(self):
        """
        Detects if left mouse button is hovering over button\n
        :return: boolean
        """
        mouse_pos = pygame.mouse.get_pos()
        if self.x - self.width <= mouse_pos[0] <= self.x + self.width and self.center_y - self.height <= \
                mouse_pos[1] <= self.center_y + self.height:
            if self.text.active_color:
                self.text.new_render()
            return True
        else:
            if not self.text.active_color:
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
        self.last_click = 0
        self.rectangle.set_alpha(120)

        if text is not None:
            self.font = font
            self.words = text
            self.text = Text.Text(self.font, self.words, self.inverse_color)
        else:
            self.text = None
        if outline is not None:
            self.outline_color = outline[0]
            self.outline_thick = outline[1]
            self.outline = pygame.Surface((size[0] + (self.outline_thick * 2), size[1] + (self.outline_thick * 2)))
            self.outline.fill(self.outline_color)
            self.outline.set_alpha(100)
        else:
            self.outline = None

    def flip_color(self):
        if self.active_color:
            self.rectangle.fill(self.inverse_color)
            self.active_color = False
            if self.text is not None:
                self.text.new_render()
        elif not self.active_color:
            self.rectangle.fill(self.color)
            self.active_color = True
            if self.text is not None:
                self.text.new_render()

    def is_hovering(self):
        """
        Detects if left mouse button is hovering over button\n
        :return: boolean
        """
        if self.center_x - self.width <= pygame.mouse.get_pos()[
            0] <= self.center_x + self.width and self.center_y - self.height <= \
                pygame.mouse.get_pos()[1] <= self.center_y + self.height:
            if self.active_color != False:
                self.flip_color()
            return True
        else:

            if self.active_color != True:
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
        self.text = pygame.freetype.font.render_to()


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
        scale_area = (size[0]/4 * size[1])
        self.sprite = self.mon.scale(self.mon,self.mon.Left_pic, scale_area )
        while self.sprite.get_size()[0] > self.width/2 - 2 or self.sprite.get_size()[1] > self.height*2 - 2:
            scale_area *= .95
            self.sprite = self.mon.scale(self.mon, self.mon.Left_pic, scale_area)
        self.text = Text.Text(self.font, self.words, self.inverse_color)
        self.text_height = self.text.render.get_size()[1]



class selectButton(rectangleButton):
    def __init__(self, x, y, size,color = (50, 50, 50)):
        super().__init__( x, y, size, color, None, None, ((0,0,0),1))
        self.size = size
        self.image = pygame.transform.scale(Textures.plus,(size))
        self.image_width,self.image_height = self.image.get_size()
        self.selected = False
        self.color = color
        self.alt_color = (55, 55, 55)
        mon = None

    def change_image(self,mon = None):
        if mon == None:
            self.image = pygame.transform.scale(Textures.plus,(self.size))
        else:
            self.image = mon.scale(mon,mon.Left_pic, self.size[0]*self.size[1] * .6)
        self.image_width, self.image_height = self.image.get_size()



def button_hovers(buttons):
    for button in buttons:
        button.is_hovering()


def paste_buttons(buttons):
    for button in buttons:
        if type(button) == textButton:
            button.text.paste((button.center_x, button.center_y), 'center')
            continue
        if type(button) == rectangleButton:
            if button.outline is not None:
                screen.blit(button.outline, (button.x - button.outline_thick, button.y - button.outline_thick))
            screen.blit(button.rectangle, (button.x, button.y))
            if button.text is not None:
                button.text.paste((button.center_x, button.center_y), 'center')
            continue

        if type(button) == moveButton:
            screen.blit(button.outline, (button.x - button.outline_thick, button.y - button.outline_thick))
            screen.blit(button.rectangle, (button.x, button.y))
            button.text.paste((button.center_x, button.center_y), 'center')
            continue

        if type(button) == monButton:
           # screen.blit(button.outline, (button.x - button.outline_thick, button.y - button.outline_thick))
            pygame.draw.rect(screen, (0, 0, 0),
                            (button.x - 1, button.y - 1, (button.width * 2) + 2, (button.height * 2) + 2), 1)
            screen.blit(button.rectangle, (button.x, button.y))


            button.text.paste((button.x + screen_w(2/1920) + button.width/2, button.y + button.height - button.text_height/2), 'left')
            screen.blit(button.sprite, (button.x + screen_w(2/1920),
                                        button.y + (button.height * 2) - button.sprite.get_size()[1]))
            continue
        if type(button) == selectButton:

            pygame.draw.rect(screen, (0, 0, 0),
                             (button.x - 1, button.y - 1, (button.width * 2) + 2, (button.height * 2) + 2), 1)
            screen.blit(button.rectangle, (button.x, button.y))
            screen.blit(button.image,(button.x + button.width -button.image_width/2,button.y+button.height - button.image_height/2))


def create_move_buttons(moves, font, center):
    total = []
    move_count = 0
    center_x = center
    length = len(moves)
    button_width = 125
    for i in moves:
        x = screen_w((center_x - length * 1 / 2 * button_width) / 1920) + move_count * screen_w(button_width / 1920)
        y = screen_h(1000 / 1080)
        move_count += 1
        total.append(moveButton(x, y, (screen_w(button_width / 1920), screen_h(75 / 1080)), font, i, ((0, 0, 0), 2)))
    return total


def create_mon_buttons(mons, font):
    total = []
    move_count = 0
    for i in mons:
        x = screen_w(1500 / 1920) + move_count * screen_w(150 / 1920)
        y = screen_h(1000 / 1080)
        move_count += 1
        total.append(monButton(x, y, (screen_w(150 / 1920), screen_h(75 / 1080)), font, i, ((0, 0, 0), 2)))
    return total
