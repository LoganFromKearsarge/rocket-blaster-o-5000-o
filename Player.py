import pygame, sys, math

width = 900
height = 480
size = width, height

class Player():
    def __init__(self, image, speed = [2,2], size = [100,40], pos = (0,0)):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.maxSpeedx = speed[0]
        self.maxSpeedy = speed[1]
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.radius = self.rect.width/2
        self.place(pos)
        self.living = True
        
        
    def place(self, pos):
        self.rect.center = pos
        
    def direction(self, dir):
        if dir == "up":
            self.speedy = -self.maxSpeedy
        if dir == "stop up":
            self.speedy = 0
        if dir == "down":
            self.speedy = self.maxSpeedy
        if dir == "stop down":
            self.speedy = 0
    
    def update(self):
        self.move()
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speedy = 0
            
    def collide(self, other):
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
    
    def distanceToPoint(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))