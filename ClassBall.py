#----------------------------------------------------------------------------------------------------------
#--1. Inicializo el sistema -------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

import random
import pygame

#---- Se crea una clase para la creación y movimiento de los balones -------------------------------------

class Ball:

#---- Se crean e inicializan los atributos de la clase ball ----------------------------------------------

    def __init__(self):
        self.x = random.randint(100, 500)
        self.y = -50
        self.radius = 42
        self.color = pygame.image.load('images/ball.png')
        self.v0y = 0
        self.vy = 0
        self.vx = 0

#---- Método para actualizar la posción del balón -------------------------------------------------------

    def update(self):  
        g = 4
        self.vy = self.vy + 1/2 * g
        self.y += self.vy
        self.x += self.vx 
        
        if ((self.x > 600 - self.radius and self.vx > 0) or (self.x < - 40 + self.radius and self.vx < 0)) :
            self.vx = -self.vx

#---- Método para dibujar el balon ----------------------------------------------------------------------

    def draw(self, screen):
        screen.blit(self.color, (self.x, self.y))
        
        # Actualizar la pantalla
        pygame.display.flip()
        
    def __del__(self):
        self.y = 600