

import csv
from Readers.CSVReader import CSVReader
from Trajectories.Trajectory import Trajectory
from Trajectories.Point import Point

class DatasetReader(CSVReader):
    def __init__(self, csv_path):
        super().__init__(csv_path)
        self.set_csv_data(csv_path)
        self.__header = next(self.__csv_data)

    def __str__(self) -> str:
        s = ''
        for trajectory in self.processed_data:
            s += f"{trajectory[0]} -> X: {trajectory[1]}, Y: {trajectory[2]}\n"
        return s

    @property
    def processed_data(self):
        return self.__processed_data

    @property
    def header(self):
        return self.__header

    def set_csv_data(self, csv_path):
        self.__csv_data = csv.reader(open(csv_path, "r"), delimiter=';')

    def process_data(self):
        self.__processed_data = []
        current_traj = Trajectory(id='initial')
        semantics = {}
        for row in self.__csv_data:
            if row[0] != current_traj.id:
                self.__processed_data.append(current_traj)
                semantics = {}
                current_traj = Trajectory(row[0])
            pos = row[1].split(' ')
            time = row[2]
            for key, value in zip(self.__header[3:], row[3:]):
                semantics[key] = value
            current_traj.add_point(Point(round(float(pos[0]), 3),
                                         round(float(pos[1]), 3), 
                                         time, semantics))
        self.__processed_data.pop(0)