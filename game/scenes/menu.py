import pygame as pg
import random
from game.core.entity import Entity
from game.core.text import Text
from game.entities.pipe import Pipe

class Menu:
    
    def __init__(self):
        
        self.change_scene = False
        self.ticks = 0
        
        self.all_sprites_group = pg.sprite.Group()
        
        self.bg = Entity("assets/sky.png", 0, 0, self.all_sprites_group)
        self.bg2 = Entity("assets/sky.png", 359.9, 0, self.all_sprites_group)
        self.ground = Entity("assets/ground.png", 0, 480, self.all_sprites_group)
        self.ground2 = Entity("assets/ground.png", 359.9, 480, self.all_sprites_group)
        
        self.get_ready = Entity("assets/getready.png", 60, 100, self.all_sprites_group)
        self.table_score = Entity("assets/score.png", 20, 200, self.all_sprites_group)
        self.go_button = Entity("assets/go.png", 100, 420, self.all_sprites_group)
        
        self.score = Text(text="0", size=100, pos=(160, 260))
    
    def events(self, event):
        if event.type == pg.MOUSEBUTTONUP:
            if self.go_button.rect.collidepoint(pg.mouse.get_pos()):
                self.change_scene = True
                
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                self.change_scene = True
    
    def draw(self, window):
        self.all_sprites_group.draw(window)
        self.score.draw(window)
    
    def update(self, pts):
        self.move_bg()
        self.move_ground()
        self.all_sprites_group.update()
        self.score.update(pts)
        
    def move_bg(self):
        self.bg.rect[0] -= 1
        self.bg2.rect[0] -= 1
        
        if self.bg.rect[0] <= -360:
            self.bg.rect[0] = 0
            
        if self.bg2.rect[0] <= 0:
            self.bg2.rect[0] = 359.9
            
    def move_ground(self):
        self.ground.rect[0] -= 3
        self.ground2.rect[0] -= 3
        
        if self.ground.rect[0] <= -360:
            self.ground.rect[0] = 0
            
        if self.ground2.rect[0] <= 0:
            self.ground2.rect[0] = 359.9