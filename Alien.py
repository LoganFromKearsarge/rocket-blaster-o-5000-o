import pygame, sys, math, random, time

class Alien():
    def __init__(self, image, speed = [-2,0], size = [100,40], pos = (0,0):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.maxSpeedx = speed[0]
        self.maxSpeedy = speed[1]
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.radius = self.rect.width/2
        self.place(pos)
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(self):
        self.move()
        
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    
        











