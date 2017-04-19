import pygame
import random
import ConfigParser
import math

'''
    Buscar DDA
'''

ANCHO=512
ALTO=480
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

class Jugador(pygame.sprite.Sprite):
  def __init__(self, matx, pos):
    pygame.sprite.Sprite.__init__(self)
    self.matx = matx
    self.dir = 2
    self.cont = 0
    self.image = self.matx[self.dir][0]
    self.rect = self.image.get_rect()
    self.rect.x = pos[0]
    self.rect.y = pos[1]
    self.ipos = pos
    self.fpos = [30, 30]
    self.m = 0
    self.mover = 0
    self.x = pos[0]

  def Mover(self, info, posf):
    if info == 1:
        self.xf = self.fpos[0]
        self.yf = self.fpos[1]
        self.dx = self.xf - self.rect.x
        self.dy = self.yf - self.rect.y
        if self.dx != 0:
            pend = float(self.dy/self.dx)
            if pend >= 0:
                self.m = 1
            else:
                self.m = -1
            self.x = 1
        else:
            self.m = 0
            self.x = 0

        self.mover = 1

  def update(self):
    if(self.rect.x <= self.fpos[0]):
        self.rect.x += 1
    if(self.rect.x > self.fpos[0]):
        self.rect.x -= 1

    if(self.rect.y <= self.fpos[1]):
        self.rect.y += self.m
    if(self.rect.y > self.fpos[1]):
        self.rect.y -= self.m


    self.image = self.matx[self.dir][self.cont]
    #self.rect.self.image.get_rect()
    if self.cont < 2:
      self.cont += 1
    else:
      self.cont = 0

if __name__ == '__main__':
    pygame.init()
    pantalla= pygame.display.set_mode([ANCHO, ALTO])

    imagen = pygame.image.load('img-anim/animals.png').convert_alpha()

    m = []
    for fila in range(4):
      lista= []
      for i in range(3):
        cuadro = imagen.subsurface(0+(i*32), 0+(fila*32), 32, 32)
        lista.append(cuadro)
      m.append(lista)
    jp = Jugador(m,[20, 20])
    todos = pygame.sprite.Group()
    todos.add(jp)

    fin = False
    reloj = pygame.time.Clock()
    i = 0
    while not fin:
        #Captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                btns = pygame.mouse.get_pressed()
                if btns[0] == 1:
                    pos = pygame.mouse.get_pos()
                    jp.fpos = pos
                    jp.Mover(1, pos)



        pantalla.fill(NEGRO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)
