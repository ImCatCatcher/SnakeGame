from random import randrange

import options

class Apple:
    def __init__(self):
        self.__speedMod = 1
        self.__lengthMod = 1
        self.__x = randrange(0,options.mapSize,options.cellSize)
        self.__y = randrange(0,options.mapSize,options.cellSize)
        self.__color = "red"

    @property
    def speedMod(self): return self.__speedMod

    @property
    def lengthMod(self): return self.__lengthMod

    @property
    def x(self): return self.__x

    @property
    def y(self): return self.__y

    @property
    def color(self): return self.__color

    @property
    def xytuple(self): return (self.x, self.y)

class Peach:
    def __init__(self):
        self.__speedMod = 0
        self.__lengthMod = 1
        self.__x = randrange(0,options.mapSize,options.cellSize)
        self.__y = randrange(0,options.mapSize,options.cellSize)
        self.__color = "sienna1"

    @property
    def speedMod(self): return self.__speedMod

    @property
    def lengthMod(self): return self.__lengthMod

    @property
    def x(self): return self.__x

    @property
    def y(self): return self.__y

    @property
    def color(self): return self.__color

    @property
    def xytuple(self): return (self.x, self.y)

class Banana:
    def __init__(self):
        self.__speedMod = 0
        self.__lengthMod = 2
        self.__x = randrange(0,options.mapSize,options.cellSize)
        self.__y = randrange(0,options.mapSize,options.cellSize)
        self.__color = "yellow"

    @property
    def speedMod(self): return self.__speedMod

    @property
    def lengthMod(self): return self.__lengthMod

    @property
    def x(self): return self.__x

    @property
    def y(self): return self.__y

    @property
    def color(self): return self.__color

    @property
    def xytuple(self): return (self.x, self.y)