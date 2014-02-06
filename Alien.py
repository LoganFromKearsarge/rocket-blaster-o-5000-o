import pygame, sys, math, random, time

class Alien():
    def __init__(self, speed = [-2,0], pos = (0,0)):
    #Loading all the alien animation images, as well as explosion images
        self.images = [pygame.image.load("Resources/Alien/mob1.png"),
                       pygame.image.load("Resources/Alien/mob1-2.png"),
                       pygame.image.load("Resources/Alien/mob2.png"),
                       pygame.image.load("Resources/Alien/mob2-2.png"),
                       pygame.image.load("Resources/Alien/mob3.png"),
                       pygame.image.load("Resources/Alien/mob3-2.png"),
                       pygame.image.load("Resources/Alien/mob4.png"),
                       pygame.image.load("Resources/Alien/mob4-2.png"),
                       pygame.image.load("Resources/Alien/mob5.png"), 
                       pygame.image.load("Resources/Alien/mob5-2.png"),]
        self.explosionImages = [pygame.image.load("Resources/Explosion/Explosion1.png"), 
                       pygame.image.load("Resources/Explosion/Explosion2.png"),
                       pygame.image.load("Resources/Explosion/Explosion3.png"),
                       pygame.image.load("Resources/Explosion/Explosion3.png"),
                       pygame.image.load("Resources/Explosion/Explosion3.png"),
                       pygame.image.load("Resources/Explosion/Explosion2.png")]
        self.frame = 0
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.maxSpeedx = speed[0]
        self.maxSpeedy = speed[1]
        self.speedx = self.maxSpeedx
        self.speedy = self.maxSpeedy
        self.speed = [self.speedx, self.speedy]
        self.radius = self.rect.width/2
        self.place(pos)
        self.waitCount = 0
        self.waitMax = 15
        self.living = True
        self.dying = False
        
    #set position of alien
    def place(self, pos):
        self.rect.center = pos
        
    #telling the alien it can move
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    #telling the alien that it can't pass through walls   
    def collideWall(self, width, height):
        if self.rect.right < 0:
            self.living = False
            
        #Alien Collide, pretty self explanatory
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
    #Animate function for the alien                        
    def animateAlien(self):
        if self.waitCount < self.waitMax:
            self.waitCount +=3
        else:
            self.waitCount = 0
            if self.frame < len(self.images) - 1:
                self.frame += 1
            else:
                if not self.dying:
                    self.frame = 0
                else:
                    self.living = False
            self.image = self.images[self.frame]
    #define the kill for alien        
    def kill(self):
        self.images = self.explosionImages
        self.dying = True
        self.frame = 0
        self.waitCount = 0
        self.speedx = 0
        self.speedy = 0
        self.waitMax = 5
    #just updating the whole alien
    def update(self):
        self.move()
        self.animateAlien()
    #complicated math
    def distanceToPoint(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
    
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    
    
        











