import pygame

'''
    - algo de herencia
    
    - color, ancho, alto
    - hay cosas fijas como el color y el tamaño

    - metodo moverse: solo hacia arriba y hacia abajo
    - metodo de chocar: limite para no salirse de la win

    - metodo para interactuar con la pelota??
'''

class Paleta(pygame.Rect):
    _COLOR = (255, 255, 255)
    pass


class Pong:
    # Medidas del campo
    _ANCHO = 800
    _ALTO = 600
    _MARGEN_LATERAL = 10

    # Especificaciones de la paleta
    _ANCHO_PALETA = 10
    _ALTO_PALETA = _ALTO / 5

    # Especificaciones de la red
    net = pygame.Rect(_ANCHO/2-10, 5, 10, _ALTO-10)    
    _NET_COLOR = (255, 0, 0)    

    # Color del fondo
    _BACKGROUND_COLOR = (0, 255, 0)

    def __init__(self):        
        pygame.init()

        self.win = pygame.display.set_mode((self._ANCHO, self._ALTO), 0, 0)

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

    def draw(self):

        self.win.fill(self._BACKGROUND_COLOR)
        pygame.draw.rect(self.win, Paleta._COLOR , self.jugador1)
        pygame.draw.rect(self.win, Paleta._COLOR, self.jugador2)
        for i in range(10, self.net.height, self.net.height//2):
            if i % 2 == 1:
                continue
        pygame.draw.rect(self.win, self._NET_COLOR, self.net, 0, 10)


        pygame.display.update()        

    def bucle_principal(self):        
        exit_game = False        
        while not exit_game:
            eventos = pygame.event.get()
            for i in eventos:
                if i.type == pygame.QUIT:
                    exit_game = True
            
            self.draw()           

if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal() 

        