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
    reloj = pygame.time.Clock()
    n = 1
    m = 1
    flag = True
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

        if(n < ANCHO and n > 0):
            plano.Puntico([0+n, ALTO-n])
            reloj.tick(90)
            m = 0
        else:
            if(m > 0 and m < ALTO):
                plano.Puntico2([ANCHO-m, 0+2*m])
                reloj.tick(90)


        m+=1
        n+=1
        pygame.display.flip()
