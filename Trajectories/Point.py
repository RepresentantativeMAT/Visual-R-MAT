

class Point:
    def __init__(self, x, y, time, semantics : dict):
        self.__x = x
        self.__y = y
        self.__time = time
        self.__semantics = semantics
    
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def time(self):
        return self.__time

    @property
    def semantics(self):
        return self.__semantics