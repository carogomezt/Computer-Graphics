import pygame
import random
import ConfigParser



ANCHO=800
ALTO=600
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
    self.muros = []
    self.vida = 100

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

    #colision
    lcol = pygame.sprite.spritecollide(self, muros, False)
    for e in lcol:
        self.vida -= 1
        if self.dir == 2:
            self.rect.right = e.rect.left
        if self.dir == 1:
            self.rect.left = e.rect.right
        if self.dir == 0:
            self.rect.bottom = e.rect.top
        if self.dir == 3:
            self.rect.top = e.rect.bottom

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

    def Traer_fondo(self, archivo, an_re, al_re):
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

    def Ret_mapa(self, archivo):
      archivo = 'mapa.map'
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

    muros = pygame.sprite.Group()
    mapa = Nivel('mapa.map', 32, 32)
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
        todos.add(m)

    jp.muros = muros
    todos.add(jp)
    fondo = pygame.image.load('img-maze/fondo.jpg')
    fuente = pygame.font.Font(None, 30)


    fin = False
    reloj = pygame.time.Clock()
    i = 0
    puntos = 0
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

        if finjuego:
            pantalla.fill(NEGRO)
            texto = fuente.render('GAME OVER', True, BLANCO)
            pantalla.blit(texto, [250, 200])
            pygame.display.flip()

        else:
            pantalla.fill(NEGRO)
            vida = str(jp.vida)
            if(jp.vida <= 0):
                finjuego = True
            texto = fuente.render('Vida: ' + vida, True, NEGRO)
            pantalla.blit(fondo, [0, 0])
            pantalla.blit(texto, [20, 435])
            todos.update()
            todos.draw(pantalla)
            pygame.display.flip()
            reloj.tick(20)
