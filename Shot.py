import pygame, sys, math

class Shot():
    def __init__(self, image, size = [50,20], pos = (0,0)):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.maxSpeedy = [0]
        self.maxSpeedx = [1]
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.radius = self.rect.width/2
        self.place(pos)
        
    def place(self, pos):
        self.rect.center = pos
        
    def direction(self, dir):
        if dir == "right":
            self.speedx = self.maxSpeedx
            
    def collide(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceToPoint(other.rect.center):
                    self.living = False
                    other.living = False
                    
    