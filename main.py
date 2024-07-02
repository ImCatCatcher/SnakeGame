import pygame as pg
from random import randrange

import Classes

import functions

while True:
    screen.fill(pg.Color("black"))

    if len(snake) != len(set(snake)):
        functions.exitGame(snakeLen)
        

    key = pg.key.get_pressed()
    if key[pg.K_w] and curDir != "w" and curDir != "s":
        changeX,changeY = 0, -1
        curDir = "w"
    if key[pg.K_s] and curDir != "w" and curDir != "s":
        changeX,changeY = 0, 1
        curDir = "s"
    if key[pg.K_a] and curDir != "a" and curDir != "d":
        changeX,changeY = -1, 0
        curDir = "a"
    if key[pg.K_d] and curDir != "a" and curDir != "d":
        changeX,changeY = 1, 0
        curDir = "d"
    
    for i, j in snake:
        pg.draw.rect(screen, pg.Color("green"), (i,j,20,20))

    pg.draw.rect(screen, pg.Color("red"),(bonus[0], bonus[1], 20, 20))

    curX += changeX * 20
    curY += changeY * 20

    if curX > 400: curX = 0
    if curX < 0:   curX = 400
    if curY > 400: curY = 0
    if curY < 0:   curY = 400

    snake.append((curX, curY))
    snake = snake[-snakeLen:]

    if snake[-1] == bonus:
        bonus = (randrange(0,400,20),randrange(0,400,20))
        snakeLen += 1
        fps += 1

    pg.display.flip()
    clock.tick(fps)    

    for event in pg.event.get():
        if event.type == pg.QUIT:
            functions.exitGame(snakeLen)