import tkinter as tk
import pygame as pg

def exitGame(snakeLen):
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

def gameInit():
    pg.init()
    screen = pg.display.set_mode((400, 400))
    pg.display.set_caption("Змейка")

    snakeLen = 1
    bonus = (randrange(0,400,20),randrange(0,400,20))
    curX = randrange(0,400,20)
    curY = randrange(0,400,20)
    snake = [(curX, curY)] #координаты старта змейки

    changeX, changeY = 0, 0
    fps = 10

    curDir = ""

    clock = pg.time.Clock()

    return screen

def gameRun():
    pass