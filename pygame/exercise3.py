'''
    Ejercicio 2:
    1.Graficar Y=3x+2 para [-200][200]
    2. Ver en pantalla Y = 3x+2
    3. Graficar coordenadas polares
    4. Dibujar la cicloide

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

def Polares(a, n):
    l_np = []
    for l in range(0, 361):
        r = a * math.cos(math.radians(n * l))
        x = r * math.cos(math.radians(l))
        y = r * math.sin(math.radians(l))
        np = [x, y]
        l_np.append(Cartesiano(np))
    return l_np

if __name__=='__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.set_caption('Ejemplo')
    fin = False
    #
    pantalla.fill(BLANCO)
    dibujar_plano()

    #  Primer punto
    # for x in range(-200, 200):
    #     Punto(Cartesiano([x, 3*x+2]))
    #
    # pygame.display.flip()
    #Polares(100, 4)
    pygame.display.flip()
    reloj =pygame.time.Clock()
    var_x = 1
    var_y = 1
    cont = 0
    pt = Polares(100, 4)
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pass

            if event.type == pygame.QUIT:
                fin = True

        #  Punto 2
        # pantalla.fill(BLANCO)
        dibujar_plano()
        # Polares(100)
        # x= -200+ var_x
        # y = -602
        # var_x += 1
        # if(x <= 200):
        #     Punto(Cartesiano([x, 3*x +2]))
        # else:
        #     break
        #
        # pygame.display.flip()
        # reloj.tick(60)

        # Punto 3
        n = [int(pt[cont][0]), int(pt[cont][1])]
        Punto(n)
        reloj.tick(60)
        cont +=1

        pygame.display.flip()
