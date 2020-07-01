import pygame as pg
import os


pg.init()

WIN_WIDTH = 400
WIN_LENGTH = 400

WIN = pg.display.set_mode((WIN_LENGTH,WIN_WIDTH))
PLAYER = pg.transform.scale(pg.image.load(os.path.join('imgs', 'ghost.png')), (32,32))
COIN = pg.image.load(os.path.join('imgs','heart.png'))


pg.display.set_caption("Coin Collector")
pg.display.set_icon(PLAYER)

def run():
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()

        WIN.fill((0,150,0))
        pg.display.update()

run()
