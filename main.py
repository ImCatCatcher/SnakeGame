import pygame as pg
from random import randrange
import tkinter as tk

def exitGame():
    global snakeLen

    root = tk.Tk()
    pg.display.quit()

    msg_label = tk.Label(root, text="Вы проиграли!")
    msg_label.pack()

    msg_label_1 = tk.Label(root, text=f"Счет: {snakeLen}")
    msg_label_1.pack()

    msg_label_2 = tk.Label(root, text=f"Рекорд: 0")
    msg_label_2.pack()

    dismiss_btn = tk.Button(root, text="Выход", command=quit)
    dismiss_btn.pack()

    root.title("Змейка")
    root.geometry("250x100")
    root.resizable(False, False)
    root.configure(bg="white")

    root.mainloop()
 
pg.init()
screen = pg.display.set_mode((400, 400))
pg.display.set_caption("Змейка")

snakeLen = 1
bonus = (randrange(0,400,20),randrange(0,400,20))
curX = randrange(0,400,20)
curY = randrange(0,400,20)
snake = [(curX, curY)] #координаты старта змейки

dx, dy = 0, 0
fps = 10

curDir = ""

clock = pg.time.Clock()

while True:
    screen.fill(pg.Color("black"))

    if len(snake) != len(set(snake)):
        exitGame()
        

    key = pg.key.get_pressed()
    if key[pg.K_w] and curDir != "w" and curDir != "s":
        dx,dy = 0, -1
        curDir = "w"
    if key[pg.K_s] and curDir != "w" and curDir != "s":
        dx,dy = 0, 1
        curDir = "s"
    if key[pg.K_a] and curDir != "a" and curDir != "d":
        dx,dy = -1, 0
        curDir = "a"
    if key[pg.K_d] and curDir != "a" and curDir != "d":
        dx,dy = 1, 0
        curDir = "d"
    
    for i, j in snake:
        pg.draw.rect(screen, pg.Color("green"), (i,j,20,20))

    pg.draw.rect(screen, pg.Color("red"),(bonus[0], bonus[1], 20, 20))

    curX += dx * 20
    curY += dy * 20

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
            exitGame()