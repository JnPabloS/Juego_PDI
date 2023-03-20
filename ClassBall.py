import pygame
#from datetime import datetime

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 42
        self.color = pygame.image.load('ball.png')
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
        #pygame.draw.circle(screen, (255, 0, 0), (self.x+self.radius+7, int(self.y+self.radius+3)), self.radius)
        screen.blit(self.color, (self.x, self.y))