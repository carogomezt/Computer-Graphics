import pygame
import time
from libreria import *

'''
    Ejercicio 5:
    1. Dibujar un vector V1 en el plano.
    2. Defina un radio n, rotar desde 0 a 360 un vector de radio n sobre la cabeza del vector v1(ciclo infinito)
    TODO:
    1. seleccionar 50 valores de x aleatoreamente
    2. Para cada punto muestre desplazamiento en Y hasta desaparecer de la pantalla.
    los desplazamientos en Y seran aleatorios
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
    reloj = pygame.time.Clock()
    n = 0
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
        if(n <= 360):
            pantalla.fill(BLANCO)
            plano = Cartesiano(pantalla, [300, 300])
            v = Vector([100, 100])
            plano.Linea([0, 0], v.p)
            pf = v.AnguloPunto(100, n)
            puntoFinalv2 = [pf[0] + v.p[0], pf[1] + v.p [1]]
            plano.Linea(v.p, puntoFinalv2)
            reloj.tick(20)
            n += 1
        else:
            n = 0
        pygame.display.flip()
