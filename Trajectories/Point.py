

# Represents a point from a trajectory
class Point:
    def __init__(self, x, y, time, semantics : dict):
        self.__x = x                    # X Position
        self.__y = y                    # Y Position
        self.__time = time              # Time mark
        self.__semantics = semantics    # Semantic attributes
    
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