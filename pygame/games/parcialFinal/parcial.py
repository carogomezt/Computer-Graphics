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
        self.cielo = []
        self.vida = 300
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

            col_cielo = pygame.sprite.spritecollide(self, cielo, False)
            if len(col_cielo) > 0:
                self.vida -= 10



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
                b = Muro(img, pos)
                b.an_img = an_img
                spriteUnico.add(b)
                spriteGeneral.add(b)
            x += an_c
        y+= al_c
        x = 0

def cargar_Enemigo(archivo, capa, spriteUnico, spriteGeneral, an_img, tipo):
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
                if tipo == 1:
                    b = Enemy(img, pos)
                if tipo == 2:
                    b = EnemyMove(img, pos)
                b.an_img = an_img
                spriteUnico.add(b)
                spriteGeneral.add(b)
            x += an_c
        y+= al_c
        x = 0

def cargar_EnemigoNivel2(archivo, capa, spriteUnico, spriteGeneral, an_img, tipo):
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
                b = EnemyLevel2(img, pos, tipo)
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


class Enemy(pygame.sprite.Sprite):
    def __init__(self, obj_img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/enemy.gif').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.cont = 0
        self.varx = 3
        self.vary = 0

    def update(self):
        self.rect.x -= self.varx
        self.rect.y += self.vary

class EnemyMove(pygame.sprite.Sprite):
    def __init__(self, obj_img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/ghost.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.cont = 0
        self.varizq = 6
        self.varder = 1
        self.vary = 0

    def update(self):
        # print self.rect.x, self.cont
        # self.rect.x -= self.varx
        if self.cont < 150:
            self.rect.x -= self.varizq
            self.cont += 1
        elif self.cont >= 150  and self.cont < 250:
            self.rect.x += self.varder
            self.cont += 1
        elif self.cont == 250:
            self.cont = 0

class EnemyLevel2(pygame.sprite.Sprite):
    def __init__(self, obj_img, pos, tipo):
        pygame.sprite.Sprite.__init__(self)
        if tipo == 1:
            self.image = pygame.image.load('img/thwomp.png').convert_alpha()
        if tipo == 2:
            self.image = pygame.image.load('img/superthwomp.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.cont = 0
        self.varx = 3
        self.vary = 3

    def update(self):
        if self.cont < 50:
            self.rect.y += self.vary
            self.rect.x -= self.varx
            self.cont += 1
        elif self.cont >= 50  and self.cont < 100:
            self.rect.y -= self.vary
            self.rect.x -= self.varx
            self.cont += 1
        elif self.cont == 100:
            self.cont = 0

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

    enemy = pygame.sprite.Group()
    enemyMove = pygame.sprite.Group()

    cargar_Enemigo('nivel1Enemys.json', 'Enemys', enemy, todos, an_img, 1)
    cargar_Enemigo('nivel1Enemys2.json', 'Enemys2', enemyMove, todos, an_img, 2)

    cielo = pygame.sprite.Group()

    cargar_fondo('nivel1Cielo.json', 'Cielo', cielo, todos, an_img)
    jp.cielo = cielo
    jp.bloques = bloques
    jp.agua = agua
    jp.final = final
    todos.add(jp)
    fuente = pygame.font.Font(None, 30)
    finjuego = False
    continuar = True
    reloj = pygame.time.Clock()
    # x = 0
    while continuar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finjuego = True
                continuar = False
            if event.type == pygame.KEYDOWN:
                continuar = False

        intro = pygame.image.load('img/intro.jpg')
        pantalla.blit(intro, [0, 100])
        descrp = fuente.render('Press any key to continue', True, BLANCO)
        pantalla.blit(descrp, [290, 420])
        pygame.display.flip()
    seguir = True
    victoria = True
    time = 0
    while seguir and not finjuego:
        #Captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
                seguir = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jp.Izquierda()
                if event.key == pygame.K_RIGHT:
                    jp.Derecha()
                if event.key == pygame.K_SPACE:
                    jp.Salto()
                    jp.saltar = 1
                if event.key == pygame.K_a:
                    victoria = True
                    seguir = False

        # print "vida", jp.vida
        todos.update()
        pantalla.blit(fondo, [0, 0])
        todos.draw(pantalla)
        pygame.display.flip()
        # print jp.vida
        # print jp.flag
        if not jp.flag:
            victoria = True
            seguir = False
        if jp.vida <= 0:
            victoria = False
            seguir = False

        # print jp.flag
        reloj.tick(20)
    if not victoria:
        seguir = True
        while seguir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finjuego = True
                    seguir = False
                if event.type == pygame.KEYDOWN:
                    seguir = False
            pantalla.fill(NEGRO)
            win = pygame.image.load('img/gameover.jpg')
            pantalla.blit(win, [150, 100])
            pygame.display.flip()
    else:
        continuar = True
        while continuar and not finjuego:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finjuego = True
                    continuar = False
                if event.type == pygame.KEYDOWN:
                    continuar = False

            pantalla.fill(NEGRO)
            fte = pygame.font.Font(None, 80)
            texto = fte.render('LEVEL 2', True, BLANCO)
            descrp = fuente.render('Press any key to continue', True, BLANCO)
            pantalla.blit(texto, [300, 250])
            pantalla.blit(descrp, [290, 350])
            pygame.display.flip()
            reloj.tick(60)

        fondo= pygame.image.load('nivel2.png')
        an_img, al_img = fondo.get_size()
        hero = pygame.image.load('img/character.png').convert_alpha()
        todos = pygame.sprite.Group()
        jp = Player(transformImage(hero, 96, 0, 32, 32))
        jp.an_img = an_img

        bloques = pygame.sprite.Group()
        agua = pygame.sprite.Group()
        final = pygame.sprite.Group()

        cargar_fondo('nivel2Muros.json', 'Muros', bloques, todos, an_img)
        cargar_fondo('nivel2Peligro.json', 'Peligro', agua, todos, an_img)
        cargar_fondo('nivel2Final.json', 'Final', final, todos, an_img)

        enemy = pygame.sprite.Group()
        enemyMove = pygame.sprite.Group()

        cargar_EnemigoNivel2('nivel2Enemigo.json', 'Enemigo', enemy, todos, an_img, 1)
        cargar_EnemigoNivel2('nivel2Enemigo2.json', 'Enemigo2', enemyMove, todos, an_img, 2)

        jp.flag = True
        jp.bloques = bloques
        jp.final = final
        todos.add(jp)

        if victoria:
            victoria = False
            seguir = True

        while seguir and not finjuego:
            #Captura de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin = True
                    seguir = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        jp.Izquierda()
                    if event.key == pygame.K_RIGHT:
                        jp.Derecha()
                    if event.key == pygame.K_SPACE:
                        jp.Salto()

            todos.update()
            pantalla.blit(fondo, [0, 0])
            todos.draw(pantalla)
            pygame.display.flip()
            print "final", jp.flag
            if not jp.flag:
                victoria = True
                seguir = False
            if jp.vida <= 0:
                victoria = False
                seguir = False

            reloj.tick(20)

        if not victoria:
            seguir = True
            while seguir:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        finjuego = True
                        seguir = False
                    if event.type == pygame.KEYDOWN:
                        seguir = False
                pantalla.fill(NEGRO)
                win = pygame.image.load('img/gameover.jpg')
                pantalla.blit(win, [150, 100])
                pygame.display.flip()
        else:
            continuar = True
            while continuar and not finjuego:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        finjuego = True
                        continuar = False
                    if event.type == pygame.KEYDOWN:
                        continuar = False

                pantalla.fill(NEGRO)
                fte = pygame.font.Font(None, 80)
                texto = fte.render('LEVEL 3', True, BLANCO)
                descrp = fuente.render('Press any key to continue', True, BLANCO)
                pantalla.blit(texto, [300, 250])
                pantalla.blit(descrp, [290, 350])
                pygame.display.flip()
                reloj.tick(60)
