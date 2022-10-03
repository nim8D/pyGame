import imp


import pygame as pg

pg.init()
screen = pg.display.set_mode((800,400))
pg.display.set_caption("Running")
while True:
    for event in  pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
pg.display.update()