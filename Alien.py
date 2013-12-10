import pygame, sys, math, random, time

class Alien():
    def __init__(self, image, speed = [-2,0], size = [100,40], pos = (0,0)):
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
        
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def collideAlien(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceToPoint(other.rect.center):
                    other.living = False
                    if self.rect.center[0] < other.rect.center[0]:
                        if other.speedx < 0:
                            self.living = False
                    if self.rect.center[0] > other.rect.center[0]:
                        if other.speedx > 0:
                            self.living = False
                    if self.rect.center[1] < other.rect.center[1]:
                        if other.speedy < 0:
                            self.living = False
                    if self.rect.center[1] > other.rect.center[1]:
                        if other.speedy > 0:
                            self.living = False
    def update(self):
        self.move()
    
        











