import pygame
import random
import ConfigParser
import math

ANCHO=640
ALTO=480
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

class Luchador(pygame.sprite.Sprite):
    def __init__(self, mati, pos):
        pygame.sprite.Sprite.__init__(self)
        self.mati = mati
        self.accion = 1
        self.dir = 0
        self.varx = 4
        self.cont = 0
        self.image = self.mati[self.accion][0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.lsriv = []

    def update(self):
        if self.accion == 1:
            self.image = self.mati[self.accion][self.cont]
            if self.cont < 3:
                self.cont += 1
            else:
                self.cont = 0
            if self.dir == 1:
                self.rect.x += self.varx
            if self.dir == 2:
                self.rect.x -= self.varx

        if self.accion == 2:
            self.image = self.mati[self.accion][self.cont]
            if self.cont < 2:
                self.cont += 1
            else:
                self.cont = 0
        if self.accion == 6:
            self.image = self.mati[self.accion][self.cont]
            if self.cont < 5:
                self.cont += 1
            else:
                self.cont = 0

            for e in self.lsriv:
                posgp = [self.rect.x + self.rect.width, self.rect.y]
                if e.rect.collidepoint(posgp):
                    e.rect.x += 2
                    print "golpe"

class Dummy(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([35,80])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]



if __name__ == '__main__':
    pygame.init()
    pantalla= pygame.display.set_mode([ANCHO, ALTO])
    imagen = pygame.image.load("ken.png").convert_alpha()
    c_an = 70
    c_al= 80
    m = []
    for fila in range(10):
        lista=[]
        for i in range(7):
            cuadro = imagen.subsurface((i*c_an), (fila*c_al), c_an, c_al)
            lista.append(cuadro)
        m.append(lista)
    jp = Luchador(m, [100, 250])


    todos = pygame.sprite.Group()
    todos.add(jp)
    rivales = pygame.sprite.Group()

    ob = Dummy([250, 250])
    rivales.add(ob)
    jp.lsriv = rivales
    todos.add(ob)
    fin = False
    reloj = pygame.time.Clock()
    # x = 0
    while not fin:
        #Captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jp.dir = 1
                if event.key == pygame.K_LEFT:
                    jp.dir = 2
                if event.key == pygame.K_SPACE:
                    jp.accion = 2
                    jp.cont = 0
                if event.key == pygame.K_a:
                    jp.accion = 6
                    jp.cont = 0
            if event.type == pygame.KEYUP:
                jp.dir = 0
                jp.accion= 1
                # if event.key == pygame.K_UP:
                #     jp.dir = 3
                # if event.key == pygame.K_DOWN:
                #     jp.dir = 0
                # if event.key == pygame.K_SPACE:


        pantalla.fill(NEGRO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(10)
