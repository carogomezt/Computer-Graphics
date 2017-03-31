import pygame
import random
import ConfigParser



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

  def update(self):
    if self.dir == 2:
      self.rect.x += 2
    if self.dir == 1:
      self.rect.x -= 2
    if self.dir == 0:
      self.rect.y += 2
    if self.dir == 3:
      self.rect.y -= 2

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
    jp = Jugador(m,[100, 100])
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jp.dir = 2
                if event.key == pygame.K_LEFT:
                    jp.dir = 1
                if event.key == pygame.K_UP:
                    jp.dir = 3
                if event.key == pygame.K_DOWN:
                    jp.dir = 0
      


        pantalla.fill(NEGRO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)

