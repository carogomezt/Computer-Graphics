import pygame
import random
import ConfigParser
import math
import json

ANCHO=1100
ALTO= 460
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
        self.enemy = []
        self.enemyMove = []
        self.enemylevel2 = []
        self.patron = []
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

            for e in col_cielo:
                if self.vary > 0:
                    self.rect.bottom = e.rect.top
                elif self.vary < 0:
                    self.rect.top = e.rect.bottom
                self.vary = 0

            col_enemy = pygame.sprite.spritecollide(self, enemy, False)
            if len(col_enemy) > 0:
                self.vida -= 10

            col_enemyMove = pygame.sprite.spritecollide(self, enemyMove, False)
            if len(col_enemyMove) > 0:
                self.vida -= 10

            col_enemylevel2 = pygame.sprite.spritecollide(self, self.enemylevel2, False)
            if len(col_enemylevel2) > 0:
                self.vida -= 10

            col_patron = pygame.sprite.spritecollide(self, self.patron, False)
            if len(col_patron) > 0:
                self.vida = 0


        self.rect.y += self.vary
        col_bloques = pygame.sprite.spritecollide(self, bloques, False)
        for e in col_bloques:
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

def cargar_EnemigoNivel3(archivo, capa, spriteUnico, spriteGeneral, an_img):
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
                b = EnemyLevel3(img, pos)
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

