import pygame
import time
from libreria import *
import random

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
    #plano.Linea([0, 0], v.p)
    # lista = [[-10, 50], [40, 100], [-100, 100]]
    # plano.Poligono(lista)
    n_list = []
    for i in xrange(0,50):
        x = random.randint(0, ANCHO)
        plano.Puntico([x, 0])
        n_list.append(x)
    pygame.display.flip()
    reloj = pygame.time.Clock()
    n = 10
    m = 0
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

        for x in xrange(0,50):
            reloj.tick(500)
            if n < ALTO:
                y = random.randint(m, n)
                plano.Puntico([n_list[x],y])

                print n_list[x] , y
        n+=20
        m+=20

            #pantalla.fill(BLANCO)
        pygame.display.flip()
