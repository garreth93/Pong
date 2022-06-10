import pygame

'''
    - algo de herencia
    
    - color, ancho, alto
    - hay cosas fijas como el color y el tamaño

    - metodo moverse: solo hacia arriba y hacia abajo
    - metodo de chocar: limite para no salirse de la pantalla

    - metodo para interactuar con la pelota??
'''

class Paleta(pygame.Rect):
    _COLOR = (255, 255, 255)
    pass


class Pong:

    _ANCHO = 800
    _ALTO = 600
    _MARGEN_LATERAL = 10

    _ANCHO_PALETA = 5
    _ALTO_PALETA = _ALTO / 5

    red = pygame.Rect(_ANCHO/2-1, 0, 3, _ALTO)
    _RED_COLOR = (255, 0, 0)

    def __init__(self):
        print('Construyendo un objeto pong')
        pygame.init()

        self.pantalla = pygame.display.set_mode((self._ANCHO, self._ALTO))

        self.jugador1 = Paleta(
            self._MARGEN_LATERAL,               # coordenada x (left)
            (self._ALTO-self._ALTO_PALETA)/2,   # coordenada y (top)
            self._ANCHO_PALETA,                 # ancho (width)
            self._ALTO_PALETA)                  # alto (height)

        self.jugador2 = Paleta(
            self._ANCHO - self._ANCHO_PALETA - self._MARGEN_LATERAL,
            (self._ALTO-self._ALTO_PALETA)/2,
            self._ANCHO_PALETA,
            self._ALTO_PALETA)



    def bucle_principal(self):
        print('Estoy en el bucle principal')        
        while True:
            pygame.draw.rect(self.pantalla, Paleta._COLOR , self.jugador1)
            pygame.draw.rect(self.pantalla, Paleta._COLOR, self.jugador2)
            pygame.draw.rect(self.pantalla, self._RED_COLOR, self.red)
            pygame.display.flip()

if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal() 

        