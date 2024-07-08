import tkinter as tk
import pygame as pg
from random import randint
import os

import Bonuses, Obstacles, options

difficulty = 0

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

    restart_btn = tk.Button(root, text="Рестарт", command=restartGame)
    restart_btn.pack()

    root.title("Змейка")
    root.geometry("250x100")
    root.resizable(False, False)

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

def restartGame():
    os.system("python3 main.py")
    quit()

def askDifficulty():
    global difficulty

    def classic():
        global difficulty
        difficulty = 0
        root.destroy()
    
    def hardcore():
        global difficulty
        difficulty = 1
        root.destroy()

    root = tk.Tk()

    tk.Label(root, text="Выберите сложность игры").pack()

    tk.Button(root, text="Обычная", command=classic).pack()

    tk.Button(root, text="Хардкор", command=hardcore).pack()

    root.title("Змейка")
    root.geometry("250x100")
    root.resizable(False, False)

    root.protocol("WM_DELETE_WINDOW", quit)
    root.mainloop()

def getGeneratedDifficulty():
    global difficulty
    return difficulty