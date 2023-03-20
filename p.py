import pygame
from ClassBall import Ball
import cv2
import numpy as np
import random

def InicioJuego():
    # Actualizar y dibujar la bola
    ball.update()
    ball.draw(screen)

    # Si la bola se sale de la pantalla, reubicarla en la parte superior
    if ball.y > screen_height + ball.radius:
        ball.x = random.randint(0, screen_width)
        ball.y = -150
        ball.vy = 0
    
    if(colision.any()==1):
        ball.vy = -random.randint(25, 40)
        ball.vx = random.randint(-9, 9)

def GenMasks():
    # Se definen las máscaras
    face_mask = np.zeros(frame.shape[:2], dtype='uint8')
    ball_mask = np.zeros(frame.shape[:2], dtype='uint8')

    # Si se detecta al menos un rostro se crean las máscaras 
    if len(faces) > 0:
        (x,y,w,h) = faces[0]
        
        #Ajustes de las coordenadas de las máscaras
        x1_fmask = x + int(w / 8)
        x2_fmask = x + int(w * 7 / 8)
        y1_fmask = y - int(h/12)
        y2_fmask = y + int(h/12)
        x_bmask = int(ball.x + ball.radius + 7)
        y_bmask = int(ball.y + ball.radius + 3)
        
        #cv2.rectangle(frame,(x1_fmask, y1_fmask),(x2_fmask, y2_fmask),(0, 255, 0),1)
        detectado = True
        
        # Se crean las máscaras
        cv2.circle(ball_mask,(x_bmask, y_bmask),ball.radius ,255 , -1)
        cv2.rectangle(face_mask, (x1_fmask, y1_fmask),(x2_fmask, y2_fmask),255,-1)
        face_mask = cv2.flip(face_mask, 1)
        
    else:
        detectado = False
        
    return [face_mask, ball_mask]
            
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

# Agregar la bola
x = random.randint(0, screen_width-40)
y = -150
ball = Ball(x, y)

while True:
    
    # Obtener un fotograma de la cámara
    ret, frame = cap.read()

    # Convertir el fotograma a un formato compatible con Pygame
    bckgd = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    bckgd = np.rot90(bckgd)
    bckgd = pygame.surfarray.make_surface(bckgd)

    # Mostrar el fotograma en el fondo de la ventana
    screen.blit(bckgd, (0, 0))
    
    # Detectar rostros en el fotograma
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    [face_mask, ball_mask] = GenMasks()
    
    colision = cv2.bitwise_and(face_mask, face_mask, mask=ball_mask)
    
    InicioJuego()
    
    # Actualizar la ventana de Pygame
    pygame.display.update()

    # Esperar a que el usuario presione una tecla para salir
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                cap.release()
                pygame.quit()
                quit()

