from pongapp.figura_class import *
from pongapp.pantallas import *
'''
juego = Partida()
juego.bucle_fotograma()

objetoRaqueta = Raqueta(0,500)

objetoPelota = Pelota(0,300)

print(objetoRaqueta.derecha)
print(objetoRaqueta.izquierda)
print(objetoRaqueta.arriba)
print(objetoRaqueta.abajo)

print(objetoPelota.derecha)
print(objetoPelota.izquierda)
print(objetoPelota.arriba)
print(objetoPelota.abajo)


def datosPersonales(*args):
    for datos in args:
        print(datos)

datosPersonales('Jose', 'Martinez', 25, True, [1,2,3])


def mover_mano()->str:
    return 'izquierda'

def recibirMano(mano):
    if mano == 'izquierda':
        print('Zurda')
    else:
        print('Derecha')

recibirMano(mover_mano())


def nombres(apellido):
    return 'Jose Alfredo ' + apellido

def apellidos(apellidos):
    return apellidos

nombres_apellidos = nombres(apellidos('Perez Ruiz'))
print(nombres_apellidos)
'''
file_imagenes = {
            'drcha':[RAQUETA_DERECHA, RAQUETA_DERECHA1, RAQUETA_DERECHA2],
            'izqda':[RAQUETA_IZQUIERDA, RAQUETA_IZQUIERDA1, RAQUETA_IZQUIERDA2]
        }

lado = 'drcha'

def pruebita(lado):
    imagenprueba = {}
    for lado in file_imagenes:
        imagenprueba[lado] = []
        for nombre_fichero in file_imagenes[lado]:
            imagen = pg.image.load(f'pongapp/images/raquetas/imagen00')
            imagenprueba[lado].append(imagen)
    return imagenprueba

respuesta = pruebita(lado)