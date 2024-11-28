import pygame as pg

class Entity(pg.sprite.Sprite):

    def __init__(self, img, x, y, *groups):
        super().__init__(*groups)
        
        self.image = pg.image.load(img)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y