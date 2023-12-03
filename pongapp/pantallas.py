import pygame as pg
from pongapp.figura_class import *
from pongapp.utils import *

class Partida():
    def __init__(self):
        pg.init()
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption('Pong')
        self.tasa_refresco = pg.time.Clock()

        self.pelota = Pelota(ANCHO//2, ALTO//2, COLOR_PELOTA)
        self.raqueta1 = Raqueta(ANCHO-800, ALTO//2)
        self.raqueta2 = Raqueta(ANCHO-20, ALTO//2)

        self.fuente1 = pg.font.Font(None, 40)
        self.fuente2 = pg.font.SysFont('Verdana', 30)
        self.contadorDerecho = 0
        self.contadorIzquierdo = 0
        self.quienMarco = ''

    def bucle_fotograma(self):
        game_over = True
        while game_over:
            self.valor_tasa = self.tasa_refresco.tick(350)

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = False
        
            self.pantalla_principal.fill(COLOR_CANCHA)
            #pg.draw.line(self.pantalla_principal, COLOR_BLANCO, (ANCHO//2,0), (ANCHO//2,ALTO), width=10)
            self.mostrar_linea_central()

            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)
            self.pelota.dibujar(self.pantalla_principal)
            self.mostrar_jugadores()

            self.raqueta1.mover(pg.K_w, pg.K_s)
            self.raqueta2.mover(pg.K_UP, pg.K_DOWN)
            self.quienMarco = self.pelota.mover()

            self.pelota.comprobar_choqueV2(self.raqueta1, self.raqueta2)
            self.mostrar_marcador()

            pg.display.flip()

        pg.quit()

    def mostrar_linea_central(self):
            '''
            cont_linea = 0
            while cont_linea <= 600:
                pg.draw.line(self.pantalla_principal, COLOR_BLANCO, (400,cont_linea), (400,cont_linea+50), width=10)
                cont_linea += 70
            '''

            for cont_linea in range(0,601,70):
                pg.draw.line(self.pantalla_principal, COLOR_BLANCO, (ANCHO//2,cont_linea), (ANCHO//2,cont_linea+50), width=10)
            
    def mostrar_jugadores(self):
        player1 = self.fuente2.render('Player 1', True, COLOR_AZUL)
        player2 = self.fuente2.render('Player 2', True, COLOR_AZUL)
        self.pantalla_principal.blit(player1, (225,20))
        self.pantalla_principal.blit(player2, (450,20))

    def mostrar_marcador(self):
        if self.quienMarco == 'right':
                self.contadorDerecho += 1
        elif self.quienMarco == 'left':
                self.contadorIzquierdo += 1
        self.fuente1 = pg.font.Font(None, 40)
        marcador1 = self.fuente1.render(str(self.contadorIzquierdo), True, COLOR_NARANJA)
        marcador2 = self.fuente1.render(str(self.contadorDerecho), True, COLOR_NARANJA)
        self.pantalla_principal.blit(marcador1, (325,50))
        self.pantalla_principal.blit(marcador2, (450,50))   



