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

def ShowStart (fondo, logo, ventana, boton_rect, fuente, color1, color2):
        
        ventana.blit(fondo,(0,0))

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
    # Crea una fuente de texto y renderiza el texto que quieres mostrar
    font = pygame.font.Font('fonts/ARCO.ttf', 22)
    
    tiempo_actual = time.time()
    tiempo_transcurrido = int(tiempo_finalizacion - tiempo_actual)

    if tiempo_transcurrido >=0:
        Text = "Tiempo: " + str(tiempo_transcurrido) + " s     "
        text = font.render(Text, True, color)
        pos = (50, 50)
        screen.blit(text, pos)
        
        Text = "      Puntos:" + str(points)
        text = font.render(Text, True, color)
        pos = (200, 50)
        screen.blit(text, pos)


    elif tiempo_transcurrido < 0:
        carmesi = (165, 28, 48)
        Text = "Tiempo Agotado"
        pos = (200,250)
        text = font.render(Text, True, carmesi)
        puntuacion = font.render("Puntuación: " + str(points), True, carmesi)
        reestar = font.render("Press R to re-Start", True, carmesi)
        screen.blit(text, pos)
        screen.blit(puntuacion, (210,270))
        screen.blit(reestar,(170,290))
        pygame.mixer.music.stop()
        ball.x = 0
        ball.y = 0
        ball.vy = 0
        jugando = False

    pygame.display.flip()
    
def UpdateWindow(ball, screen, screen_height):
  
    # Actualizar y dibujar la bola
    ball.update()
    ball.draw(screen)

    # Si la bola se sale de la pantalla pierde
    if ball.y > screen_height + ball.radius:
        ball.x = random.randint(100, 500)
        ball.y = -150
        ball.vy = -random.randint(25, 40)
        ball.vx = random.randint(-19, 19)
    