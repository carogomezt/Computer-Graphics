import pygame

ANCHO = 500
ALTO = 400

if __name__=='__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.set_caption('Ejemplo')
    fin = False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
