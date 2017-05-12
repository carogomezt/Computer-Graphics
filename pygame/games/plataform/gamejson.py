import pygame
import random
import ConfigParser
import math
import json

ANCHO=800
ALTO=640
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

def Separar(l, ancho):
    con = 0
    m = []
    fila = []
    for e in l:
        fila.append(e)
        con += 1
        if con == ancho:
            m.append(fila)
            fila = []
            con = 0
    return m

def listaSpr(archivo, al_re, an_re):
  imagen = pygame.image.load(archivo)
  ancho, alto = imagen.get_size()


  tabla = []

  for var_y in range(0, alto/al_re):
    for var_x in range(0, ancho/an_re):
      cuadro = ((var_x*an_re), (var_y*al_re), an_re, al_re)
      img_cuadro = imagen.subsurface(cuadro)
      tabla.append(img_cuadro)
  return tabla

class Muro(pygame.sprite.Sprite):
    def __init__(self, obj_img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = obj_img
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

if __name__ == '__main__':
    pygame.init()
    pantalla= pygame.display.set_mode([ANCHO, ALTO])

    fondo= pygame.image.load('fondo.png')
    # pantalla.blit(fondo, [0, 0])
    # pygame.display.flip()

    #abrimos el archivo json
    with open('mapa.json') as json_file:
        base = json.load(json_file)

    #Extraemos informacion de la imagen de fondo
    ar_sp = ''
    al_c = 0
    an_c = 0

    for valor in base['tilesets']:
        ar_sp = valor['image']
        al_c = valor['tileheight']
        an_c = valor['tilewidth']

    l_sp = listaSpr(ar_sp, al_c, an_c)

    '''
    px = 0
    py = 0
    for c in l_sp:
        pantalla.blit(c, [px, py])
        px += an_c
    pygame.display.flip()
    '''
    #Extraemos informacion de la capa muros
    listam = []
    muros = base['layers']
    ancho_c = 0
    for m in muros:
        # print m["name"]
        if m["name"] == "plataforma":
            listam = m["data"]
            ancho_c = m["width"]

    lsep = Separar(listam, ancho_c)
    for f  in lsep:
        print f

    #Crear lista de bloques de muros
    todos = pygame.sprite.Group()
    bloques = pygame.sprite.Group()

    #cargar muros
    x = 0
    y = 0
    for fila in lsep:
        for e in fila:
            if e != 0:
                pos = [x, y]
                img = l_sp[e-1]
                b = Muro(img, pos)
                bloques.add(b)
                todos.add(b)
            x += an_c
        y+= al_c
        x = 0



    fin = False
    reloj = pygame.time.Clock()
    # x = 0
    while not fin:
        #Captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

        pantalla.blit(fondo, [0, 0])
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)
