import pygame, sys, math, time

class Background():
    def __init__(self, speed = [0,-3]):
        self.image = pygame.image.load("Resources/Background/Background.png")
        self.rect = self.image.get_rect()
        self.maxSpeedx = speed[1]
        self.maxSpeedy = speed[0]
        self.speedy = self.maxSpeedy
        self.speedx = self.maxSpeedx
    #telling the background to move
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
    #telling the background to update   
    def update(self):
        self.move()
        if self.rect.x <= -1800:
            self.reset()
    #telling the background where it needs to reset    
    def reset(self):
        self.rect.x = 0
        