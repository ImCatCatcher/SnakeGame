class Bonus:
    def __init__(self, speedMod, lengthMod):
        self.__speedMod  = speedMod
        self.__lengthMod = lengthMod

    @property
    def speedMod(self): return self.__speedMod

    @property
    def lengthMod(self): return self.__lengthMod

#apple = Bonus(speedMod=1,lengthMod=2)
#print(apple.speedMod)