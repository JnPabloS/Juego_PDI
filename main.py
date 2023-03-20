from ClassBall import Ball
import random
import time

from ProcessImages import *
from window import *

def Col(points):
      
    if(IntersectionMasks(frame, faces, ball)):
        #Mostrar el puntaje
        points = points + 1

        ball.vy = -random.randint(25, 40)
        ball.vx = random.randint(-9, 9)
        
        rebote.play()
        
    return points
        
# Inicializar Pygame
pygame.init()

# Definir la resolución de la ventana
ANCHO = 640
ALTO = 480
screen_width, screen_height = ANCHO, ALTO

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Crear una ventana de Pygame
startScreen = pygame.display.set_mode((screen_width, screen_height))
screen = pygame.display.set_mode((screen_width, screen_height))

# Agregar la bola
x = random.randint(100, 500)
y = -150
ball = Ball(x, y)

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)

pygame.init()

# Crear una ventana
pygame.display.set_caption("Inicio")

# Crear un objeto Font
fuente = pygame.font.SysFont(None, 50)

# Crear un rectángulo para el botón de "start"
boton_rect = pygame.Rect(ANCHO/2 - 100, ALTO/2 - 50, 200, 100)
jugando = False  # Variable de estado para indicar si se está jugando o no

#sonidos
start = pygame.mixer.Sound('start.mp3')
rebote = pygame.mixer.Sound('rebote.mp3')

logo = pygame.image.load('logo.png') #logo

#contador de puntos
points = 0

while True:
    
    # Obtener eventos
    for evento in pygame.event.get():
    # Salir del programa si se cierra la ventana
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Detectar si se hace clic en el botón
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_rect.collidepoint(evento.pos):
                start.play()
                count = 0
                tiempo = 15
                tiempo_inicial = time.time()
                tiempo_finalizacion = tiempo_inicial + tiempo
                jugando = True
                pygame.display.set_caption("Yellow Ball")

        ShowStart(logo, startScreen, boton_rect, fuente, AZUL, BLANCO)

    #Pabloooooooo aquiiiiiii 
    if jugando == True:
        # Obtener un fotograma de la cámara
        ret, frame = cap.read()
    
        # Mostrar tiempo y puntaje en pantalla
        ShowText(screen, BLANCO, ball, tiempo_finalizacion, points)
        
        # Identifica objetos de color amarillo
        faces = BuscarColor(frame)

        
        # Poner la imagen de la cámara en el fondo de la ventana
        SetBackground(frame, screen)
        
        # Actualizar la ventana
        UpdateWindow(ball, screen, screen_height)
        
        # Actualizar los puntos
        points = Col(points)


        # Esperar a que el usuario presione una tecla para salir
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    cap.release()
                    pygame.quit()
                    quit()