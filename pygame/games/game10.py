import pygame

ANCHO=640
ALTO=480
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

class Jugador(pygame.sprite.Sprite):
    def __init__(self, alto, ancho):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.varx = 2
        self.vary = 0
        self.saltar = 1
        self.velocidad = 5
        self.xf = 0
        self.an_img = 0

    def Salto(self):
        if self.saltar == 0:
            self.vary =- 10

    def Derecha(self):
        self.varx =+ self.velocidad

    def Izquierda(self):
        self.varx = -self.velocidad

    def gravedad(self):
        if(self.vary == 0):
            self.vary = 1
        else:
            self.vary += 0.35

        piso = ALTO - self.rect.height
        if self.rect.y >= piso and self.vary >= 0:
            self.vary = 0
            self.rect.y = piso
            self.saltar = 0

    def update(self):
        self.gravedad()
        if self.rect.x >= ANCHO - 80 and self.varx > 0:
            self.rect.x = ANCHO - 80
            self.xf -= 2
            print xf
            #-1280 = anchoimg-anchoventana
            lim = (self.an_img - ANCHO) *(-1)
            if self. xf < lim:
                self.xf = lim
        elif self.rect.x <= 60 and self.varx < 0:
            self.rect.x = 60
            self.xf += 2
            if self.xf > 0:
                self.xf = 0
        else:
            self.rect.x += self.varx
        self.rect.y += self.vary

if __name__ == '__main__':
    pygame.init()
    pantalla= pygame.display.set_mode([ANCHO, ALTO])
    fondo = pygame.image.load("background.jpg")
    an_img, al_img = fondo.get_size()

    todos = pygame.sprite.Group()
    jp = Jugador(50, 30)
    jp.an_img = an_img
    todos.add(jp)


    fin = False
    reloj = pygame.time.Clock()
    xf = 0
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

        xf = jp.xf
        pantalla.blit(fondo, [xf, -520])
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
