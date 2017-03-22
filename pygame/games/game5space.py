import pygame
import random



ANCHO=600
ALTO=800
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = ALTO-self.rect.height
        self.dire = 1

    def direccion(self, dire):
        self.dire = dire

    def update(self):

        if( (self.dire == 1) and (self.rect.x < (ANCHO-self.rect.width))):
            self.rect.x += 3
        if ((self.dire == 0) and self.rect.x > 0):
            self.rect.x -= 3

class Enemy(pygame.sprite.Sprite):
    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.vel = 4
        self.flag = 1
        self.contador = random.randint(0, 400)
        self.shot = 0

    def update(self):
        if(self.rect.x >= (ANCHO-self.rect.width)):
            self.flag = 0
            self.vel += 1
            self.rect.y += self.vel

        if(self.rect.x < 0):
            self.flag = 1
            self.rect.y += self.vel

        if(self.flag == 1):
            self.rect.x += self.vel

        if(self.flag == 0):
            self.rect.x -= self.vel

        self.contador -= 1

        if self.contador == 0:
            self.shot = 1

class Bullet(pygame.sprite.Sprite):
    def __init__(self, archivo, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.var_y = 5

    def update(self):
        self.rect.y -= self.var_y


if __name__ == '__main__':
    pygame.init()
    pantalla= pygame.display.set_mode([ANCHO, ALTO])

    #groups

    allPlayers = pygame.sprite.Group()
    enemy = pygame.sprite.Group()
    b_enem = pygame.sprite.Group()
    b_play = pygame.sprite.Group()

    #variables: init
    fondo = pygame.image.load('images-space/background.jpg')
    ply = Player('images-space/spaceship.png')
    allPlayers.add(ply)
    sn_bullet = pygame.mixer.Sound('bulletsound.wav')

    for i in range(5):
        enm = Enemy('images-space/spaceshipenemy.png')
        enm.rect.x = random.randint(10, 600)
        enemy.add(enm)
        allPlayers.add(enm)

    fin = False
    reloj = pygame.time.Clock()
    while not fin:
        #Captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ply.direccion(1)
                if event.key == pygame.K_LEFT:
                    ply.direccion(0)
                if event.key == pygame.K_SPACE:
                    sn_bullet.play()
                    blt_ply = Bullet('images-space/moonball.png', ply.rect.x + 20, ply.rect.y)
                    allPlayers.add(blt_ply)
                    b_play.add(blt_ply)

        '''
            Hacer que los enemigos disparen
        '''

        for bullet in b_play:
            ls = pygame.sprite.spritecollide(bullet, enemy, True)
            for e in ls:
                b_play.remove(bullet)
                allPlayers.remove(bullet)

        pantalla.blit(fondo, [0, 0])
        allPlayers.update()
        allPlayers.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
