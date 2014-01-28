import pygame, sys, math, time

class Background():
    def __init__(self, speed = [0,-3]):
        self.image = pygame.image.load("Resources/Background/Background.png")
        self.rect = self.image.get_rect()
        self.maxSpeedx = speed[1]
        self.maxSpeedy = speed[0]
        self.speedy = self.maxSpeedy
        self.speedx = self.maxSpeedx
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def update(self):
        self.move()
        print self.rect.x
        if self.rect.x <= -950:
            print "blam"
            self.reset()
        
    def reset(self):
        self.rect.x = 0
        