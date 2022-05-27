import Textures,pygame,screen_parameters

class hpBar:
    def __init__(self,position,size):
        self.width = size[0]
        self.height = size[1]
        self.x = position[0]
        self.y = position[1]
        self.Back = pygame.transform.smoothscale(Textures.HP_Back,size)
        self.Border = pygame.transform.smoothscale(Textures.HP_Border,size)
        self.HP_High = pygame.transform.smoothscale(Textures.HP_High,size)
        self.HP_Low = pygame.transform.smoothscale(Textures.HP_Low,size)
        self.bar = self.HP_High

    def new_joshumon(self,Joshumon):
        self. mon = Joshumon
        self.current_HP = Joshumon.current_HP
        self.max_HP = Joshumon.HP

    def calc_Bar(self):
        self.current_HP = self.mon.current_HP
        percent = self.current_HP/self.max_HP
        if percent<= .2:
            self.bar = self.HP_Low
        elif percent > .2:
            self.bar = self.HP_High
        self.bar = pygame.transform.smoothscale(self.bar,(self.width *percent,self.height))

    def paste(self):
        screen_parameters.screen.blit(self.Border,(self.x,self.y))
        screen_parameters.screen.blit(self.Back, (self.x,self.y))
        screen_parameters.screen.blit(self.bar, (self.x,self.y))

