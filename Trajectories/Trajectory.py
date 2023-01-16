

from Trajectories.Point import Point


# Represents a group of points
class Trajectory:
    def __init__(self, id):
        self.__id = id                      # ID of the trajectory
        self.__points : list[Point] = []    # List of points
        self.__num_points = 0               # Number of points
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, traj_id):
        self.__id = traj_id
    
    @property
    def points(self):
        return self.__points
    
    @property
    def num_points(self):
        return self.__points
    
    # Return (x,y) of every point in two lists
    def positions(self):
        pos = ([],[])
        for point in self.__points: # For every point in the trajectory
            pos[0].append(point.x)  # Add x cord to first list
            pos[1].append(point.y)  # Add y cord to second list
        return pos
    
    # Return time marks of every point
    def time_marks(self):
        time_marks = []
        for point in self.__points:
            time_marks.append(point.time)
        return time_marks

    # Return semantic attribute of every point based on given key
    def semantics(self, key):
        semantics = []
        for point in self.__points: # For every point in the trajectory
            semantics.append(point.semantics.get(key, ''))  # Add attribute value to list

    # Adds a point to the trajectory
    def add_point(self, point: Point):
        self.__points.append(point)
        self.__num_points += 1
    
    # Return true is trajectory has no points
    def is_empty(self):
        if len(self.__points) == 0:
            return True
        return False
