import pygame
import random
import ConfigParser



ANCHO=600
ALTO=400
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

if __name__ == '__main__':
    pygame.init()
    pantalla= pygame.display.set_mode([ANCHO, ALTO])

    fr_cont = 0
    tasa = 60
    t_ini = 10
    fuente = pygame.font.Font(None, 32)
    col = BLANCO
  


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

        total_seg = fr_cont // tasa
        minutos = total_seg // 60
        segundos = total_seg % 60
        pantalla.fill(NEGRO)
        txt_tiempo = 'tiempo:  {0:02}: {1:02}'.format(minutos, segundos)
        texto = fuente.render(txt_tiempo, True, BLANCO)
        pantalla.blit(texto, [100, 100])


        total_seg = t_ini - (fr_cont // tasa)
        if(total_seg < 0):
        	total_seg = 0

        if total_seg < 5:
        	col = ROJO
        minutos = total_seg // 60
        segundos = total_seg % 60
        txt_tiempo = 'tiempo:  {0:02}: {1:02}'.format(minutos, segundos)
        texto = fuente.render(txt_tiempo, True, col)
        pantalla.blit(texto, [100, 200])

        pygame.display.flip()
        reloj.tick(tasa) 
        fr_cont +=1

