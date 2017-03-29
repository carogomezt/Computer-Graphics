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

def Traer_fondo(archivo, an_re, al_re):
  imagen = pygame.image.load('img-maze/background.png')
  ancho, alto = imagen.get_size()
  print ancho, alto
  an_re = 32
  al_re = 32

  tabla = []

  for var_x in range(0, ancho/an_re):
    fila = []
    for var_y in range(0, alto/al_re):
      cuadro = (0 + (var_x*an_re), 0 + (var_y*al_re), an_re, al_re)
      img_cuadro = imagen.subsurface(cuadro)
      fila.append(img_cuadro)
    tabla.append(fila)
  return tabla

if __name__ == '__main__':
    pygame.init()
    pantalla= pygame.display.set_mode([ANCHO, ALTO])



    pygame.display.flip()

    fin = False
    reloj = pygame.time.Clock()
    while not fin:
        #Captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
