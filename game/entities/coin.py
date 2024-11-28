import pygame as pg
from game.core.entity import Entity

class Coin(Entity):
    
    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)
        
        self.ticks = 0
        
    def update(self, *args):
        self.move()
        self.anim()
    
    def move(self):
        self.rect[0] -= 3
        
        if self.rect[0] <= -100:
            self.kill()
            
    def anim(self):
        self.ticks = (self.ticks + 1) % 6
        self.image = pg.image.load("assets/" + str(self.ticks) + ".png")