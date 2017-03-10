import pygame

'''
    Perro moviendose por la pantalla con el mouse y siendo perseguido por otro perro
'''

ANCHO=640
ALTO=480

if __name__ == '__main__':
    pygame.init()
    pantalla= pygame.display.set_mode([ANCHO, ALTO])
    fondo = pygame.image.load("img1.jpg")
    perro = pygame.image.load("dog.png")
    mono = pygame.image.load("mon.png")
    pygame.mouse.set_visible(False)
    fin = False
    var_x = 0
    var_y = 0
    lim_x = 0
    lim_y = 0
    while not fin:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                btns = pygame.mouse.get_pressed()
                if btns[0] == 1:
                    lim_x = pos[0]
                    lim_y = pos[1]

        if lim_x != 0:
            if var_x < lim_x:
                var_x += 1
            if var_x > lim_x:
                var_x -= 1
        if lim_y != 0:
            if var_y < lim_y:
                var_y += 1
            if var_y > lim_y:
                var_y -= 1
        pantalla.blit(fondo, [0, 0])
        pantalla.blit(perro, pos)
        pantalla.blit(mono, [var_x, var_y])
        pygame.display.flip()
