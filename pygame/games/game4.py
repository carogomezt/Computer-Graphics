import pygame
import random

'''
    objetos moviendose
    para la proxima clase traer:
    sprite de nave jugador, enemiga, balas y sonido cuando dispara el jugador, cuando dispara el enemigo, cuando explota la nave
'''

ANCHO=640
ALTO=480
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

class Bloque(pygame.sprite.Sprite):
    def __init__(self, archivo_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, archivo_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.vel = 5
        self.flag = True 

    def update(self):
        if(self.rect.x >= (ANCHO-self.rect.width)):
            self.flag = False
            self.vel += 1
            self.rect.y += self.vel

        if(self.rect.x < 0):
            self.flag = True
            self.rect.y += self.vel

        if(self.flag):
            self.rect.x += self.vel

        if(not self.flag):
            self.rect.x -= self.vel
    
            


if __name__ == '__main__':
    pygame.init()
    pantalla= pygame.display.set_mode([ANCHO, ALTO])

    todos =pygame.sprite.Group()
    enemigos = pygame.sprite.Group()

    jugador = Bloque('bear.png')
    todos.add(jugador)
    

    for i in range(2):
        b = Enemigo('star.gif')
        b.rect.x = random.randint(10, 600)
        b.rect.y = random.randint(0, 450)
        enemigos.add(b)
        todos.add(b)

    fin = False
    puntos = 0
    reloj = pygame.time.Clock()
    while not fin:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

        jugador.rect.x = pos[0]
        jugador.rect.y = pos[1]
        #lsita de tocados
        ls_t = pygame.sprite.spritecollide(jugador, enemigos, True)
        for i in ls_t:
            puntos += 1
            print puntos
           
        pantalla.fill(BLANCO)
        todos.update()
        reloj.tick(20)
        todos.draw(pantalla)
        pygame.display.flip()