import pygame, sys, math, time
width = 900
height = 480

width = 900
height = 480
size = width, height

class Player():
    def __init__(self, images, speed = [2,2], size = [100,40], pos = (0,0)):
        self.images = []
        for image in images:
            newimage = pygame.image.load(image)
            self.images += [newimage]
        self.frame = 0
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.maxSpeedx = speed[0]
        self.maxSpeedy = speed[1]
        self.speedx = 0
        self.speedy = 0 
        self.speed = [self.speedx, self.speedy]
        self.radius = self.rect.width/2
        self.waitCount = 0
        self.waitMax = 30
        self.place(pos)
        self.rolling = "none"
        self.accelerating = "none"
        self.living = True
        
        
    def place(self, pos):
        self.rect.center = pos
        
    def direction(self, dir):
        if dir == "up":
            self.speedy = -self.maxSpeedy
            self.rolling = "up"
        if dir == "stop up":
            self.speedy = 0
            self.rolling = "none"
        if dir == "down":
            self.speedy = self.maxSpeedy
            self.rolling = "down"
        if dir == "stop down":
            self.speedy = 0
            self.rolling = "none"
        if dir == "right":
            self.speedx = self.maxSpeedx
            self.accelerating = "forward"
        if dir == "stop right":
            self.speedx = 0
            self.accelerating = "none"
        if dir == "left":
            self.speedx = -self.maxSpeedx
            self.accelerating = "back"
        if dir == "stop left":
            self.speedx = 0
            self.accelerating = "none"
    
    def update(self):
        self.move()
        self.animatePlayer()
        
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speedy = 0
            
    def collide(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceToPoint(other.rect.center):
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
    
    def animatePlayer(self):
        if self.rolling == "none":
            self.images = self.   
        if self.waitCount < self.waitMax:
            self.waitCount +=3
        else:
            self.waitCount = 0
            if self.frame < len(self.images) - 1:
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.images[self.frame]
    
    def collideWall(self,width,height):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
    
    def distanceToPoint(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))