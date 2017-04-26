import pygame
import random
import ConfigParser
import math

'''
    Buscar DDA
'''

ANCHO=640
ALTO=480
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

class Jugador(pygame.sprite.Sprite):
  def __init__(self, pos):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface([50, 30])
    self.image.fill(VERDE)
    self.rect = self.image.get_rect()
    self.rect.x = pos[0]
    self.rect.y = pos[1]




if __name__ == '__main__':
    pygame.init()
    pantalla= pygame.display.set_mode([ANCHO, ALTO])

    fuente = pygame.font.Font(None, 32)
    texto = fuente.render("Mensaje", True, BLANCO)
    todos = pygame.sprite.Group()
    jp = Jugador([100, 100])
    todos.add(jp)



    fin = False
    reloj = pygame.time.Clock()
    continuar = True
    pag = 0
    while continuar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
                continuar = False
            if event.type == pygame.KEYDOWN:
                pag+=1
                if pag > 2:
                    continuar = False

        if pag == 1:
            txt = "Habia una vez..."
            texto = fuente.render(txt, True, BLANCO)
            pantalla.blit(texto, [200, 200])
            pygame.display.flip()
        if pag == 2:
            txt = "En un futuro muy cercano..."
            texto = fuente.render(txt, True, BLANCO)
            pantalla.blit(texto, [200, 50])
            img_info = pygame.image.load('bosque.jpg')
            img_info = pygame.transform.scale(img_info,(500, 200))
            pantalla.blit(img_info, [20, 80])
            pygame.display.flip()
        reloj.tick(60)

    #Codigo del juego
    #Nivel 1
    #Cargar info mapa
    fondo = pygame.image.load("background.jpg")
    victoria = False
    seguir = True
    while seguir and not fin:
        #Captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
                seguir = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    victoria = True
                if event.key == pygame.K_a:
                    victoria = False
                seguir = False
        txt = "Informacion"
        pantalla.blit(fondo, [0, 0])
        todos.draw(pantalla)
        texto = fuente.render(txt, True, BLANCO)
        pantalla.blit(texto, [20, 450])
        pygame.display.flip()
        reloj.tick(60)

    if not victoria:
        seguir = True
        while seguir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin = True
                    seguir = False
                if event.type == pygame.KEYDOWN:
                    seguir = False
            pantalla.fill(NEGRO)
            txt = "Fin del juego"
            texto = fuente.render(txt, True, BLANCO)
            pantalla.blit(texto, [200, 200])
            pygame.display.flip()
    else:
        continuar = True
        while continuar:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin = True
                    continuar = False
                if event.type == pygame.KEYDOWN:
                    pag+=1
                    if pag > 2:
                        continuar = False

            pantalla.fill(NEGRO)
            txt = "Nivel 2"
            texto = fuente.render(txt, True, BLANCO)
            pantalla.blit(texto, [200, 200])
            pygame.display.flip()


        #Codigo del juego
        #Nivel 2
        #Cargar info mapa
        fondo = pygame.image.load("bosque.jpg")
        if victoria:
            victoria = False
            seguir = True
        while seguir and not fin:
            #Captura de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin = True
                    seguir = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        victoria = True
                    if event.key == pygame.K_a:
                        victoria = False
                    seguir = False
            txt = "Informacion"
            pantalla.blit(fondo, [0, 0])
            todos.draw(pantalla)
            texto = fuente.render(txt, True, BLANCO)
            pantalla.blit(texto, [20, 450])
            pygame.display.flip()
            reloj.tick(60)
