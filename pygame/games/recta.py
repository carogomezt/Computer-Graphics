import pygame
import json
ANCHO=800
ALTO=600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

def Traer_fondo(archivo, an_re, al_re):
  imagen = pygame.image.load(archivo)
  ancho, alto = imagen.get_size()
  print ancho, alto
  an_re = 32
  al_re = 32

  tabla = []

  for var_y in range(0, alto/al_re):
    #fila = []
    for var_x in range(0, ancho/an_re):
      cuadro = (0 + (var_x*an_re), 0 + (var_y*al_re), an_re, al_re)
      img_cuadro = imagen.subsurface(cuadro)
      tabla.append(img_cuadro)
    #tabla.append(fila)
  return tabla

if __name__ == '__main__':
    pygame.init()
    pantalla= pygame.display.set_mode([ANCHO, ALTO]) 
    with open('img-maze/mapa.json') as js_archivo:
        doc = json.load(js_archivo)

    print 'altura: ', doc['height']
    print 'ancho: ', doc['width']

    origen =''
    c_an = ''
    c_al = ''

    for valor in doc['tilesets']:
        #print valor
        origen = (valor['image'])
        c_an = valor['tilewidth']
        c_al = valor['tileheight']

    print origen, c_an, c_al
    img_fondo = Traer_fondo(origen, c_an, c_al)

    for valor in doc['layers']:
        dato =  valor['data']
        i = 0
        y = 0
        for iv in dato:            
            pantalla.blit(img_fondo[iv-1], [0+ (i * 32),0 + (y *32)])
            if i <= 40:
                i += 1
            else:
                i = 0
                y += 1


    

    #    pantalla.blit(img_fondo[20], [100, 100])
    pygame.display.flip()

    fin = False
    reloj = pygame.time.Clock()
    while not fin:
        #Captura de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True