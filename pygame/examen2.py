import pygame
import time
from libreria import *


C = [ANCHO/2, ALTO/2]

if __name__=='__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pantalla.fill(BLANCO)
    fin = False
    plano = Cartesiano(pantalla, [300, 300])
    # plano.Punto([20, 20])
    # lista = [[-10, 50], [40, 100], [-100, 100]]
    # plano.Poligono(lista)
    r = 20
    v = Vector([2*r, 0])
    m = Vector([2*r, 2*r])
    plano.Linea(v.p, m.p)
    plano.Circulo(r)
    pygame.display.flip()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
