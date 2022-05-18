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

    def __init__(self, font, text, position, color, orient):
        self.font = font
        self.text = text
        self.size = font.size(text)
        if orient == 'right':
            self.position = (position[0] - self.size[0], position[1])
        elif orient == 'left':
            self.position = position
        elif orient == 'center':
            self.position = (position[0] - (self.size[0] / 2), position[1])
        self.color = color
        self.inverse_color = (255 - self.color[0], 255 - self.color[1], 255 - self.color[2])
        self.active_color = True
        self.render = font.render(text, False, color)
        self.center = (position[0], position[1] + (self.size[1] / 2))

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
