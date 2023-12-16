import pygame as pg
from pongapp.figura_class import *
from pongapp.utils import *

class Partida():
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption('Pong')
        self.tasa_refresco = pg.time.Clock()

        self.pelota = Pelota(ANCHO//2, ALTO//2, COLOR_PELOTA)
        self.raqueta1 = Raqueta(ANCHO-800, ALTO//2)
        self.raqueta2 = Raqueta(ANCHO-20, ALTO//2)

        self.fuente1 = pg.font.Font(FUENTE1, TAMAÑO1)
        self.fuente2 = pg.font.SysFont('Verdana', TAMAÑO2)

        self.contadorDerecho = 0
        self.contadorIzquierdo = 0
        self.quienMarco = ''
        self.temporizador = TIEMPO_JUEGO #Son 10 segundos
        self.game_over = True
        self.contadorFotograma = 0
        self.colorFondo = COLOR_CANCHA

        self.resultado_partida = ''

    def bucle_fotograma(self):
        #Iniciar en punto de partida con parámetros de finalización de juego
        self.temporizador = TIEMPO_JUEGO
        self.tasa_refresco.tick()
        self.contadorDerecho = 0
        self.contadorIzquierdo = 0
        
        while self.game_over and (self.contadorDerecho < 7 or self.contadorIzquierdo < 7) and self.temporizador > 0:
            self.valor_tasa = self.tasa_refresco.tick(VELOCIDAD_JUEGO)
            self.temporizador = self.temporizador - self.valor_tasa
            self.finalizacion_de_juego()
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return True
            
            color = self.fijar_fondo()
            self.pantalla_principal.fill(color)

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
            self.mostrar_temporizador()
            self.finalizacion_de_juego()
 
            pg.display.flip()

        return self.resultado_partida
    
        

    def mostrar_linea_central(self):
            for cont_linea in range(0,ALTO+1,70):
                pg.draw.line(self.pantalla_principal, COLOR_BLANCO, (ANCHO//2,cont_linea), (ANCHO//2,cont_linea+50), width=10)
            
    def mostrar_jugadores(self):
        player1 = self.fuente2.render('Player 1', True, COLOR_AZUL)
        player2 = self.fuente2.render('Player 2', True, COLOR_AZUL)
        self.pantalla_principal.blit(player1, (POSX_PLAYER1,POSY_PLAYER1Y2))
        self.pantalla_principal.blit(player2, (POSX_PLAYER2,POSY_PLAYER1Y2))

    def mostrar_marcador(self):
        if self.quienMarco == 'right':
                self.contadorDerecho += 1
        elif self.quienMarco == 'left':
                self.contadorIzquierdo += 1
        marcador1 = self.fuente1.render(str(self.contadorIzquierdo), True, COLOR_NARANJA)
        marcador2 = self.fuente1.render(str(self.contadorDerecho), True, COLOR_NARANJA)
        self.pantalla_principal.blit(marcador1, (POSX_MARCADOR1,POSY_MARCADOR1Y2))
        self.pantalla_principal.blit(marcador2, (POSX_MARCADOR2,POSY_MARCADOR1Y2))

    def finalizacion_de_juego(self):
        if self.contadorDerecho > self.contadorIzquierdo:
            self.resultado_partida = f'El ganador es el Player 1:  resultado = Player1:{self.contadorDerecho} , Player2:{self.contadorIzquierdo}'
        elif self.contadorIzquierdo > self.contadorDerecho:
            self.resultado_partida = f'El ganador es el Player 2:  resultado = Player1:{self.contadorDerecho} , Player2:{self.contadorIzquierdo}'
        else:
            self.resultado_partida = f'Empate entre Player 1 y Player 2, resultado = Player1:{self.contadorDerecho} , Player2:{self.contadorIzquierdo}'

    def mostrar_temporizador(self):
        TIEMPO_JUEGO = self.fuente2.render(str(int(self.temporizador/1000)), True, COLOR_ROJO)
        self.pantalla_principal.blit(TIEMPO_JUEGO, (ANCHO//2,20))

    def fijar_fondo(self):
        self.contadorFotograma += 1
        if self.temporizador > 10000:
            self.contadorFotograma = 0
        elif self.temporizador > 5000:
            if self.contadorFotograma == 20:
                if self.colorFondo == COLOR_CANCHA:
                    self.colorFondo = FONDO_NARANJA
                else:
                    self.colorFondo = COLOR_CANCHA
                self.contadorFotograma = 0
        else:
            if self.contadorFotograma == 20:
                if self.colorFondo == COLOR_CANCHA or self.colorFondo == FONDO_NARANJA:
                    self.colorFondo = FONDO_ROJO
                else:
                    self.colorFondo = COLOR_CANCHA
                self.contadorFotograma = 0
        
        return self.colorFondo
        
        '''
        if self.temporizador < 10000 and self.temporizador > 5000:
            self.pantalla_principal.fill(FONDO_NARANJA)
        elif self.temporizador < 5000:
            self.pantalla_principal.fill(FONDO_ROJO)
        else:
            self.pantalla_principal.fill(COLOR_CANCHA)
        '''

class Menu():
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption('Menú')
        self.tasa_refresco = pg.time.Clock()
        self.imagenFondo = pg.image.load('pongapp/images/pong.jpg') #Cargar imágenes
        self.fuente = pg.font.Font(FUENTE1, TAMAÑO2)
        self.sonido = pg.mixer.Sound(SONIDO1)
        
    def bucle_pantalla(self):
        game_over = True
        while game_over:
            pg.mixer.Sound.play(self.sonido)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
                #if event.type == pg.KEYDOWN:
                    #if event.key == pg.K_RETURN:
                        #game_over = False
                        #print('precionaste enter')
            botones = pg.key.get_pressed()
            if botones[pg.K_RETURN]:
                #game_over = False
                return 'partida'
            elif botones[pg.K_r]:
                pg.mixer.Sound.stop(self.sonido)
                return 'record'
        
            self.pantalla_principal.blit(self.imagenFondo, (0,0))
            texto_menu = self.fuente.render('Pulsa ENTER para jugar', True, COLOR_BLANCO)
            texto_record = self.fuente.render('Pulsa R para ver el TOP', True, COLOR_ROJO)
            self.pantalla_principal.blit(texto_menu, (ANCHO//2, ALTO//2))
            self.pantalla_principal.blit(texto_record, (ANCHO//2, ALTO//2+30))

            pg.display.flip()

class Resultado():
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode ((ANCHO,ALTO))
        pg.display.set_caption('Resultado')
        self.tasa_refresco = pg.time.Clock()
        self.fuenteResultado = pg.font.Font(FUENTE1, TAMAÑO3)
        
        self.resultado = ''

    def bucle_pantalla(self):
        game_over = True
        while game_over:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_over = False
            
            botones = pg.key.get_pressed()

            if botones[pg.K_RETURN]:
                game_over = False

        
            self.pantalla_principal.fill(COLOR_BLANCO)
            result = self.fuenteResultado.render(str(self.resultado), True, COLOR_GRANATE)
            self.pantalla_principal.blit(result, (ANCHO-700, ALTO//2))
        
            pg.display.flip()

    def cargar_resultado(self, resultado):
        self.resultado = resultado

class Record():
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode ((ANCHO,ALTO))
        pg.display.set_caption('Records')
        self.tasa_refresco = pg.time.Clock()
        self.fuenteRecord = pg.font.Font(FUENTE1, TAMAÑO1)

    def bucle_pantalla(self):
        game_over = True
        while game_over:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True

            self.pantalla_principal.fill(COLOR_BLANCO)
            result = self.fuenteRecord.render('Mejores Puntuaciones', True, COLOR_GRANATE)

            self.pantalla_principal.blit(result, (ANCHO-600, ALTO-500))

            pg.display.flip()

    