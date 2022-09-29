

from Trajectories.Point import Point


class Trajectory:
    def __init__(self, id):
        self.__id = id
        self.__points : list[Point] = []
        self.__num_points = 0
    
    @property
    def id(self):
        return self.__id
    
    @property
    def points(self):
        return self.__points
    
    @property
    def num_points(self):
        return self.__points
    
    def positions(self):
        pos = ([],[])
        for point in self.__points:
            pos[0].append(point.x)
            pos[1].append(point.y)
        return pos
    
    def time_marks(self):
        time_marks = []
        for point in self.__points:
            time_marks.append(point.time)
        return time_marks

    def semantics(self, key):
        semantics = []
        for point in self.__points:
            semantics.append(point.semantics.get(key, ''))

    def add_point(self, point: Point):
        self.__points.append(point)
        self.__num_points += 1
