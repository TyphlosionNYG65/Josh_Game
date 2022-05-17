import pygame,math,random, Textures
from screen_parameters import screen_vals
import Textures


width = screen_vals.width
height = screen_vals.height
speed = 1
class Player:
    def __init__(self,x,y,pic,x_dim,y_dim):
        self.x = x
        self.y = y
        self.x_velocity = 0
        self.y_velocity = 0
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.pic_name = pic
        self.pic = pygame.image.load(pic)
        self.pic = pygame.transform.scale(self.pic,(self.x_dim,self.y_dim))

    def update_position(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

        if 0 > self.x :
            self.x = 0
            self.x_velocity = 0
        if self.x> width - 30:
            self.x =width - 30
            self.x_velocity = 0
        if 0 > self.y :
            self.y = 0
            self.y_velocity = 0
        if self.y> height-60:
            self.y = height-60
            self.y_velocity = 0

    def update_velocity(self,movement):
        velocity = self.add(movement)
        self.x_velocity = velocity[0]
        self.y_velocity = velocity[1]

    def magnitude(self,v):
        return math.sqrt(sum(v[i] * v[i] for i in range(len(v))))

    def add(self,v):
        total = [0, 0]
        for i in v:
            total[0] += i[0]
            total[1] += i[1]
        mag = self.magnitude(total)
        if mag != 0:
            vector = [(speed * i) / mag for i in total]
            return vector
        else:
            return [0, 0]

    def contact(self,other):
        x_range = [self.x-(self.x_dim/2),self.x+(self.x_dim/2)]
        y_range = [self.y-(self.y_dim/2),self.y+(self.y_dim/2)]
        if x_range[0] <= other.x <= x_range[1] and y_range[0] <= other.y <= y_range[1]:
            return True


class Enemy(Player):
    def __init__(self,x,y,pic,x_dim,y_dim,target,targeting):
        super().__init__(x,y,pic,x_dim,y_dim)
        self.target = target
        self.targeting = targeting

    def add(self,v):
        mag = self.magnitude(v)
        if mag != 0:
            vector = [(speed * i) / mag for i in v]
            return vector
        else:
            return [0, 0]

    def update_velocity(self):
        hor_displace = self.target.x - self.x
        ver_displace = self.target.y - self.y
        AI_Moves = {'Right' : [1,0],'Left':[-1,0], 'Up': [0,-1],'Down': [0,1]}
        if hor_displace >= 0:
            pref_x = 'Right'
            el_x = 'Left'
        else:
            pref_x = 'Left'
            el_x = 'Right'
        if ver_displace >= 0:
            pref_y = 'Down'
            el_y = 'Up'
        else:
            pref_y = 'Up'
            el_y = 'Down'
        direction = random.choices([pref_x,pref_y,el_x,el_y], weights = (self.targeting/2,self.targeting/2,(1-self.targeting)/2,(1-self.targeting)/2))
        direction = AI_Moves[direction[0]]
        velocity = self.add(direction)
        self.x_velocity = velocity[0]
        self.y_velocity = velocity[1]









