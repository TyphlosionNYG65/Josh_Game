import pygame
import screen_parameters


class Text:
    """
    Initial Parameters\n
    1. font: Font selection for the text from pygame.font.SysFont n
    2. text: String value for desired text to be represented by Text object\n
    3. position: Tuple for the initial desired position of the text on screen\n
    4. color: Tuple for the rgb color value of the text\n
    5. orient: orientation of the text based off of position. Possible values are left, right, and center\n
    \n
    Attributes\n
    1. self.font: Equivalent to inital font parameter\n
    2. self.text: Equivalent to initial text parameter\n
    3. self.position: Altered position to match orientation of text object\n
    4. self.color: Equivalent to initial color parameter\n
    5. self.size: (x,y) for size of the Text Object\n
    6. self.inverse_color: Inverse of self.color\n
    7. self.center: (x,y) for center of Text object position\n
    8. self.active_color: True if current color of the Text object is equivalent to self.color\n
    9. self.render: The rendered surface of the Text object for blitting onto screen\n
    Methods\n
    1. new_render(self): If active_color bool is True then active_color bool is set to False and a new render is set
    with inverse color. Opposite if active_color bool is False
    """

    def __init__(self, font, text,  color):
        self.font = font
        self.text = text


        self.color = color
        self.inverse_color = (255 - self.color[0], 255 - self.color[1], 255 - self.color[2])
        self.active_color = True
        self.render = font.render(text, False, color)
        if type(self.render) == tuple:
            self.render = self.render[0]

        self.size = self.render.get_size()



    def new_render(self):
        """
        If active_color bool is True then active_color bool is set to False and a new render is set
        with inverse color. Opposite if active_color bool is False
        """
        if self.active_color:
            self.render = self.font.render(self.text, False, self.inverse_color)
            self.active_color = False
        else:
            self.render = self.font.render(self.text, False, self.color)
            self.active_color = True

    def paste(self,position,orient):
        if orient == 'right':
            self.position = (position[0] - self.size[0], position[1])
        elif orient == 'left':
            self.position = position
        elif orient == 'center':
            self.position = (position[0] - (self.size[0] / 2), position[1] - (self.size[1] / 2))
        screen_parameters.screen.blit(self.render,self.position)

class textBox:
    def __init__(self, position, width, height, font, delay):
        self.height = height
        self.size = [width, (font.size(' ')[1] * height) + 4]
        self.rectangle = pygame.Surface((self.size[0], self.size[1]))
        self.rectangle.fill((255, 255, 255))
        self.text = []
        self.font = font
        self.space = font.size(' ')[0]
        self.word_height = font.size(' ')[1]
        self.text_lines = []
        self.position = position
        self.start_time = pygame.time.get_ticks()
        self.outline = pygame.Surface((self.size[0] + 2, self.size[1] + 2))
        self.outline.fill((0, 0, 0))
        self.delay = delay

    def render_text(self):
        """
        Creates renders for lines in text box to pute in text_lines print queue
        """
        current_line = ''  # create current line initial
        for line in self.text:  # each line loaded into queue
            x = 0
            self.text_lines.append([[False]])  # create first variable in line indicating it hasnt been printed yet
            current_line = ''  # create string for current line
            for word in line.split(' '):  # iterates for each word in line

                word_width = self.font.render(word, 0, (0, 0, 0)).get_size()[0]
                if x + word_width - 2 >= self.size[0]:  # checks if current line goes over size limit
                    x = 0
                    self.text_lines[-1][-1].append(
                        self.font.render(current_line, 0, (0, 0, 0)))  # render current line and create new one
                    self.text_lines[-1].append([False])
                    current_line = ''
                current_line += (' ' + word)  # add current word to line
                x += word_width + self.space  # update position
            if current_line != '':  # checks if leftover from last queue
                self.text_lines[-1][-1].append(self.font.render(current_line, 0, (0, 0, 0)))
        self.text = []  # clears text

    def paste_textBox(self):
        try:  # checks if current line has been printed for enought time
            if pygame.time.get_ticks() >= self.delay + self.start_time and self.text_lines[0][0][0] == True:
                self.text_lines.remove(self.text_lines[0])  # removes current line
            current_text = self.text_lines[0]  # loads next line
            if current_text[0][0] != True:  # if current text hasnt been printed yet resets timer
                self.start_time = pygame.time.get_ticks()
        except IndexError:
            return

        count = 0
        screen_parameters.screen.blit(self.outline, (self.position[0] - 1, self.position[1] - 1,))
        screen_parameters.screen.blit(self.rectangle, self.position)
        for line in current_text:
            x = self.position[0] + 2
            y = self.position[1] + (self.word_height * count)
            count += 1
            line[0] = True
            for word in line[1:]:
                word_width, word_height = word.get_size()
                screen_parameters.screen.blit(word, (x, y))
                x += word_width + self.space
