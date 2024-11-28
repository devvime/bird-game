import pygame as pg
from game.core.entity import Entity

class Pipe(Entity):
    
    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)
        
    def update(self, *args):
        self.move()
    
    def move(self):
        self.rect[0] -= 3
        
        if self.rect[0] <= -100:
            self.kill()