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
    self.speed = 2

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

  def update(self):
    if (self.rect.x >= 17*32) and (self.rect.x <= 23*32) and (self.rect.y == 10*32):
        self.dir = 2
        self.rect.x += self.speed
    if(self.rect.x == (23*32) and (self.rect.y >= 10*32) and (self.rect.y <= 16*32)):
        self.dir = 0
        self.rect.y += self.speed
    if (self.rect.x >= 20*32) and (self.rect.x <= 23*32) and (self.rect.y == 16*32):
        self.dir = 1
        self.rect.x -= self.speed
    if(self.rect.x == (20*32) and (self.rect.y >= 16*32) and (self.rect.y <= 18*32)):
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


class Bullet(pygame.sprite.Sprite):
    def __init__(self, archivo, posx, posy, dire):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.dir = dire
        self.var_y = 5
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
    def __init__(self, ar_mapa, an_re, al_re):
      pygame.sprite.Sprite.__init__(self)
      self.mapa = self.Ret_mapa(ar_mapa)
      self.fondo = self.Traer_fondo(self.ar_fondo, an_re, al_re)
      self.tierra = self.Ret_tierra(ar_mapa)

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

    def Ret_mapa(self, archivo):
      archivo = 'mapaparcial.map'
      mapa = ConfigParser.ConfigParser()
      mapa.read(archivo)
      self.ar_fondo=  mapa.get('nivel1', 'origen')
      plano = mapa.get('nivel1', 'mapa').split('\n')
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

    def Ret_tierra(self, archivo):
        archivo = 'mapaparcial.map'
        mapa = ConfigParser.ConfigParser()
        mapa.read(archivo)
        self.ar_fondo=  mapa.get('nivel1', 'origen')
        plano = mapa.get('nivel1', 'mapa').split('\n')
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

    hero = pygame.image.load('img/character.png').convert_alpha()

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

    elements = pygame.sprite.Group()
    blt = pygame.sprite.Group()
    mdf = pygame.sprite.Group()
    enemys = pygame.sprite.Group()
    enemys_blue =  pygame.sprite.Group()
    enemys_red = pygame.sprite.Group()


    md1 = Modifiers('img/modifier1.png', 10*32, 9*32)

    muros = pygame.sprite.Group()
    tierra = pygame.sprite.Group()
    mapa = Nivel('mapaparcial.map', 32, 32)
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

    elements.add(enem_red)
    mdf.add(md1)
    enemys.add(enem)
    enemys_blue.add(enem_blue)
    elements.add(enem)
    elements.add(enem_blue)
    elements.add(jp)
    elements.add(md1)

    fin = False
    reloj = pygame.time.Clock()
    fuente = pygame.font.Font(None, 30)
    flag = False
    e_modifier = False
    finjuego = False

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

        dead = pygame.sprite.spritecollide(jp, enemys, False)
        if len(dead) > 0:
            jp.vida = jp.vida - 100
            jp.rect.x = 100
            jp.rect.y = 100

        dead = pygame.sprite.spritecollide(jp, enemys_blue, False)
        if len(dead) > 0:
            jp.vida = jp.vida - 100
            jp.rect.x = 100
            jp.rect.y = 100


        if finjuego:
            pantalla.fill(NEGRO)
            texto = fuente.render('GAME OVER', True, BLANCO)
            pantalla.blit(texto, [250, 200])
            pygame.display.flip()

        else:
            pantalla.fill(NEGRO)
            vida = str(jp.vida)
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
                finjuego = True
            texto = fuente.render('Vida: ' + vida, True, BLANCO)
            pantalla.blit(texto, [100, 0])

            elements.update()
            elements.draw(pantalla)
            pygame.display.flip()
            
            blt_enem = Bullet('img/fire.png', enem_red.rect.x-20, enem_red.rect.y+50, 0)
            blt.add(blt_enem)
            elements.add(blt_enem)
            reloj.tick(20)
