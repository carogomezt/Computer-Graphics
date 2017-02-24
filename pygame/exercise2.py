'''
    Ejercicio 2:
    1. Dibujar un poligono regular de n lados.
    2. Asignar a una tecla aumentar en escala 1 y a otra disminurie en scala de 1.
    3. Dibujar un cajon isometrico
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

def Poligono_Regular(r, angl, n):
    l_np = []
    for i in range(0, 361, angl):
        px = r * math.cos(math.radians(i))
        py = r * math.sin(math.radians(i))
        np = [px, py]
        l_np.append(Cartesiano(np))
    pygame.draw.polygon(pantalla, VERDE, l_np, 0)

def Isometrico(r, angl):
    px = r * math.cos(math.radians(angl))
    py = r * math.sin(math.radians(angl))
    np = [px, py]
    return Cartesiano(np)

def addVector(v1, v2):
    result = []
    for i in range(len(v1)):
        result.append(v1[i] + v2[i])
    return result

if __name__=='__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.set_caption('Ejemplo')
    fin = False
    #
    pantalla.fill(BLANCO)
    dibujar_plano()
    r = 100
    a = [0, -50]
    # n = 3
    # grad = 360/n
    # Poligono_Regular(r, grad, n)
    # pygame.display.flip()
    Punto(Cartesiano([0,0]))
    p1 = addVector( Isometrico(r, 45), a)
    p2 = addVector( Isometrico(r, 135), a)
    p3 = addVector( Isometrico(0, 90), a)
    pygame.draw.polygon(pantalla, VERDE, (Cartesiano([0,0]), Isometrico(r, 45), p1, p3, p2,  Isometrico(r, 135) ), 1)
    # Punto()
    pygame.display.flip()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    r = r+1
                if event.key == pygame.K_s:
                    r = r-1

            if event.type == pygame.QUIT:
                fin = True

        # pantalla.fill(BLANCO)
        # dibujar_plano()
        # Poligono_Regular(r, grad, n)
        # pygame.display.flip()
