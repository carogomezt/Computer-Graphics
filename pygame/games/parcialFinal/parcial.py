import pygame
import random
import ConfigParser
import math
import json

ANCHO=1100
ALTO= 416
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self, matx):
        pygame.sprite.Sprite.__init__(self)
        self.matx = matx
        self.dir = 2
        self.image = self.matx[self.dir][0]
        self.rect = self.image.get_rect()
        self.varx = 2
        self.vary = 0
        self.saltar = 1
        self.velocidad = 3
        self.xf = 0
        self.an_img = 0
        self.flag = True
        self.bloques = []
        self.agua = []
        self.final = []
        self.vida = 100
        self.cont = 0


    def Salto(self):
        self.vary =- 8

    def Derecha(self):
        self.varx =+ self.velocidad
        self.dir = 2

    def Izquierda(self):
        self.varx = -self.velocidad
        self.dir = 1

    def gravedad(self):
        if(self.vary == 0):
            self.vary = 1
        else:
            self.vary += 0.35

        piso = ALTO - self.rect.height
        if (self.rect.y >= piso )  and self.vary >= 0:
            self.vary = 0
            self.rect.y = piso

    def update(self):
        self.gravedad()
        # print self.an_img - ANCHO - 16
        if self.rect.x >= ANCHO - 120 and self.varx > 0:
            self.rect.x = ANCHO - 120
            self.xf -= 3

            #-1280 = anchoimg-anchoventana
            lim = (self.an_img - ANCHO -16) *(-1)
            # print "xf", self.xf, "lim", lim
            if self.xf < lim :
                # print "xf", self.xf, "lim", lim,
                self.xf = lim

        elif self.rect.x <= 60 and self.varx < 0:
            self.rect.x = 60
            self.xf += 3

            if self.xf > 0:
                self.xf = 0
        else:
            self.rect.x += self.varx
            col_bloques = pygame.sprite.spritecollide(self, bloques, False)
            for e in col_bloques:
                # print "bloque", e.rect.height
                if self.varx > 0:
                    self.rect.right = e.rect.left

                elif self.varx < 0:
                    self.rect.left = e.rect.right
            col_agua = pygame.sprite.spritecollide(self, agua, False)
            if len(col_agua) > 0:
                self.vida = 0

        self.rect.y += self.vary
        # self.val += 1
        col_bloques = pygame.sprite.spritecollide(self, bloques, False)
        for e in col_bloques:
            # print "bloque", e.rect.height
            if self.vary > 0:
                self.rect.bottom = e.rect.top
            elif self.vary < 0:
                self.rect.top = e.rect.bottom

            self.vary = 0

        self.image = self.matx[self.dir][self.cont]
        if self.cont < 2:
          self.cont += 1
        else:
          self.cont = 0
        col_final = pygame.sprite.spritecollide(self, final, False)
        if len(col_final) > 0:
            self.flag = False


def transformImage(image, posx, posy, width, height):
    d = []
    for fila in range(4):
      l_h= []
      for i in range(4):
        square = image.subsurface(posx+(i*width), posy+(fila*height), width, height)
        l_h.append(square)
      d.append(l_h)
    return d

def cargar_fondo(archivo, capa, spriteUnico, spriteGeneral, an_img):
    #abrimos el archivo json
    with open(archivo) as json_file:
        base = json.load(json_file)

    #Extraemos informacion de la imagen de fondo
    ar_sp = ''
    al_c = 0
    an_c = 0

    for valor in base['tilesets']:
        ar_sp = valor['image']
        al_c = valor['tileheight']
        an_c = valor['tilewidth']
        firstgid = valor['firstgid']

    l_sp = listaSpr(ar_sp, al_c, an_c)
    listam = []
    muros = base['layers']
    ancho_c = 0
    for m in muros:
        # print m["name"]
        if m["name"] == capa:
            listam = m["data"]
            ancho_c = m["width"]
    lsep = Separar(listam, ancho_c)
    x = 0
    y = 0
    for fila in lsep:
        for e in fila:
            if e != 0:
                pos = [x, y]
                img = l_sp[e-firstgid]
                if e == 738:
                    print pos
                b = Muro(img, pos)
                b.an_img = an_img
                spriteUnico.add(b)
                spriteGeneral.add(b)
            x += an_c
        y+= al_c
        x = 0

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
        self.xf = 0
        self.an_img= 0
        self.varx = 3
        self.vary = 0
        self.flag = False

    def update(self):
        self.rect.x -= self.varx
        self.rect.y += self.vary





if __name__ == '__main__':
    pygame.init()
    pantalla= pygame.display.set_mode([ANCHO, ALTO])

    fondo= pygame.image.load('nivel1.png')
    an_img, al_img = fondo.get_size()
    hero = pygame.image.load('img/character.png').convert_alpha()
    todos = pygame.sprite.Group()
    jp = Player(transformImage(hero, 0, 0, 32, 32))
    jp.an_img = an_img

    bloques = pygame.sprite.Group()
    agua = pygame.sprite.Group()
    final = pygame.sprite.Group()
    cargar_fondo('nivel1Muros.json', 'Muros', bloques, todos, an_img)
    cargar_fondo('nivel1Peligro.json', 'Peligro', agua, todos, an_img)
    cargar_fondo('nivel1Agua.json', 'Agua', agua, todos, an_img)
    cargar_fondo('nivel1Final.json', 'Final', final, todos, an_img)

    jp.bloques = bloques
    jp.agua = agua
    jp.final = final
    todos.add(jp)

    fin = False
    reloj = pygame.time.Clock()
    # x = 0

    while not fin:
        #Captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jp.Izquierda()
                if event.key == pygame.K_RIGHT:
                    jp.Derecha()
                if event.key == pygame.K_SPACE:
                    jp.Salto()
                    jp.saltar = 1

        # print "vida", jp.vida
        todos.update()
        pantalla.blit(fondo, [0, 0])
        todos.draw(pantalla)
        pygame.display.flip()
        if not jp.flag:
            pantalla.fill(NEGRO)
            fin = True
        # print jp.flag
        reloj.tick(20)
