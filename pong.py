import pygame
from random import randint

# Especificaciones de la paleta

WIDTH_PADDLE = 15
HEIGTH_PADDLE = 100

# Medidas del campo

WIDTH = 700
HEIGHT = 500
MARGEN_LATERAL = 10

# Especificaciones de la Pelota

BALL_SIZE = 15

'''
    - algo de herencia
    
    - color, ancho, alto
    - hay cosas fijas como el color y el tamaño

    - metodo moverse: solo hacia arriba y hacia abajo
    - metodo de chocar: limite para no salirse de la win

    - metodo para interactuar con la pelota??
'''

class Paddle(pygame.Rect): 
    _COLOR = (255, 255, 255)

    UP = True
    DOWN = False

    def __init__(self, x, y):
        super(Paddle, self).__init__(x , y, WIDTH_PADDLE, HEIGTH_PADDLE)
        self.speed = 5

    def move_paddle(self, direction):
        if direction == self.UP:
            self.y = self.y - self.speed
            if self.y < 0:
                self.y = 0
        else:
            self.y = self.y + self.speed
            if self.y > HEIGHT - HEIGTH_PADDLE:
                self.y = HEIGHT - HEIGTH_PADDLE
    
class Ball(pygame.Rect):
    BALL_COLOR = (0, 0, 255)

    def __init__(self):
        super(Ball, self).__init__((WIDTH -BALL_SIZE)/2, (HEIGHT-BALL_SIZE)/2,
                BALL_SIZE, BALL_SIZE)
        self.speed_x = randint(-5, 5)
        self.speed_y = randint(-5, 5)

    def ball_move(self):
        self.y = self.y + self.speed_y
        self.x = self.x + self.speed_x
 
class Pong:

    # Especificaciones de la red        
    _NET_COLOR = (255, 0, 0)    

    # Color del fondo
    _BACKGROUND_COLOR = (0, 255, 0)

    def __init__(self):        
        pygame.init()

        self.win = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Pong')

        self.player1 = Paddle(
            MARGEN_LATERAL,               # coordenada x (left)
            (HEIGHT - HEIGTH_PADDLE)/2)       # coordenada y (top)
                             

        self.player2 = Paddle(
            WIDTH - WIDTH_PADDLE - MARGEN_LATERAL,
            (HEIGHT - HEIGTH_PADDLE )/2)

        self.ball = Ball()
        

    def draw(self):

        self.win.fill(self._BACKGROUND_COLOR)
        pygame.draw.rect(self.win, Paddle._COLOR , self.player1, 0, 10)
        pygame.draw.rect(self.win, Paddle._COLOR, self.player2, 0, 10)
        for i in range(10, HEIGHT, HEIGHT//10):
            if i % 2 == 1:
                continue
            pygame.draw.rect(self.win, self._NET_COLOR, (WIDTH//2 - 5, i, 5, HEIGHT//20), 0, 10)
        
        pygame.draw.rect(self.win, Ball.BALL_COLOR, self.ball, 0, 10)

        pygame.display.update()        
        self.clock.tick(60)
    # BUCLE PRINCIPAL DEL JUEGO

    def main_cicle(self):        
        exit_game = False        
        while not exit_game:            
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit_game = True
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_ESCAPE:
                        exit_game = True
                    
            key_state = pygame.key.get_pressed()
            if key_state[pygame.K_a]:
                self.player1.move_paddle(Paddle.UP)
            if key_state[pygame.K_z]:
                self.player1.move_paddle(Paddle.DOWN)
            if key_state[pygame.K_UP]:
                self.player2.move_paddle(Paddle.UP)
            if key_state[pygame.K_DOWN]:
                self.player2.move_paddle(Paddle.DOWN)
            
            self.ball.ball_move()
 
            self.draw()           

if __name__ == "__main__":
    game = Pong()
    game.main_cicle() 

        