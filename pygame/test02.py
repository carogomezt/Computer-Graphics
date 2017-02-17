import pygame

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
def Triangulo(p):
    pygame.draw.polygon(pantalla, VERDE, (p[0], p[1], p[2]))

def Triangulo_Plano(p):
    pygame.draw.polygon(pantalla, VERDE, (Cartesiano(p[0]),Cartesiano(p[1]),Cartesiano(p[2])))

def Escalamiento(k, p):
    n_point = []
    for i in p:
        np = [i[0]*k[0], i[1]*k[1]]
        n_point.append(np)
    return n_point

if __name__=='__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.set_caption('Ejemplo')
    fin = False

    pantalla.fill(BLANCO)
    dibujar_plano()
    Punto(Cartesiano([20, 30]), 2)
    triangulo = [[0, 0], [0, 10], [10, 10]]

    puntos = Escalamiento([10,10], triangulo)
    t_car = []
    for punto in puntos:
        np = Cartesiano(punto)
        t_car.append(np)
    Triangulo(t_car)
    pygame.display.flip()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True