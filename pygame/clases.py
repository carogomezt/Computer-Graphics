import pygame
from libreria import *


C = [ANCHO/2, ALTO/2]

if __name__=='__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pantalla.fill(BLANCO)
    fin = False
    plano = Cartesiano(pantalla, [300, 300])
    # plano.Punto([20, 20])
    v = Vector([100, 100])
    plano.Linea([0, 00], v.p)
    # lista = [[-10, 50], [40, 100], [-100, 100]]
    # plano.Poligono(lista)

    pygame.display.flip()



    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            if event.type == pygame.KEYDOWN:
                v.Evento(event)
                plano.Linea([0, 0], v.p)
                pygame.display.flip()
