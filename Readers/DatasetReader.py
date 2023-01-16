

import csv
from Readers.CSVReader import CSVReader
from Trajectories.Trajectory import Trajectory
from Trajectories.Point import Point


# Process dataset files
class DatasetReader(CSVReader):
    def __init__(self, csv_path):
        super().__init__(csv_path)
        self.set_csv_data(csv_path)             # Sets file
        self.__header = self.__process_header() # Saves header and determines semantic attributes categories

    @property
    def header(self):
        return self.__header

    def set_csv_data(self, csv_path):
        self.__csv_file = open(csv_path, "r")                           # Open file
        self.__csv_data = csv.reader(self.__csv_file, delimiter=';')    # Creates reader
    
    # Process file and saves information on trajectory bank
    def process_data(self, traj_bank):
        current_traj = Trajectory(id='initial') # Initial trajectory

        for row in self.__csv_data:         # For each line in the file
            if row[0] != current_traj.id:   # Checks if it is new trajectory
                traj_bank.add_traj(current_traj)    # Adds current trajectory to bank
                current_traj = Trajectory(row[0])   # Creates new trajectory

            semantics = {}  # Semantic attributes from current point
            pos = row[1].split(' ')     # Position (x,y) from point
            time = row[2]               # Time mark

            # For each other column in the line
            for key, value in zip(self.__header[4:], row[3:]):
                semantics[key[0]] = value   # Adds semantic value to dict with key from header

            # Adds point to current trajectory
            current_traj.add_point(Point(round(float(pos[0]), 3),
                                         round(float(pos[1]), 3), 
                                         time, semantics))

        traj_bank.remove_traj('initial')    # Removes first trajectory
    
    # Dertemines the semantic type of a value
    def semantic_type(self, value: str):
        try:
            float(value)
            return "numerical"
        except:
            return "categorical"
    
    # Process header and determines semantic type of every attributes
    def __process_header(self):
        attributes = next(self.__csv_data)  # Header categories
        row = next(self.__csv_data)         # First row
        header = [("tid", "categorical"), ("lat", "numerical"), 
                  ("lon", "numerical"), ("date_time", "categorical")]
        # For every semantic attribute determines its type based on the value from the first row
        for i, attribute in enumerate(attributes[3:]):
            header.append((attribute, self.semantic_type(row[i+3])))
        
        self.__csv_file.seek(0) # Return to file start
        next(self.__csv_data)   # Skips header
        return header