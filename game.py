import imp


import pygame as pg
from sys import exit

pg.init()
screen = pg.display.set_mode((800,400))
pg.display.set_caption("Running")
clock = pg.time.Clock()
test_Surface = pg.Surface(100,200)
test_Surface.fill('Red')
while True:
    for event in  pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
pg.display.update()
screen.blit(test_Surface, (0,0))
clock.tick(60) 