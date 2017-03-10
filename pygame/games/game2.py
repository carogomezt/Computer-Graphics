import pygame

'''
    Perro moviendose por la pantalla con el mouse y con sonidos
'''
ANCHO=640
ALTO=480

if __name__ == '__main__':
    pygame.init()
    pantalla= pygame.display.set_mode([ANCHO, ALTO])
    fondo = pygame.image.load("img1.jpg")
    objeto = pygame.image.load("dog.png")
    sonido = pygame.mixer.Sound("dog.ogg")
    pygame.mouse.set_visible(False)
    fin = False
    while not fin:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                btns = pygame.mouse.get_pressed()
                if btns[0] == 1:
                    sonido.play()

        pantalla.blit(fondo, [0, 0])
        pantalla.blit(objeto, pos)
        pygame.display.flip()
