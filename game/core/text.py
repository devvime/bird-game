import pygame as pg

class Text:
    
    def __init__(self, text="0", size=30, pos=(0, 0), color=(255, 255, 255)):
        
        self.pos = pos
        self.color = color
        
        self.font = pg.font.Font("assets/font/font.ttf", size)
        self.reder = self.font.render(text, False, self.color)
        
    def draw(self, window):
        window.blit(self.reder, self.pos)
        
    def update(self, text):
        self.reder = self.font.render(text, True, self.color)