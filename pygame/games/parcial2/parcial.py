import pygame
import random
import ConfigParser



ANCHO=800
ALTO=640
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

class Player(pygame.sprite.Sprite):
  def __init__(self, matx, pos):
    pygame.sprite.Sprite.__init__(self)
    self.matx = matx
    self.dir = 2
    self.cont = 0
    self.image = self.matx[self.dir][0]
    self.rect = self.image.get_rect()
    self.rect.x = pos[0]
    self.rect.y = pos[1]
    self.muros = []
    self.tierra = []
    self.vida = 300
    self.speed = 5

  def update(self):
    if self.dir == 2:
      self.rect.x += self.speed
    if self.dir == 1:
      self.rect.x -= self.speed
    if self.dir == 0:
      self.rect.y += self.speed
    if self.dir == 3:
      self.rect.y -= self.speed

    self.image = self.matx[self.dir][self.cont]
    #self.rect.self.image.get_rect()
    if self.cont < 2:
      self.cont += 1
    else:
      self.cont = 0

    col_tierra = pygame.sprite.spritecollide(self, tierra, False)
    for e in col_tierra:
        if self.dir == 2:
            self.rect.right = e.rect.left
        if self.dir == 1:
            self.rect.left = e.rect.right
        if self.dir == 0:
            self.rect.bottom = e.rect.top
        if self.dir == 3:
            self.rect.top = e.rect.bottom
    lcol = pygame.sprite.spritecollide(self, muros, False)
    for e in lcol:
        if self.dir == 2:
            self.rect.right = e.rect.left
        if self.dir == 1:
            self.rect.left = e.rect.right
        if self.dir == 0:
            self.rect.bottom = e.rect.top
        if self.dir == 3:
            self.rect.top = e.rect.bottom

class Enemy(pygame.sprite.Sprite):
  def __init__(self, matx, pos):
    pygame.sprite.Sprite.__init__(self)
    self.matx = matx
    self.dir = 2
    self.cont = 0
    self.image = self.matx[self.dir][0]
    self.rect = self.image.get_rect()
    self.rect.x = pos[0]
    self.rect.y = pos[1]
    self.muros = []
    self.tierra = []
    self.speed = 4

  def update(self):
    if (self.rect.x >= 9*32) and (self.rect.x <= 11*32) and (self.rect.y == 8*32):
        self.dir = 2
        self.rect.x += self.speed
    if(self.rect.x == (11*32) and (self.rect.y >= 8*32) and (self.rect.y <= 10*32)):
        self.dir = 0
        self.rect.y += self.speed
    if (self.rect.x >= 9*32) and (self.rect.x <= 11*32) and (self.rect.y == 10*32):
        self.dir = 1
        self.rect.x -= self.speed
    if(self.rect.x == (9*32) and (self.rect.y >= 8*32) and (self.rect.y <= 10*32)):
        self.dir = 3
        self.rect.y -= self.speed

    self.image = self.matx[self.dir][self.cont]
    #self.rect.self.image.get_rect()
    if self.cont < 2:
      self.cont += 1
    else:
      self.cont = 0

    col_tierra = pygame.sprite.spritecollide(self, tierra, False)
    for e in col_tierra:
        if self.dir == 2:
            self.rect.right = e.rect.left
        if self.dir == 1:
            self.rect.left = e.rect.right
        if self.dir == 0:
            self.rect.bottom = e.rect.top
        if self.dir == 3:
            self.rect.top = e.rect.bottom
    lcol = pygame.sprite.spritecollide(self, muros, False)
    for e in lcol:
        if self.dir == 2:
            self.rect.right = e.rect.left
        if self.dir == 1:
            self.rect.left = e.rect.right
        if self.dir == 0:
            self.rect.bottom = e.rect.top
        if self.dir == 3:
            self.rect.top = e.rect.bottom

