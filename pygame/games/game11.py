import pygame

ANCHO=640
ALTO=480
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)


if __name__ == '__main__':
    pygame.init()
    pantalla= pygame.display.set_mode([ANCHO, ALTO])
    fondo = pygame.image.load("background.jpg")



    fin = False
    reloj = pygame.time.Clock()
    x = 0
    while not fin:
        #Captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

        pantalla.blit(fondo, [x, -720])
        pygame.display.flip()
        reloj.tick(60)
        x -= 2 
