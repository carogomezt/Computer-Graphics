import pygame
import math

ANCHO = 600
ALTO = 600
ROJO = [255, 0, 0]
VERDE = [0, 255, 0]
AZUL = [0, 0, 255]
BLANCO = [255, 255, 255]

class Cartesiano():
    def __init__(self, pan, centro):
        self.c = centro
        self.pan = pan
        self.Ejes()

    def Ejes(self):
        pygame.draw.line(self.pan, ROJO, [self.c[0], 0], [self.c[0], ALTO], 1)
        pygame.draw.line(self.pan, ROJO, [0, self.c[1]], [ANCHO, self.c[1]], 1)

    def Tras(self, p):
        xp = self.c[0] + p[0]
        yp = self.c[1] - p[1]
        return [xp, yp]

    def Puntico(self, p):
        pygame.draw.circle(self.pan, AZUL, p, 2)

    def Puntico2(self, p):
        pygame.draw.circle(self.pan, ROJO, p, 2)

    def Punto(self, p):
        pygame.draw.circle(self.pan, AZUL, self.Tras(p), 2)

    def Linea(self, p, q):
        pygame.draw.line(self.pan, AZUL, self.Tras(p), self.Tras(q), 1)

    def Poligono(self, l):
        lc=[]
        for elemento in l:
            p = self.Tras(elemento)
            lc.append(p)
        pygame.draw.polygon(self.pan, AZUL, lc, 1)

    def Circulo(self, l):
        for i in range(180, 360):
            px = l * math.cos(math.radians(i)) + l
            py = l * math.sin(math.radians(i))
            p = [int(px), int(py)]
            pygame.draw.circle(self.pan, AZUL, self.Tras(p), 1)


class Vector():
    def __init__(self, p):
        self.p = p
        self.r = math.sqrt((self.p[0]**2)+ (self.p[1]**2))
        self.ang = 0

    def NuevaPos(self):
        a = math.radians(self.ang)
        x = self.r * math.cos(a)
        y = self.r * math.sin(a)
        self.p = [int(x), int(y)]

    def Subir(self):
        self.ang +=10
        self.NuevaPos()

    def Bajar(self):
        self.ang -=10
        self.NuevaPos()

    def Evento(self, e):
        if e.key == pygame.K_UP:
            self.Subir()

        if e.key == pygame.K_DOWN:
            self.Bajar()

    def AnguloPunto(self, l, angl):
        px = l * math.cos(math.radians(angl))
        py = l * math.sin(math.radians(angl))
        return [px, py]