class EnemyLevel3(pygame.sprite.Sprite):
    def __init__(self, obj_img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/momia.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.cont = 0
        self.varx = 3
        self.vary = 7

    def update(self):
        if self.cont < 20:
            self.rect.y += self.vary
            self.rect.x -= self.varx
            self.cont += 1
        elif self.cont >= 20  and self.cont < 40:
            self.rect.y -= self.vary
            self.rect.x -= self.varx
            self.cont += 1
        elif self.cont == 40:
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

    jp.enemy = enemy
    jp.enemyMove = enemyMove
    jp.cielo = cielo
    jp.bloques = bloques
    jp.agua = agua
    jp.final = final
    todos.add(jp)
    fuente = pygame.font.Font("fuente/Orbitron/Orbitron-Regular.ttf", 30)
    menuText = pygame.font.Font("fuente/Orbitron/Orbitron-Regular.ttf", 60)
    finjuego = False
    continuar = True
    reloj = pygame.time.Clock()
    # x = 0
    menu = 0
    contador = 0
    music = pygame.mixer.Sound('sonidos/EnterSandman.wav')
    sn_jump = pygame.mixer.Sound('sonidos/jump.wav')
    sn_forest = pygame.mixer.Sound('sonidos/forest.wav')
    sn_win = pygame.mixer.Sound('sonidos/win.wav')
    while continuar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finjuego = True
                continuar = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = 1
                if event.key == pygame.K_1:
                    continuar = False
                if event.key == pygame.K_2:
                    menu = 2
                if event.key == pygame.K_3:
                    finjuego = True
                    continuar = False
                if event.key == pygame.K_ESCAPE:
                    menu = 1


        if menu == 0:
            sn_forest.set_volume(0.4)
            sn_forest.play()
            intro = pygame.image.load('img/intro.jpg')
            pantalla.blit(intro, [0, 0])
            descrp = fuente.render('Presiona la tecla Espacio para continuar', True, BLANCO)
            pantalla.blit(descrp, [250, 420])
            pygame.display.flip()
        if menu == 1:
            menu = pygame.image.load('img/menu.jpg')
            pantalla.blit(menu, [0, 0])
            descrp = menuText.render('1. Jugar', True, NEGRO)
            pantalla.blit(descrp, [350, 150])
            descrp = menuText.render('2. Instrucciones', True, NEGRO)
            pantalla.blit(descrp, [350, 250])
            descrp = menuText.render('3. Salir', True, NEGRO)
            pantalla.blit(descrp, [350, 350])
            pygame.display.flip()
        if menu == 2:
            intro = pygame.image.load('img/instrucciones.jpg')
            pantalla.blit(intro, [0,0])
            pygame.display.flip()
    sn_forest.stop()
    music.set_volume(0.2)
    music.play()
    seguir = True
    victoria = True
    time = 0
    while seguir and not finjuego:
        #Captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finjuego = True
                seguir = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jp.Izquierda()
                if event.key == pygame.K_RIGHT:
                    jp.Derecha()
                if event.key == pygame.K_SPACE:
                    jp.Salto()
                    sn_jump.play()
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
        pantalla.fill(NEGRO)
        vida = str(jp.vida)
        if jp.vida > 200:
            life = pygame.image.load("img/hearth.png")
            pantalla.blit(life, [64, 428])
        if jp.vida > 100 :
            life = pygame.image.load("img/hearth.png")
            pantalla.blit(life, [32, 428])
        if jp.vida >=0:
            life = pygame.image.load("img/hearth.png")
            pantalla.blit(life, [0, 428])

        texto = fuente.render('Vida: ' + vida, True, BLANCO)
        pantalla.blit(texto, [100, 428])
        contador += 1
        star = pygame.image.load("img/star.png")
        pantalla.blit(star, [300, 425])
        conText = str(contador - (300-jp.vida))
        texto = fuente.render('Puntuacion: ' + conText, True, BLANCO)
        pantalla.blit(texto, [335, 428])
        if not jp.flag:
            victoria = True
            seguir = False
        if jp.vida <= 0:
            victoria = False
            seguir = False

        # print jp.flag
        reloj.tick(20)
    if not victoria:
        music.fadeout(300)
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
            pantalla.blit(win, [300, 0])
            pygame.display.flip()
    else:
        music.fadeout(300)
        continuar = True
        while continuar and not finjuego:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finjuego = True
                    continuar = False
                if event.type == pygame.KEYDOWN:
                    continuar = False

            pantalla.fill(NEGRO)
            fte = pygame.font.Font("fuente/Orbitron/Orbitron-Regular.ttf", 80)
            texto = fte.render('NIVEL 2', True, BLANCO)
            descrp = fuente.render('Presione cualquier tecla para continuar.', True, BLANCO)
            pantalla.blit(texto, [350, 100])
            pantalla.blit(descrp, [220, 250])
            pygame.display.flip()
            reloj.tick(60)

        music.play()
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
        enemylevel2 = pygame.sprite.Group()

        cargar_EnemigoNivel2('nivel2Enemigo.json', 'Enemigo', enemylevel2, todos, an_img, 1)
        cargar_EnemigoNivel2('nivel2Enemigo2.json', 'Enemigo2', enemylevel2, todos, an_img, 2)

        jp.enemylevel2 = enemylevel2
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
                    finjuego = True
                    seguir = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        jp.Izquierda()
                    if event.key == pygame.K_RIGHT:
                        jp.Derecha()
                    if event.key == pygame.K_SPACE:
                        jp.Salto()
                        sn_jump.play()
                    if event.key ==pygame.K_s:
                        victoria = True
                        seguir = False

            # print "vida", jp.vida
            todos.update()
            pantalla.blit(fondo, [0, 0])
            todos.draw(pantalla)
            pygame.display.flip()

            pantalla.fill(NEGRO)
            vida = str(jp.vida)
            if jp.vida > 200:
                life = pygame.image.load("img/hearth.png")
                pantalla.blit(life, [64, 428])
            if jp.vida > 100 :
                life = pygame.image.load("img/hearth.png")
                pantalla.blit(life, [32, 428])
            if jp.vida >=0:
                life = pygame.image.load("img/hearth.png")
                pantalla.blit(life, [0, 428])

            texto = fuente.render('Vida: ' + vida, True, BLANCO)
            pantalla.blit(texto, [100, 428])

            contador += 1
            star = pygame.image.load("img/star.png")
            pantalla.blit(star, [300, 425])
            conText = str(contador - (300-jp.vida))
            texto = fuente.render('Puntuacion: ' + conText, True, BLANCO)
            pantalla.blit(texto, [335, 428])

            if not jp.flag:
                victoria = True
                seguir = False
            if jp.vida <= 0:
                victoria = False
                seguir = False

            reloj.tick(20)

        if not victoria:
            music.fadeout(300)
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
                pantalla.blit(win, [300, 0])
                pygame.display.flip()
        else:
            music.fadeout(300)
            continuar = True
            while continuar and not finjuego:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        finjuego = True
                        continuar = False
                    if event.type == pygame.KEYDOWN:
                        continuar = False

                pantalla.fill(NEGRO)
                fte = pygame.font.Font("fuente/Orbitron/Orbitron-Regular.ttf", 80)
                texto = fte.render('NIVEL 3', True, BLANCO)
                descrp = fuente.render('Presione cualquier tecla para continuar.', True, BLANCO)
                pantalla.blit(texto, [350, 100])
                pantalla.blit(descrp, [220, 250])
                pygame.display.flip()
                reloj.tick(60)

            music.play()
            fondo= pygame.image.load('nivel3.png')
            an_img, al_img = fondo.get_size()
            hero = pygame.image.load('img/character.png').convert_alpha()
            todos = pygame.sprite.Group()
            jp = Player(transformImage(hero, 0, 0, 32, 32))
            jp.an_img = an_img

            bloques = pygame.sprite.Group()
            agua = pygame.sprite.Group()
            final = pygame.sprite.Group()
            cielo = pygame.sprite.Group()

            cargar_fondo('nivel3Muros.json', 'Muros', bloques, todos, an_img)
            cargar_fondo('nivel3Hielo.json', 'Hielo', agua, todos, an_img)
            cargar_fondo('nivel3Final.json', 'Final', final, todos, an_img)
            cargar_fondo('nivel3Cielo.json', 'Cielo', cielo, todos, an_img)

            enemy = pygame.sprite.Group()
            enemyMove = pygame.sprite.Group()
            enemylevel2 = pygame.sprite.Group()
            patron = pygame.sprite.Group()

            cargar_Enemigo('nivel3EnemigoHorizontal.json', 'EnemigoHorizontal', enemyMove, todos, an_img, 2)
            cargar_EnemigoNivel2('nivel3EnemigoVertical.json', 'EnemigoVertical', enemylevel2, todos, an_img, 1)
            cargar_EnemigoNivel3('nivel3Patron.json', 'Patron', patron, todos, an_img)

            jp.patron = patron
            jp.enemyMove = jp.enemyMove
            jp.enemylevel2 = enemylevel2
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
                        finjuego = True
                        seguir = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            jp.Izquierda()
                        if event.key == pygame.K_RIGHT:
                            jp.Derecha()
                        if event.key == pygame.K_SPACE:
                            jp.Salto()
                            sn_jump.play()
                        if event.key == pygame.K_d:
                            victoria = True
                            seguir = False



                # print "vida", jp.vida
                todos.update()
                pantalla.blit(fondo, [0, 0])
                todos.draw(pantalla)
                pygame.display.flip()

                pantalla.fill(NEGRO)
                vida = str(jp.vida)
                if jp.vida > 200:
                    life = pygame.image.load("img/hearth.png")
                    pantalla.blit(life, [64, 428])
                if jp.vida > 100 :
                    life = pygame.image.load("img/hearth.png")
                    pantalla.blit(life, [32, 428])
                if jp.vida >=0:
                    life = pygame.image.load("img/hearth.png")
                    pantalla.blit(life, [0, 428])

                texto = fuente.render('Vida: ' + vida, True, BLANCO)
                pantalla.blit(texto, [100, 428])

                contador += 1
                star = pygame.image.load("img/star.png")
                pantalla.blit(star, [300, 425])
                conText = str(contador - (300-jp.vida))
                texto = fuente.render('Puntuacion: ' + conText, True, BLANCO)
                pantalla.blit(texto, [335, 428])

                if not jp.flag:
                    victoria = True
                    seguir = False
                if jp.vida <= 0:
                    victoria = False
                    seguir = False

                reloj.tick(20)
            if not victoria and not finjuego:
                music.fadeout(300)
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
                    pantalla.blit(win, [300, 0])
                    pygame.display.flip()

            else:
                music.stop()
                seguir = True
                gano = 0
                while seguir and not finjuego:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            finjuego = True
                            seguir = False
                        if event.type == pygame.KEYDOWN:
                            gano += 1
                            if gano == 2:
                                seguir = False
                    sn_win.set_volume(0.1)
                    sn_win.play()
                    if gano == 0:
                        pantalla.fill(NEGRO)
                        win = pygame.image.load('img/final.jpg')
                        pantalla.blit(win, [0, 0])
                        pygame.display.flip()
                    if gano == 1:
                        pantalla.fill(NEGRO)
                        win = pygame.image.load('img/YouWin.png')
                        pantalla.blit(win, [250, 0])
                        fte = pygame.font.Font("fuente/Orbitron/Orbitron-Regular.ttf", 40)
                        texto = fte.render('Puntuacion Total  ' + conText, True, BLANCO)
                        pantalla.blit(texto, [340, 300])
                        pygame.display.flip()
