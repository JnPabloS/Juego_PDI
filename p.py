import pygame
from ClassBall import Ball
import cv2
import numpy as np
import random
import time

def BuscarColor():
    
    # Rango de color amarillo en formato HSV
    lower = np.array([20, 100, 100])
    upper = np.array([30, 255, 255])
    
    # Convertir el fotograma a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Aplicar la máscara para filtrar el color amarillo
    mask = cv2.inRange(hsv, lower, upper)

    # Aplicar una operación de erosión y dilatación para eliminar el ruido
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.erode(mask, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=2)

    # Encontrar los contornos del objeto amarillo
    contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        # Dibujar un rectángulo alrededor del objeto rosa
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar el fotograma
    #cv2.imshow('Frame', frame)
    return 0

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
        count +=1 
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
            
def contador_tiempo(frame,Time,pos,fontScale,BLANCO):
        #Mostrar tiempo y puntaje 
    
    tiempo_actual = time.time()
    tiempo_transcurrido = int(tiempo_finalizacion - tiempo_actual)

    if tiempo_transcurrido >=0:
        Time = "Tiempo: " + str(tiempo_transcurrido) + " segundos"
        cv2.putText(frame, Time, pos, cv2.FONT_HERSHEY_PLAIN, fontScale, BLANCO, 2)

    elif tiempo_transcurrido < 0:
        Time = "Tiempo Agotado"
        fontScale = 3
        pos = (150,300)
        cv2.putText(frame, Time, pos, cv2.FONT_HERSHEY_PLAIN, fontScale, BLANCO, 2)
        balls = []

# Inicializar Pygame
pygame.init()

# Definir la resolución de la ventana
ANCHO = 640
ALTO = 480
screen_width, screen_height = ANCHO, ALTO

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

#Variables inicales para el texto
pos = (50, 50)
Time = "Hola"
fontScale = 2

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)

pygame.init()

# Crear una ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Inicio")

# Crear un objeto Font
fuente = pygame.font.SysFont(None, 50)

# Crear un rectángulo para el botón de "start"
boton_rect = pygame.Rect(ANCHO/2 - 100, ALTO/2 - 50, 200, 100)
jugando = False  # Variable de estado para indicar si se está jugando o no

#sonido de start
start = pygame.mixer.Sound('start.mp3')

#logo
logo = pygame.image.load('logo.png')

count = 0
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
                tiempo = 20
                tiempo_inicial = time.time()
                tiempo_finalizacion = tiempo_inicial + tiempo
                jugando = True

        #Logo 
        logo_rect = logo.get_rect()
        logo_rect.centerx = ventana.get_rect().centerx
        ventana.blit(logo, logo_rect)

        # Dibujar el botón
        pygame.draw.rect(ventana, AZUL, boton_rect)
        texto = fuente.render("Start", True, BLANCO)
        texto_rect = texto.get_rect(center=boton_rect.center)
        ventana.blit(texto, texto_rect)

        # Actualizar la pantalla
        pygame.display.update()

    #Pabloooooooo aquiiiiiii 
    if jugando == True:
        # Obtener un fotograma de la cámara
        ret, frame1 = cap.read()
        frame = cv2.flip(frame1, 1)
    
        contador_tiempo(frame,Time,pos,fontScale,BLANCO)
        BuscarColor()

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