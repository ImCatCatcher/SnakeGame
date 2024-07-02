import tkinter as tk
import pygame as pg
from random import randint

import Bonuses, Obstacles, options

def exitGame(snakeLen):
    root = tk.Tk()
    pg.display.quit()

    msg_label = tk.Label(root, text="Вы проиграли!")
    msg_label.pack()

    msg_label_1 = tk.Label(root, text=f"Счет: {snakeLen}")
    msg_label_1.pack()

    with open("best.txt", "r") as f:
        best = int(f.read())
    if snakeLen > best:
        with open("best.txt", "w") as f:
            f.write(str(snakeLen))
        best = snakeLen
    msg_label_2 = tk.Label(root, text=f"Рекорд: {best}")
    msg_label_2.pack()

    dismiss_btn = tk.Button(root, text="Выход", command=quit)
    dismiss_btn.pack()

    root.title("Змейка")
    root.geometry("250x100")
    root.resizable(False, False)
    root.configure(bg="white")

    root.mainloop()

def generateBonus():
    match randint(0,2):
        case 0:
            bonus = Bonuses.Apple()
        case 1:
            bonus = Bonuses.Peach()
        case 2:
            bonus = Bonuses.Banana()
    return bonus

def generateObstacle():
    match randint(0,2):
        case 0:
            obstacle = Obstacles.LongTrioObstacle(rotated=bool(randint(0,1)))
        case 1:
            obstacle = Obstacles.CorneredTrioObstacle(rotated=bool(randint(0,1)))
        case 2:
            obstacle = Obstacles.DuoObstacle(rotated=bool(randint(0,1)))
    return obstacle