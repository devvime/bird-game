import pygame as pg
import random
from game.core.entity import Entity
from game.core.text import Text
from game.entities.pipe import Pipe
from game.entities.coin import Coin
from game.entities.bird import Bird

class Game:
    
    def __init__(self):
        
        self.change_scene = False
        self.ticks = 0
        self.timer = 0
        self.max_score = 0
        self.check_max_score()
        
        self.all_sprites_group = pg.sprite.Group()
        self.coin_group = pg.sprite.Group()
        self.pipe_group = pg.sprite.Group()
        
        self.bg = Entity("assets/sky.png", 0, 0, self.all_sprites_group)
        self.bg2 = Entity("assets/sky.png", 359.9, 0, self.all_sprites_group)
        self.ground = Entity("assets/ground.png", 0, 480, self.all_sprites_group)
        self.ground2 = Entity("assets/ground.png", 359.9, 480, self.all_sprites_group) 
        self.bird = Bird("assets/bird0.png", 50, 320, self.all_sprites_group) 
        
        self.score = Text(text="0", size=100, pos=(150, 50))
    
    def events(event):
        pass
    
    def draw(self, window):
        self.all_sprites_group.draw(window)
        self.score.draw(window)
    
    def update(self):
        if self.bird.play:
            self.move_bg()
            self.move_ground()
            self.spaw_pipes()
            self.bird.collision_pipe(self.pipe_group)
            self.bird.collision_coin(self.coin_group)
            self.score.update(str(self.bird.pts))
            self.all_sprites_group.update()
        else:
            self.save_score()
            self.gameover()
        
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
            
    def spaw_pipes(self):
        self.ticks += 1
        
        if self.ticks >= random.randrange(80, 110):
            self.ticks = 0
            pipe = Pipe("assets/pipe1.png", 360, random.randrange(300, 450), self.all_sprites_group, self.pipe_group)
            pipe2 = Pipe("assets/pipe2.png", 360, pipe.rect[1] - 550, self.all_sprites_group, self.pipe_group) 
            coin = Coin("assets/0.png", 388, pipe.rect[1] - 100, self.all_sprites_group, self.coin_group) 
            
    def gameover(self):
        self.timer += 1
        if self.timer >= 30:
            self.change_scene = True
            
    def save_score(self):
        if self.bird.pts > self.max_score:
            self.max_score = self.bird.pts
            file = open("data/save.txt", "w")
            file.write(str(self.max_score))
            file.close()
            
    def check_max_score(self):
        file = open("data/save.txt", "r")
        self.max_score = int(file.read())
        file.close()