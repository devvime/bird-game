import pygame as pg
from game.core.entity import Entity

class Bird(Entity):
    
    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)
        
        self.play = True
        self.ticks = 0
        self.pts = 0
        self.velocity = 4
        self.gravity = 1
        
        pg.mixer.init()
        self.sound_pts = pg.mixer.Sound("assets/sounds/point.ogg")
        self.sound_hit = pg.mixer.Sound("assets/sounds/hit.ogg")
        self.sound_wing = pg.mixer.Sound("assets/sounds/wing.ogg")
        
    def update(self, *args):
        self.move()
        self.anim()
    
    def move(self):
        key = pg.key.get_pressed()
        
        self.velocity += self.gravity
        self.rect[1] += self.velocity
        
        if self.velocity >= 15:
            self.velocity = 15
        
        if self.play:
            if key[pg.K_SPACE]:
                self.velocity -= 5
                self.sound_wing.play()
        
        if self.rect[1] > 440:
            self.rect[1] = 440
        elif self.rect[1] <= 0:
            self.rect[1] = 0
            self.velocity = 4
            
    def anim(self):
        self.ticks = (self.ticks + 1) % 4
        self.image = pg.image.load("assets/bird" + str(self.ticks) + ".png")
        
    def collision_pipe(self, group):
        collision = pg.sprite.spritecollide(self, group, False)
        
        if collision:
            self.play = False
            self.sound_hit.play()
            
    def collision_coin(self, group):
        collision = pg.sprite.spritecollide(self, group, True)
        
        if collision:
            self.pts += 1
            self.sound_pts.play()