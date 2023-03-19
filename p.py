import pygame
from ClassBall import Ball
import cv2
import numpy as np
import random

def InicioJuego(balls, screen):
    # Actualizar y dibujar las bolas
    for ball in balls:
        ball.update()
        ball.draw(screen)

        # Si la bola se sale de la pantalla, reubicarla en la parte superior
        if ball.y > screen_height + ball.radius:
            print("salió")
            ball.x = random.randint(0, screen_width)
            ball.y = -150
            
# Inicializar Pygame
pygame.init()

# Definir la resolución de la ventana
screen_width, screen_height = 640, 480

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Cargar el clasificador de rostros
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Crear una ventana de Pygame
screen = pygame.display.set_mode((screen_width, screen_height))


# Crear una lista para almacenar los objetos Ball
balls = []

# Agregar algunas bolas a la lista
for i in range(1):
    x = random.randint(0, screen_width)
    y = -150
    ball = Ball(x, y)
    balls.append(ball)

while True:
    
    # Obtener un fotograma de la cámara
    ret, frame = cap.read()

    # Detectar rostros en el fotograma
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Si se detecta al menos un rostro, dibujar un rectángulo alrededor del primero
    if len(faces) > 0:
        (x,y,w,h) = faces[0]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        
    # Convertir el fotograma a un formato compatible con Pygame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)

    # Mostrar el fotograma en el fondo de la ventana
    screen.blit(frame, (0, 0))

    print(w)
    
    InicioJuego(balls, screen)

    # Actualizar la ventana de Pygame
    pygame.display.update()

    # Esperar a que el usuario presione una tecla para salir
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                cap.release()
                pygame.quit()
                quit()

