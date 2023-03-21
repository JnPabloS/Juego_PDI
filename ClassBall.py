import pygame

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 42
        self.color = pygame.image.load('images/ball.png')
        self.v0y = 0
        self.vy = 0
        self.vx = 0

    def update(self):  
        g = 4
        self.vy = self.vy + 1/2 * g
        self.y += self.vy
        self.x += self.vx 
        
        if ((self.x > 600 - self.radius and self.vx > 0) or (self.x < - 40 + self.radius and self.vx < 0)) :
            self.vx = -self.vx

    def draw(self, screen):
        screen.blit(self.color, (self.x, self.y))
        
        # Actualizar la pantalla
        pygame.display.flip()