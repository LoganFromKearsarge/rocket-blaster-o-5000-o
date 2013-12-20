import pygame, sys, math

class Shot():
    def __init__(self, pos = (0,0)):
        self.image = pygame.image.load("Resources/Shot/Rocket.png")
        self.rect = self.image.get_rect()
        self.speedx = 10
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.radius = self.rect.width/2
        self.place(pos)
        self.living = True
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(self):
        self.move()
        
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
            
    def collide(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceToPoint(other.rect.center):
                    self.living = False
                    other.living = False
                 
    def distanceToPoint(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
    
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
                    
    