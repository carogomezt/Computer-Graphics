import pygame
from libreria import *

'''
    Ejercicio 4:
    1. Dibujar un vector V1 en el plano.
    2. Dibujar el vector V2 a 30 grados en la horizontal con inicio en V1.
    3. Dibujar el vector V3 a 45 grados sobre la horizontal del vector V2.
    La magnitud de los vectores V1, V2, V3 es subjetiva.
'''


C = [ANCHO/2, ALTO/2]

if __name__=='__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pantalla.fill(BLANCO)
    fin = False
    plano = Cartesiano(pantalla, [300, 300])
    # plano.Punto([20, 20])
    v = Vector([100, 100])
    plano.Linea([0, 0], v.p)
    # lista = [[-10, 50], [40, 100], [-100, 100]]
    # plano.Poligono(lista)
    pf = v.AnguloPunto(100, 30)
    puntoFinalv2 = [pf[0] + v.p[0], pf[1] + v.p [1]]
    plano.Linea(v.p, puntoFinalv2)
    pf2 = v.AnguloPunto(100, 45)
    puntoFinalv3 = [pf2[0] + puntoFinalv2[0], pf2[1] + puntoFinalv2[1]]
    plano.Linea(puntoFinalv2, puntoFinalv3)
    pygame.display.flip()

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
