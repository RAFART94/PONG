#Aquí se ejecuta todo
import pygame as pg
from figura_class import Pelota, Raqueta

pg.init()
X_MAX = 800
Y_MAX = 600
pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption('Pong')

#Definir tasa de refresco en nuestro bucle de fotogramas, fps= fotograma por segundo
tasa_refresco = pg.time.Clock()

#Creamos un objeto de la clase Pelota o instanciamos la clase Pelota
pelota = Pelota(400, 300, (228,231,19), 15)

raqueta1 = Raqueta(10, 300)#Raqueta izquierda
raqueta2 = Raqueta(790, 300)#Raqueta derecha

game_over = True

while game_over:
    #Obtener la tasa de refresco en milisegundos
    valor_tasa = tasa_refresco.tick(350)#Variable para controlar la velocidad entre fotogramas

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = False

    pantalla_principal.fill((27,149,47))

    pg.draw.line(pantalla_principal, (255,255,255), (400,0), (400,600), width=10)

    raqueta1.mover(pg.K_w, pg.K_s)
    raqueta2.mover(pg.K_UP, pg.K_DOWN)

    pelota.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)

    pg.display.flip()


pg.quit()
