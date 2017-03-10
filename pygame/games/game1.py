import pygame

'''
    Perro moviendose por la pantalla con las teclas
'''


ANCHO=640
ALTO=480

if __name__ == '__main__':
    pygame.init()
    pantalla= pygame.display.set_mode([ANCHO, ALTO])
    fondo = pygame.image.load("img1.jpg")
    objeto = pygame.image.load("dog.png")
    var_x = 0
    var_y = 0
    move =[0, 0, 0, 0]
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move =[0, 0, 0, 1]
                if event.key == pygame.K_LEFT:
                    move =[0, 0, 1, 0]
                if event.key == pygame.K_UP:
                    move =[1, 0, 0, 0]
                if event.key == pygame.K_DOWN:
                    move =[0, 1, 0, 0]
                if event.key == pygame.K_SPACE:
                    move =[0, 0, 0, 0]

        if move[3] == 1:
            var_x += 1
            if var_x > (ANCHO - 64):
                var_x = ANCHO - 64
        elif move[2] == 1:
            var_x -= 1
            if var_x < 0:
                var_x = 0
        elif move[1] == 1:
            var_y += 1
            if var_y > (ALTO - 64):
                var_y = ALTO - 64
        elif move[0] == 1:
            var_y -=1
            if var_y < -0:
                var_y = ALTO
        pantalla.blit(fondo, [0, 0])
        pantalla.blit(objeto, [var_x, var_y])
        pygame.display.flip()
