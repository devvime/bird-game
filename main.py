import pygame as pg

from game.scenes.menu import Menu
from game.scenes.game import Game

class Main:
    
    def __init__(self, size_x, size_y, title):
        
        pg.init()
        pg.mixer.init()
        
        self.window = pg.display.set_mode([size_x, size_y])
        self.title = pg.display.set_caption(title)
        self.loop = True
        self.fps = pg.time.Clock()
        
        self.game_scene = Game()
        self.menu_scene = Menu()
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                self.loop = False
                
            if not self.menu_scene.change_scene:
                self.menu_scene.events(event)
                
    def draw(self):        
        if not self.menu_scene.change_scene:
            self.menu_scene.draw(self.window)
            self.menu_scene.update(str(self.game_scene.max_score))
            
        elif not self.game_scene.change_scene:
            self.game_scene.draw(self.window)
            self.game_scene.update()
            
        else:
            self.loop = False
                
    def run(self):
        while self.loop:
            self.fps.tick(30)
            self.draw()
            self.events()
            pg.display.update()


loop = True

while loop:
    game = Main(360, 640, "Flappy Bird")
    game.run()