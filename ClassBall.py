import pygame
#from datetime import datetime

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 40
        self.color = pygame.image.load('ball.png')
        self.v0y = 0
        self.vy = 6
        self.vx = 0
        #self.t =datetime.now()

    def update(self):
        
        #tf = datetime.now()
        #tiempo = tf - self.t # Devuelve un objeto timedelta
        #s = tiempo.seconds
        
        #g = 10
        
        #self.vy = self.v0y * s + 1/2 * g * s**2
        #self.y = self.vy * s
        self.y += self.vy
        #print(s)
        #print(self.x , "     ", self.y)
        #self.x += self.vx 

    def draw(self, screen):
        screen.blit(self.color, (self.x, self.y))
        #pygame.draw.circle(screen, (255, 0, 0), (self.x, int(self.y)), self.radius)