class Door(pygame.sprite.Sprite):
    def __init__(self, matx, pos):
        pygame.sprite.Sprite.__init__(self)
        self.matx = matx
        self.cont = 0
        self.image = self.matx[0][0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.open = False
        self.yp = 0

    def update(self):
        self.image = self.matx[self.yp][3]
        if self.open :
            self.yp += 1
            if self.yp > 3:
                self.yp = 3




class Enemy2(pygame.sprite.Sprite):
  def __init__(self, matx, pos):
    pygame.sprite.Sprite.__init__(self)
    self.matx = matx
    self.dir = 2
    self.cont = 0
    self.image = self.matx[self.dir][0]
    self.rect = self.image.get_rect()
    self.rect.x = pos[0]
    self.rect.y = pos[1]
    self.muros = []
    self.tierra = []
    self.speed = 8
    self.var = 0

  def update(self):
    self.var += 3
    if (self.rect.x >= 17*32) and (self.rect.x <= 22*32) and (self.rect.y == 10*32):
        self.dir = 2
        self.rect.x += self.speed
    if(self.rect.x == (22*32) and (self.rect.y >= 10*32) and (self.rect.y <= 15*32)):
        self.dir = 0
        self.rect.y += self.speed
    if (self.rect.x >= 20*32) and (self.rect.x <= 22*32) and (self.rect.y == 15*32):
        self.dir = 1
        self.rect.x -= self.speed
    if(self.rect.x == (20*32) and (self.rect.y >= 15*32) and (self.rect.y <= 18*32)):
        self.dir = 0
        self.rect.y += self.speed
    if (self.rect.x >= 12*32) and (self.rect.x <= 20*32) and (self.rect.y == 18*32):
        self.dir = 1
        self.rect.x -= self.speed
    if (self.rect.x == (12*32) and (self.rect.y >= 14*32) and (self.rect.y <= 18*32)):
        self.dir = 3
        self.rect.y -= self.speed
    if (self.rect.x >= 12*32) and (self.rect.x <= 17*32) and (self.rect.y == 14*32):
        self.dir = 2
        self.rect.x += self.speed
    if (self.rect.x == (17*32) and (self.rect.y >= 10*32) and (self.rect.y <= 14*32)):
        self.dir = 3
        self.rect.y -= self.speed

    # if(self.rect.x == (9*32) and (self.rect.y >= 8*32) and (self.rect.y <= 10*32)):
    #     self.dir = 3
    #     self.rect.y -= self.speed

    self.image = self.matx[self.dir][self.cont]
    #self.rect.self.image.get_rect()
    if self.cont < 2:
      self.cont += 1
    else:
      self.cont = 0

    col_tierra = pygame.sprite.spritecollide(self, tierra, False)
    for e in col_tierra:
        if self.dir == 2:
            self.rect.right = e.rect.left
        if self.dir == 1:
            self.rect.left = e.rect.right
        if self.dir == 0:
            self.rect.bottom = e.rect.top
        if self.dir == 3:
            self.rect.top = e.rect.bottom
    lcol = pygame.sprite.spritecollide(self, muros, False)
    for e in lcol:
        if self.dir == 2:
            self.rect.right = e.rect.left
        if self.dir == 1:
            self.rect.left = e.rect.right
        if self.dir == 0:
            self.rect.bottom = e.rect.top
        if self.dir == 3:
            self.rect.top = e.rect.bottom

class Enemy3(pygame.sprite.Sprite):
    def __init__(self, archivo, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.cont = 0

    def update(self):
        self.cont += 3

class BulletEnemy(pygame.sprite.Sprite):

    def __init__(self, archivo_img, posx, posy, dire):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x= posx
        self.rect.y= posy
        self.dir = dire
        self.speed = 5

    def update(self):
        if self.dir == 2:
          self.rect.x += self.speed
        if self.dir == 1:
          self.rect.x -= self.speed
        if self.dir == 0:
          self.rect.y += self.speed
        if self.dir == 3:
          self.rect.y -= self.speed


class Bullet(pygame.sprite.Sprite):
    def __init__(self, archivo, posx, posy, dire):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.dir = dire
        self.var_y = 8
        self.tierra = []

    def update(self):
        if self.dir == 2:
          self.rect.x += self.var_y
        if self.dir == 1:
          self.rect.x -= self.var_y
        if self.dir == 0:
          self.rect.y += self.var_y
        if self.dir == 3:
          self.rect.y -= self.var_y


class Modifiers(pygame.sprite.Sprite):
    def __init__(self, archivo, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy

class Muro(pygame.sprite.Sprite):
    def __init__(self, obj_img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = obj_img
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Nivel(pygame.sprite.Sprite):
    def __init__(self, ar_mapa, n_nivel,  an_re, al_re):
      pygame.sprite.Sprite.__init__(self)
      self.mapa = self.Ret_mapa(ar_mapa, n_nivel)
      self.fondo = self.Traer_fondo(self.ar_fondo, an_re, al_re)
      self.tierra = self.Ret_tierra(ar_mapa, n_nivel)

    def Traer_fondo(self, archivo, an_re, al_re):
      imagen = pygame.image.load('img/background.png')
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

    def Ret_mapa(self, archivo, n_nivel):
      archivo = 'mapaparcial.map'
      mapa = ConfigParser.ConfigParser()
      mapa.read(archivo)
      self.ar_fondo=  mapa.get(n_nivel, 'origen')
      plano = mapa.get(n_nivel, 'mapa').split('\n')
      posx = 0
      posy = 0
      d = {}
      for sec in mapa.sections():
          if len(sec) == 1:
              # print sec, mapa.get(sec, 'nombre')
              x = int(mapa.get(sec, 'ux'))
              y = int(mapa.get(sec, 'uy'))
              muro= int(mapa.get(sec, 'muro'))
              d[sec] = [[x, y], muro ]

      info_muros = []
      nf = 0
      for fila in plano:
        nc = 0
        print fila
        for e in fila:
          lista = d[e]
          if(lista[1] == 1):
            pos = [nc, nf]
            info = [pos, lista[0]]
            # print info
            info_muros.append(info)
          nc += 1
        nf += 1

      return info_muros

    def Ret_tierra(self, archivo, n_nivel):
        archivo = 'mapaparcial.map'
        mapa = ConfigParser.ConfigParser()
        mapa.read(archivo)
        self.ar_fondo=  mapa.get(n_nivel, 'origen')
        plano = mapa.get(n_nivel, 'mapa').split('\n')
        posx = 0
        posy = 0
        d = {}
        for sec in mapa.sections():
            if len(sec) == 1:
                # print sec, mapa.get(sec, 'nombre')
                x = int(mapa.get(sec, 'ux'))
                y = int(mapa.get(sec, 'uy'))
                muro= int(mapa.get(sec, 'muro'))
                d[sec] = [[x, y], muro ]

        info_tierra = []
        nf = 0
        for fila in plano:
          nc = 0
          print fila
          for e in fila:
            lista = d[e]
            if(lista[1] == 2):
              pos = [nc, nf]
              info = [pos, lista[0]]
              # print info
              info_tierra.append(info)
            nc += 1
          nf += 1
        print info_tierra
        return info_tierra


if __name__ == '__main__':
    pygame.init()
    pantalla= pygame.display.set_mode([ANCHO, ALTO])
    background = pygame.image.load('img/background.jpg')

    hero = pygame.image.load('img/character.png').convert_alpha()

    door_image = pygame.image.load('img/door.png').convert_alpha()

    d = []
    for fila in range(4):
      l_h= []
      for i in range(4):
        square = door_image.subsurface(0+(i*96), 0+(fila*96), 96, 96)
        print i*32, fila*96
        l_h.append(square)
      d.append(l_h)

    door = Door(d,[21.8*32, 16*32])


    m = []
    for fila in range(4):
      l_h= []
      for i in range(3):
        square = hero.subsurface(0+(i*32), 0+(fila*32), 32, 32)
        l_h.append(square)
      m.append(l_h)

    jp = Player(m,[100, 100])

    h = []
    for fila in range(4):
      l_h= []
      for i in range(3):
        square = hero.subsurface(98+(i*32), 0+(fila*32), 32, 32)
        l_h.append(square)
      h.append(l_h)

    enem = Enemy(h, [9*32, 8*32])

    b = []
    for fila in range(4):
      l_h= []
      for i in range(3):
        square = hero.subsurface((6*32)+(i*32), 0+(fila*32), 32, 32)
        l_h.append(square)
      b.append(l_h)

    enem_blue = Enemy2(b, [17*32, 10*32])

    enem_red = Enemy3('img/red-enemy.png', [23*32, 3*32])
    enem_white = Enemy3('img/white_enemy.png', [21*32, 7*32])

    elements = pygame.sprite.Group()
    blt = pygame.sprite.Group()
    blt_enemy = pygame.sprite.Group()
    players = pygame.sprite.Group()

    mdf = pygame.sprite.Group()
    enemys = pygame.sprite.Group()
    enemys_blue =  pygame.sprite.Group()
    enemys_static = pygame.sprite.Group()
    keys = pygame.sprite.Group()
    the_doors = pygame.sprite.Group()
    the_doors.add(door)
    elements.add(door)



    md1 = Modifiers('img/modifier1.png', 10*32, 9*32)
    key = Modifiers('img/key.png', 4*32, 12*32)

    muros = pygame.sprite.Group()
    tierra = pygame.sprite.Group()
    mapa = Nivel('mapaparcial.map', 'nivel1', 32, 32)
    for ls in mapa.mapa:
        pos_p = ls[0]
        x = pos_p[0]*32
        y = pos_p[1]*32
        pos_i = ls[1]
        xi = pos_i[0]
        yi = pos_i[1]
        # print ls[0], x, y
        m = Muro(mapa.fondo[xi][yi], [x, y])
        muros.add(m)
        elements.add(m)

    for ls in mapa.tierra:
        pos_p = ls[0]
        x = pos_p[0]*32
        y = pos_p[1]*32
        pos_i = ls[1]
        xi = pos_i[0]
        yi = pos_i[1]
        # print ls[0], x, y
        m = Muro(mapa.fondo[xi][yi], [x, y])
        tierra.add(m)
        elements.add(m)
    jp.tierra = tierra
    jp.muros = muros

    enem.tierra = tierra
    enem.muros = muros

    enem_blue.tierra = tierra
    enem_blue.muros = muros

    enemys_static.add(enem_red)
    enemys_static.add(enem_white)

    elements.add(enem_red)
    elements.add(enem_white)
    mdf.add(md1)
    keys.add(key)
    enemys.add(enem)
    enemys_blue.add(enem_blue)
    elements.add(enem)
    elements.add(enem_blue)
    elements.add(jp)
    elements.add(md1)
    elements.add(key)

    players.add(jp)



    finjuego = False
    reloj = pygame.time.Clock()
    fuente = pygame.font.Font(None, 30)
    flag = False
    e_modifier = False
    key_modifier = False
    continuar = True
    while continuar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finjuego = True
                continuar = False
            if event.type == pygame.KEYDOWN:
                continuar = False

        texto = fuente.render('BIENVENIDO', True, BLANCO)
        descrp = fuente.render('Presiona Cualquier tecla para Continuar', True, BLANCO)
        pantalla.blit(texto, [350, 250])
        pantalla.blit(descrp, [200, 300])
        pygame.display.flip()
        reloj.tick(60)
    seguir = True
    victoria = False
    while seguir and not finjuego:
        prueba = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finjuego = True
                seguir = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jp.dir = 2
                if event.key == pygame.K_LEFT:
                    jp.dir = 1
                if event.key == pygame.K_UP:
                    jp.dir = 3
                if event.key == pygame.K_DOWN:
                    jp.dir = 0
                if event.key == pygame.K_SPACE:
                    # sn_bullet.play()
                    if(e_modifier == True):
                        reloj.tick(10)
                        blt_jp = Bullet('img/bullet.gif', jp.rect.x+ 15, jp.rect.y +15, jp.dir)
                        blt_jp.tierra = tierra
                        elements.add(blt_jp)
                        blt.add(blt_jp)


        modifier_collide = pygame.sprite.spritecollide(jp, mdf, True)
        if(len(modifier_collide) > 0):
            e_modifier = True

        key_collide = pygame.sprite.spritecollide(jp, keys, True)
        if(len(key_collide) > 0):
            key_modifier = True


        for bullet in blt:
            ls = pygame.sprite.spritecollide(bullet, tierra, True)
            for e in ls:
                blt.remove(bullet)
                elements.remove(bullet)

        for bullet in blt:
            ls = pygame.sprite.spritecollide(bullet, muros, False)
            for e in ls:
                blt.remove(bullet)
                elements.remove(bullet)

        for bullet in blt_enemy:
            ls = pygame.sprite.spritecollide(bullet, the_doors, False)
            for e in ls:
                blt.remove(bullet)
                elements.remove(bullet)

        for bullet in blt:
            ls = pygame.sprite.spritecollide(bullet, enemys, True)
            for e in ls:
                blt.remove(bullet)
                elements.remove(bullet)

        for bullet in blt:
            ls = pygame.sprite.spritecollide(bullet, enemys_blue, True)
            for e in ls:
                blt.remove(bullet)
                elements.remove(bullet)

        for bullet in blt:
            ls = pygame.sprite.spritecollide(bullet, enemys_static, True)
            for e in ls:
                blt.remove(bullet)
                elements.remove(bullet)

        dead = pygame.sprite.spritecollide(jp, enemys, False)
        if len(dead) > 0:
            jp.vida = jp.vida - 5

        dead = pygame.sprite.spritecollide(jp, enemys_blue, False)
        if len(dead) > 0:
            jp.vida = jp.vida - 5

        if enem_red.cont % 13 == 0:
            blt_enem = BulletEnemy('img/fire.png', enem_red.rect.x+5, enem_red.rect.y+25, 0)
            blt_enemy.add(blt_enem)
            elements.add(blt_enem)

        if enem_white.cont % 13 == 0:
            blt_enem_white = BulletEnemy('img/fire.png', enem_white.rect.x-5, enem_white.rect.y, 1)
            blt_enemy.add(blt_enem_white)
            elements.add(blt_enem_white)

        if enem_blue.cont % 13 == 0:
            blt_enem_blue = BulletEnemy('img/fire.png', enem_blue.rect.x, enem_blue.rect.y, enem_blue.dir)
            blt_enemy.add(blt_enem_blue)
            elements.add(blt_enem_blue)

        for bullet in blt_enemy:
            ls = pygame.sprite.spritecollide(bullet, muros, False)
            for e in ls:
                blt_enemy.remove(bullet)
                elements.remove(bullet)

        for bullet in blt_enemy:
            ls = pygame.sprite.spritecollide(bullet, tierra, False)
            for e in ls:
                blt_enemy.remove(bullet)
                elements.remove(bullet)

        for bullet in blt_enemy:
            ls = pygame.sprite.spritecollide(bullet, players, False)
            for e in ls:
                blt_enemy.remove(bullet)
                elements.remove(bullet)
                jp.vida -= 20


        pantalla.fill(NEGRO)
        vida = str(jp.vida)
        pantalla.blit(background, [0, 64])
        if jp.vida > 200:
            life = pygame.image.load("img/hearth.png")
            pantalla.blit(life, [64, 0])
        if jp.vida > 100 :
            life = pygame.image.load("img/hearth.png")
            pantalla.blit(life, [32, 0])
        if jp.vida >=0:
            life = pygame.image.load("img/hearth.png")
            pantalla.blit(life, [0, 0])
        if(jp.vida <= 0):
            seguir = False
            victoria = False
        if (key_modifier == True) and (jp.rect.x >=22*32) and (jp.rect.x <=23*32) and (jp.rect.y >=17*32) and (jp.rect.y <=18*32):
            door.open = True
            victoria = True
            seguir = False
            reloj.tick(50)

        texto = fuente.render('Vida: ' + vida, True, BLANCO)
        pantalla.blit(texto, [100, 0])
        elements.update()
        elements.draw(pantalla)
        pygame.display.flip()

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
            texto = fuente.render('GAME OVER', True, BLANCO)
            pantalla.blit(texto, [250, 200])
            pygame.display.flip()
    else:
        continuar = True
        while continuar:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finjuego = True
                    continuar = False
                if event.type == pygame.KEYDOWN:
                    continuar = False

            pantalla.fill(NEGRO)
            txt = "Nivel 2"
            texto = fuente.render(txt, True, BLANCO)
            pantalla.blit(texto, [200, 200])
            pygame.display.flip()
        background = pygame.image.load('img/background.jpg')

        hero = pygame.image.load('img/character.png').convert_alpha()

        door_image = pygame.image.load('img/door.png').convert_alpha()

        d = []
        for fila in range(4):
          l_h= []
          for i in range(4):
            square = door_image.subsurface(0+(i*96), 0+(fila*96), 96, 96)
            print i*32, fila*96
            l_h.append(square)
          d.append(l_h)

        door = Door(d,[21.8*32, 16*32])


        m = []
        for fila in range(4):
          l_h= []
          for i in range(3):
            square = hero.subsurface(0+(i*32), 0+(fila*32), 32, 32)
            l_h.append(square)
          m.append(l_h)

        jp = Player(m,[100, 100])

        h = []
        for fila in range(4):
          l_h= []
          for i in range(3):
            square = hero.subsurface(98+(i*32), 0+(fila*32), 32, 32)
            l_h.append(square)
          h.append(l_h)

        enem = Enemy(h, [9*32, 8*32])

        b = []
        for fila in range(4):
          l_h= []
          for i in range(3):
            square = hero.subsurface((6*32)+(i*32), 0+(fila*32), 32, 32)
            l_h.append(square)
          b.append(l_h)

        enem_blue = Enemy2(b, [17*32, 10*32])

        enem_red = Enemy3('img/red-enemy.png', [23*32, 3*32])
        enem_white = Enemy3('img/white_enemy.png', [21*32, 7*32])
        elements = pygame.sprite.Group()
        muros = pygame.sprite.Group()
        tierra = pygame.sprite.Group()
        mapa = Nivel('mapaparcial.map', 'nivel2', 32, 32)
        for ls in mapa.mapa:
            pos_p = ls[0]
            x = pos_p[0]*32
            y = pos_p[1]*32
            pos_i = ls[1]
            xi = pos_i[0]
            yi = pos_i[1]
            # print ls[0], x, y
            m = Muro(mapa.fondo[xi][yi], [x, y])
            muros.add(m)
            elements.add(m)

        for ls in mapa.tierra:
            pos_p = ls[0]
            x = pos_p[0]*32
            y = pos_p[1]*32
            pos_i = ls[1]
            xi = pos_i[0]
            yi = pos_i[1]
            # print ls[0], x, y
            m = Muro(mapa.fondo[xi][yi], [x, y])
            tierra.add(m)
            elements.add(m)
        md1 = Modifiers('img/modifier1.png', 10*32, 9*32)
        key = Modifiers('img/key.png', 4*32, 12*32)
        blt = pygame.sprite.Group()
        blt_enemy = pygame.sprite.Group()
        players = pygame.sprite.Group()

        mdf = pygame.sprite.Group()
        enemys = pygame.sprite.Group()
        enemys_blue =  pygame.sprite.Group()
        enemys_static = pygame.sprite.Group()
        keys = pygame.sprite.Group()
        the_doors = pygame.sprite.Group()
        the_doors.add(door)
        elements.add(door)




        jp.tierra = tierra
        jp.muros = muros

        enem.tierra = tierra
        enem.muros = muros

        enem_blue.tierra = tierra
        enem_blue.muros = muros

        enemys_static.add(enem_red)
        enemys_static.add(enem_white)

        elements.add(enem_red)
        elements.add(enem_white)
        mdf.add(md1)
        keys.add(key)
        enemys.add(enem)
        enemys_blue.add(enem_blue)
        elements.add(enem)
        elements.add(enem_blue)
        elements.add(jp)
        elements.add(md1)
        elements.add(key)

        players.add(jp)
        flag = False
        e_modifier = False
        key_modifier = False

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
                    if event.key == pygame.K_RIGHT:
                        jp.dir = 2
                    if event.key == pygame.K_LEFT:
                        jp.dir = 1
                    if event.key == pygame.K_UP:
                        jp.dir = 3
                    if event.key == pygame.K_DOWN:
                        jp.dir = 0
                    if event.key == pygame.K_SPACE:
                        # sn_bullet.play()
                        if(e_modifier == True):
                            reloj.tick(10)
                            blt_jp = Bullet('img/bullet.gif', jp.rect.x+ 15, jp.rect.y +15, jp.dir)
                            blt_jp.tierra = tierra
                            elements.add(blt_jp)
                            blt.add(blt_jp)


            modifier_collide = pygame.sprite.spritecollide(jp, mdf, True)
            if(len(modifier_collide) > 0):
                e_modifier = True

            key_collide = pygame.sprite.spritecollide(jp, keys, True)
            if(len(key_collide) > 0):
                key_modifier = True


            for bullet in blt:
                ls = pygame.sprite.spritecollide(bullet, tierra, True)
                for e in ls:
                    blt.remove(bullet)
                    elements.remove(bullet)

            for bullet in blt:
                ls = pygame.sprite.spritecollide(bullet, muros, False)
                for e in ls:
                    blt.remove(bullet)
                    elements.remove(bullet)

            for bullet in blt_enemy:
                ls = pygame.sprite.spritecollide(bullet, the_doors, False)
                for e in ls:
                    blt.remove(bullet)
                    elements.remove(bullet)

            for bullet in blt:
                ls = pygame.sprite.spritecollide(bullet, enemys, True)
                for e in ls:
                    blt.remove(bullet)
                    elements.remove(bullet)

            for bullet in blt:
                ls = pygame.sprite.spritecollide(bullet, enemys_blue, True)
                for e in ls:
                    blt.remove(bullet)
                    elements.remove(bullet)

            for bullet in blt:
                ls = pygame.sprite.spritecollide(bullet, enemys_static, True)
                for e in ls:
                    blt.remove(bullet)
                    elements.remove(bullet)

            dead = pygame.sprite.spritecollide(jp, enemys, False)
            if len(dead) > 0:
                jp.vida = jp.vida - 5

            dead = pygame.sprite.spritecollide(jp, enemys_blue, False)
            if len(dead) > 0:
                jp.vida = jp.vida - 5

            if enem_red.cont % 13 == 0:
                blt_enem = BulletEnemy('img/fire.png', enem_red.rect.x+5, enem_red.rect.y+25, 0)
                blt_enemy.add(blt_enem)
                elements.add(blt_enem)

            if enem_white.cont % 13 == 0:
                blt_enem_white = BulletEnemy('img/fire.png', enem_white.rect.x-5, enem_white.rect.y, 1)
                blt_enemy.add(blt_enem_white)
                elements.add(blt_enem_white)

            if enem_blue.cont % 13 == 0:
                blt_enem_blue = BulletEnemy('img/fire.png', enem_blue.rect.x, enem_blue.rect.y, enem_blue.dir)
                blt_enemy.add(blt_enem_blue)
                elements.add(blt_enem_blue)

            for bullet in blt_enemy:
                ls = pygame.sprite.spritecollide(bullet, muros, False)
                for e in ls:
                    blt_enemy.remove(bullet)
                    elements.remove(bullet)

            for bullet in blt_enemy:
                ls = pygame.sprite.spritecollide(bullet, tierra, False)
                for e in ls:
                    blt_enemy.remove(bullet)
                    elements.remove(bullet)

            for bullet in blt_enemy:
                ls = pygame.sprite.spritecollide(bullet, players, False)
                for e in ls:
                    blt_enemy.remove(bullet)
                    elements.remove(bullet)
                    jp.vida -= 20


            pantalla.fill(NEGRO)
            vida = str(jp.vida)
            pantalla.blit(background, [0, 64])
            if jp.vida > 200:
                life = pygame.image.load("img/hearth.png")
                pantalla.blit(life, [64, 0])
            if jp.vida > 100 :
                life = pygame.image.load("img/hearth.png")
                pantalla.blit(life, [32, 0])
            if jp.vida >=0:
                life = pygame.image.load("img/hearth.png")
                pantalla.blit(life, [0, 0])
            if(jp.vida <= 0):
                seguir = False
                victoria = False
            if (key_modifier == True) and (jp.rect.x >=22*32) and (jp.rect.x <=23*32) and (jp.rect.y >=17*32) and (jp.rect.y <=18*32):
                door.open = True
                victoria = True
                seguir = False
                reloj.tick(50)

            texto = fuente.render('Vida: ' + vida, True, BLANCO)
            pantalla.blit(texto, [100, 0])
            elements.update()
            elements.draw(pantalla)
            pygame.display.flip()

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
                texto = fuente.render('GAME OVER', True, BLANCO)
                pantalla.blit(texto, [250, 200])
                pygame.display.flip()
        else:
            seguir = True
            while seguir:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        finjuego = True
                        seguir = False
                    if event.type == pygame.KEYDOWN:
                        seguir = False
                pantalla.fill(NEGRO)
                texto = fuente.render('YOU WIN', True, BLANCO)
                pantalla.blit(texto, [250, 200])
                pygame.display.flip()
