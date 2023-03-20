import random
import time
import cv2
import numpy as np
import pygame

def SetBackground(frame, screen):
    
    # Convertir el fotograma a un formato compatible con Pygame
    bckgd = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    bckgd = np.rot90(bckgd)
    bckgd = pygame.surfarray.make_surface(bckgd)

    # Mostrar el fotograma en el fondo de la ventana
    screen.blit(bckgd, (0, 0))

def ShowStart (logo, ventana, boton_rect, fuente, color1, color2):
        #Logo 
        logo_rect = logo.get_rect()
        logo_rect.centerx = ventana.get_rect().centerx
        ventana.blit(logo, logo_rect)

        # Dibujar el botón
        pygame.draw.rect(ventana, color1, boton_rect)
        texto = fuente.render("Start", True, color2)
        texto_rect = texto.get_rect(center=boton_rect.center)
        ventana.blit(texto, texto_rect)

        # Actualizar la pantalla
        pygame.display.update()

def ShowText(screen, color, ball, tiempo_finalizacion, points):
    #Mostrar tiempo y puntaje 
    
    # Crea una fuente de texto y renderiza el texto que quieres mostrar
    font = pygame.font.SysFont('Arial', 32)
    
    tiempo_actual = time.time()
    tiempo_transcurrido = int(tiempo_finalizacion - tiempo_actual)

    if tiempo_transcurrido >=0:
        Text = "Tiempo: " + str(tiempo_transcurrido) + " s"
        text = font.render(Text, True, color)
        pos = (50, 50)
        screen.blit(text, pos)
        
        Text = "Puntos:" + str(points)
        text = font.render(Text, True, color)
        pos = (200, 50)
        screen.blit(text, pos)


    elif tiempo_transcurrido < 0:
        Text = "Tiempo Agotado"
        pos = (150,300)
        text = font.render(Text, True, color)
        screen.blit(text, pos)
        ball.x = 0
        ball.y = 0
        ball.vy = 0

    pygame.display.flip()
    
def UpdateWindow(ball, screen, screen_height):
  
    # Actualizar y dibujar la bola
    ball.update()
    ball.draw(screen)

    # Si la bola se sale de la pantalla pierde
    if ball.y > screen_height + ball.radius:
        ball.x = random.randint(200, 400)
        ball.y = -50
        ball.vy = 0
        ball.vx = random.randint(-10, 10)
    