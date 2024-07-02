import pygame as pg
from random import randrange

import functions, Bonuses, Obstacles, options

pg.init()
screen = pg.display.set_mode((options.mapSize, options.mapSize))
pg.display.set_caption("Змейка")

snakeLen = 1
curX = randrange(0,options.mapSize,options.cellSize)
curY = randrange(0,options.mapSize,options.cellSize)
snake = [(curX, curY)] #координаты старта змейки

bonus = functions.generateBonus()

obstacles = [functions.generateObstacle() for i in range(2)]

changeX, changeY = 0, 0
fps = options.startFPS

curDir = ""

clock = pg.time.Clock()

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
    
    [pg.draw.rect(screen, pg.Color("green"), (i,j,options.cellSize,options.cellSize)) for i, j in snake]

    pg.draw.rect(screen, pg.Color(bonus.color),(*bonus.xytuple, options.cellSize, options.cellSize))
    
    [[pg.draw.rect(screen, pg.Color("white"),(*i, options.cellSize, options.cellSize)) for i in obstacle.xytuples] for obstacle in obstacles]

    curX += changeX * options.cellSize
    curY += changeY * options.cellSize

    if curX > options.mapSize: curX = 0
    if curX < 0:   curX = options.mapSize
    if curY > options.mapSize: curY = 0
    if curY < 0:   curY = options.mapSize

    snake.append((curX, curY))
    snake = snake[-snakeLen:]

    pg.display.flip()
    clock.tick(fps)

    if snake[-1] == bonus.xytuple:
        snakeLen += bonus.lengthMod
        fps += bonus.speedMod*options.baseSpeedMultiplier
        bonus = functions.generateBonus()

    for obstacle in obstacles:
        if snake[-1] in set(obstacle.xytuples):
            functions.exitGame(snakeLen)    

    for event in pg.event.get():
        if event.type == pg.QUIT:
            functions.exitGame(snakeLen)