'''
    Ejercicio 1:
    1. Dibujar triangulo.
    2. Posicionar el triangulo en el plano cartesiano.
    3. Implementar matriz de rotacion.
    4. Rotar el triangulo  30, 45, 90, 135, 180 (al pulsar la tecla)
    5. Rotar el triangulo de 0 a360 incrementando 15 al pulsar cada tecla

'''

import pygame
import math
import time

ANCHO = 600
ALTO = 400
ROJO = [255, 0, 0]
VERDE = [0, 255, 0]
AZUL = [0, 0, 255]
BLANCO = [255, 255, 255]
C = [ANCHO/2, ALTO/2]

def dibujar_plano():
    pi= [0, C[1]]
    pf= [ANCHO, C[1]]
    pygame.draw.line(pantalla, AZUL,pi,pf)

    pi= [C[0], 0]
    pf= [C[0], ALTO]
    pygame.draw.line(pantalla, AZUL, pi,pf)

def Punto(p, r=1):
    pygame.draw.circle(pantalla, ROJO,p, r)

def Vec_Escalar(p, k):
    vr =[p[0]*k, p[1]*k]
    return vr

def Cartesiano(p):
    #Transformacion
    np = [C[0]+p[0], C[1]-p[1]]
    return np

# Dibuja un triangulo
def Triangulo(p):
    pygame.draw.polygon(pantalla, VERDE, (p[0], p[1], p[2]))

# Dibuja un triangulo y lo situa en el plano
def Triangulo_Plano(p):
    pygame.draw.polygon(pantalla, VERDE, (Cartesiano(p[0]),Cartesiano(p[1]),Cartesiano(p[2])))

def Escalamiento(k, p):
    n_point = []
    for i in p:
        np = [i[0]*k[0], i[1]*k[1]]
        n_point.append(np)
    return n_point

def Rotacion (a, points):
    n_point = []
    for elem in points:
        px = (elem[0] * math.cos(math.radians(a))) + (elem[1] * math.sin(math.radians(a)))
        py = (-elem[0] * math.sin(math.radians(a))) + (elem[1] * math.cos(math.radians(a)))
        np = [px, py]
        n_point.append(np)
    return n_point


if __name__=='__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.set_caption('Ejemplo')
    fin = False

    pantalla.fill(BLANCO)
    dibujar_plano()
    #Punto(Cartesiano([20, 30]), 2)
    triangulo = [[0.0, 0.0], [0.0, 100.0], [100.0, 100.0]]
    Triangulo_Plano(triangulo)
    l = [30, 45, 90, 135, 180]
    cont = 0
    reloj = pygame.time.Clock()
    flag = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if(cont < len(l)):
                        triangulo = Rotacion(l[cont], triangulo)
                        cont = cont + 1
                    else:
                        cont = 0
                    flag = True

                if event.key == pygame.K_s:
                    for i in range(0, 360, 15):
                        triangulo = Rotacion(i, triangulo)
                        pantalla.fill(BLANCO)
                        dibujar_plano()
                        Triangulo_Plano(triangulo)
                        # Punto(p)
                        pygame.display.flip()
                        reloj.tick(10)
                #print 'tecla'
            if event.type == pygame.QUIT:
                fin = True
        if(flag):
            pantalla.fill(BLANCO)
            dibujar_plano()
            Triangulo_Plano(triangulo)
            # Punto(p)
            pygame.display.flip()
