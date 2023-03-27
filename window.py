import random
import cv2
import numpy as np
import pygame

# Muestra la ventana de inico 
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
        
# Actualiza la imagen de fondo
def SetBackground(frame, screen):
    
    # Convertir el fotograma a un formato compatible con Pygame
    bckgd = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    bckgd = np.rot90(bckgd)
    bckgd = pygame.surfarray.make_surface(bckgd)

    # Mostrar el fotograma en el fondo de la ventana
    screen.blit(bckgd, (0, 0))

# Muestra el tiempo de juego y puntos en la pantalla
def ShowText(screen, color, tiempo_transcurrido, points):
    # Crea una fuente de texto y renderiza el texto que quieres mostrar
    font = pygame.font.Font('fonts/ARCO.ttf', 22)

    Text = "Tiempo: " + str(tiempo_transcurrido) + " s     "
    text = font.render(Text, True, color)
    pos = (50, 50)
    screen.blit(text, pos)
    
    Text = "      Puntos: " + str(points)
    text = font.render(Text, True, (165, 28, 48))
    pos = (400, 50)
    screen.blit(text, pos)

# Muestra los resultados una vez se termina el juego
def ShowFinal(screen, ball, points):
    
    pygame.display.update()
    ball.__del__()
    # Crea una fuente de texto y renderiza el texto que quieres mostrar
    font = pygame.font.Font('fonts/ARCO.ttf', 22)
    
    carmesi = (165, 28, 48)
    Text = "Tiempo Agotado"
    pos = (200,200)
    text = font.render(Text, True, carmesi)
    puntuacion = font.render("Puntuación: " + str(points), True, (0, 0, 255))
    reestar = font.render("Press R to re-Start", True, carmesi)
    screen.blit(text, pos)

    screen.blit(puntuacion, (210,250))
    screen.blit(reestar,(170,400))

    pygame.display.flip()
    
    return True
    
# Actualiza la posicion de la bola en la pantalla
def UpdateWindow(ball, screen, screen_height):
  
    # Actualizar y dibujar la bola
    ball.update()
    ball.draw(screen)

    # Si la bola se sale de la pantalla se reubica arriba de nuevo
    if ball.y > screen_height + 2 * ball.radius:
        ball.x = random.randint(200, 400)
        ball.y = -50
        ball.vy = 0
        ball.vx = random.randint(-10, 10)
        