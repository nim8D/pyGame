import imp


import pygame as pg
from sys import exit

pg.init()
screen = pg.display.set_mode((800,400))
pg.display.set_caption("Running")
clock = pg.time.Clock()
test_Surface = pg.image.load('graphics/Sky.png')
ground_Surface = pg.image.load('graphics/ground.png')

while True:
    for event in  pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        screen.blit(test_Surface, (0,0))
        screen.blit(ground_Surface, (0,100))
        pg.display.update()
        clock.tick(60) 