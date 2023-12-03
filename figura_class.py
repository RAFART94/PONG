import pygame as pg
import random as ra

class Raqueta():
    def __init__(self, pos_x, pos_y, color=(255,255,255),  w=20, h=120):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w = w
        self.h = h

    def dibujar(self, surface):
        pg.draw.rect(surface, self.color, (self.pos_x, self.pos_y, self.w, self.h))

    def mover(self, teclado_arriba, teclado_abajo):
        estado_teclado = pg.key.get_pressed()

        if estado_teclado[teclado_arriba] == True and self.pos_y >= 0:
            self.pos_y -= 1

        if estado_teclado[teclado_abajo] == True and  self.pos_y <= 480:
            self.pos_y += 1

    #Lo que hace el '@property' o decorador, es poder nombrar o invocar las funciones sin necesidad de parentesis
    @property
    def derecha(self):
        return self.pos_x + (self.w//2)
    @property
    def izquierda(self):
        return self.pos_x - (self.w//2)
    @property
    def arriba(self):
        return self.pos_y + (self.h//2)
    @property
    def abajo(self):
        return self.pos_y - (self.h//2)

    

class Pelota():
    def __init__(self, pos_x, pos_y, color=(255,255,255), radio=5, vx=1, vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.radio = radio
        self.vx = vx
        self.vy = vy
        self.contadorDerecho = 0
        self.contadorIzquierdo = 0

    def dibujar(self, surface):
        pg.draw.circle(surface, self.color, (self.pos_x, self.pos_y), self.radio)

    def mover(self, x_max=800, y_max=600):
        self.pos_x += self.vx
        self.pos_y += self.vy
        #limite derecho
        if self.pos_x >= x_max + (1*self.radio):
            self.pos_x = 400
            self.pos_y = 300
            self.vx *= -1
            self.vy *= -1
            self.contadorDerecho += 1

        #limite izquierdo
        if self.pos_x <= 0 - (1*self.radio):
            self.pos_x = 400
            self.pos_y = 300
            self.vx *= -1
            self.vy *= -1
            self.contadorIzquierdo += 1

        if self.pos_y >= y_max or self.pos_y <= 0:
            self.vy *= -1
        
    def mostrar_marcador(self, surface):
        fuente1 = pg.font.Font(None, 30)
        fuente2 = pg.font.SysFont('Verdana', 30)
        marcador1 = fuente1.render(str(self.contadorIzquierdo), True, (255,255,255))
        marcador2 = fuente1.render(str(self.contadorDerecho), True, (255,255,255))
        player1 = fuente2.render('Player 1', True, (255,255,255))
        player2 = fuente2.render('Player 2', True, (255,255,255))
        surface.blit(marcador1, (325,50))
        surface.blit(marcador2, (450,50))
        surface.blit(player1, (225,20))
        surface.blit(player2, (450,20))

    @property
    def derecha(self):
        return self.pos_x + (self.radio)
    @property
    def izquierda(self):
        return self.pos_x - (self.radio)
    @property
    def arriba(self):
        return self.pos_y + (self.radio)
    @property
    def abajo(self):
        return self.pos_y - (self.radio)