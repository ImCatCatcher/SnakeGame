from random import randrange, randint

import options

class LongTrioObstacle:
    def __init__(self, rotated):
        self.__length = 3
        self.__xytuples = [(randrange(0,options.mapSize,options.cellSize),randrange(0,options.mapSize,options.cellSize))]
        if not rotated: [self.__xytuples.append((self.__xytuples[-1][0],self.__xytuples[-1][1]+options.cellSize)) for i in range(self.__length-1)]
        else: [self.__xytuples.append((self.__xytuples[-1][0]+options.cellSize,self.__xytuples[-1][1])) for i in range(self.__length-1)]

    @property
    def length(self): return self.__length

    @property
    def xytuples(self): return self.__xytuples

class CorneredTrioObstacle:
    def __init__(self, rotated):
        self.__length = 3
        self.__xytuples = [(randrange(0,options.mapSize,options.cellSize),randrange(0,options.mapSize,options.cellSize))]
        if not rotated:
            self.__xytuples.append((self.__xytuples[0][0],self.__xytuples[0][1]+options.cellSize))
            self.__xytuples.append((self.__xytuples[1][0]+options.cellSize,self.__xytuples[1][1]))
        else:
            self.__xytuples.append((self.__xytuples[0][0]+options.cellSize,self.__xytuples[0][1]))
            self.__xytuples.append((self.__xytuples[1][0],self.__xytuples[1][1]+options.cellSize))

    @property
    def length(self): return self.__length

    @property
    def xytuples(self): return self.__xytuples

class DuoObstacle:
    def __init__(self, rotated):
        self.__length = 3
        self.__xytuples = [(randrange(0,options.mapSize,options.cellSize),randrange(0,options.mapSize,options.cellSize))]
        if not rotated:
            self.__xytuples.append((self.__xytuples[0][0],self.__xytuples[0][1]+options.cellSize))
        else:
            self.__xytuples.append((self.__xytuples[0][0]+options.cellSize,self.__xytuples[0][1]))

    @property
    def length(self): return self.__length

    @property
    def xytuples(self): return self.__xytuples