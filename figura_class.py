import pygame as pg

class Raqueta():
    def __init__(self, pos_x, pos_y, color=(255,255,255),w=20, h=120):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h

    def dibujar(self, surface):
        pg.draw.rect(surface, self.color, (self.pos_x-(self.w//2), self.pos_y-(self.h//2), self.w, self.h))


class Pelota():
    def __init__(self, pos_x, pos_y, color=(255,255,255), radio=5):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.radio = radio

    def dibujar(self, surface):
        pg.draw.circle(surface, self.color, (self.pos_x, self.pos_y), self.radio)