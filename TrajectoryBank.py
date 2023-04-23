

import csv
from Trajectory import Trajectory
from Point import Point

# Dertemines the semantic type of a value
def semantic_type(value: str):
    try:
        float(value)
        return "numerical"
    except:
        return "categorical"

def isfloat(n):
    try: 
        float(n)
        return True
    except ValueError:
        return False

class TrajectoryBank:
    def __init__(self) -> None:
        self.__trajectories : dict[str][Trajectory] = {}    # Stores trajectories
        self.__num_traj : int = 0
        self.__header : list[tuple]                         # Semantic categories
        self.__settings : dict[str][float] = {}             # MAT-SG output settings
        
    # See type of file and calls corret function
    def add_from_file(self, file_path : str, file_type: str):
        if file_type == 'dataset':
            return self.__read_dataset_file(file_path, file_type)
        else:
            return self.__read_rep_traj_file(file_path, file_type)

    # Reads dataset type file (MAT-SG input). True if file is correct format
    def __read_dataset_file(self, file_path : str, file_type: str):
        csv_file = open(file_path, "r")                           # Open file
        csv_data = csv.reader(csv_file, delimiter=';')    # Creates reader

        attributes = next(csv_data)  # Header categories
        if attributes[0] == 'rt': return False

        row = next(csv_data)         # First row
        self.__header = [("tid", "categorical"), ("lat", "numerical"), 
                  ("lon", "numerical"), ("date_time", "categorical")]
        # For every semantic attribute determines its type based on the value from the first row
        for i, attribute in enumerate(attributes[4:]):
            self.__header.append((attribute, semantic_type(row[i+3])))
        
        csv_file.seek(0) # Return to file start
        next(csv_data)   # Skips header

        current_traj = Trajectory('initial', 'initial') # Initial trajectory

        for row in csv_data:         # For each line in the file
            if row[0] != current_traj.id:   # Checks if it is new trajectory
                self.add_traj(current_traj)    # Adds current trajectory to bank
                current_traj = Trajectory(row[0], file_type)   # Creates new trajectory

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

        self.remove_traj('initial')    # Removes first trajectory

        csv_file.close()
        return True

    # Reads representative trajectory type file (MAT-SG output). True if file is correct format
    def __read_rep_traj_file(self, file_path : str, file_type: str):
        csv_data = open(file_path, "r").readlines() # Open file and saves lines
        if csv_data[0][0:3] == "tid": return False
        
        rep_traj = Trajectory('Representative Trajectory', file_type)
        semantics = {}
        for row in csv_data: # For each line in the file
            # Process line according with information find in it
            if row[0:6] == '(x,y)=':
                pos = row.split(' ')[1][1:-2].split(',')
            elif row[0:28] == 'Ranking of Interval Temporal':
                time = row.split('[')[1][0:-4]
                time = time.split(' ')
                time = [str(round(100*float(n[:-1]), 2))+',' if isfloat(n[:-1]) else n for n in time]
                time = ' '.join(time).replace(', ', ' / ').split(' / ')[0]
            elif row[0:7] == 'Ranking':
                text = row.split('[')[1][0:-4]
                text = text.split(' ')
                text = [str(round(100*float(n[:-1]), 2))+',' if isfloat(n[:-1]) else n for n in text]
                text = ' '.join(text).replace(', ', ' / ')
                semantics[row.split(' ')[2][0:-1].lower()] = text.split(' / ')[0]
            elif row[0:12] == 'Local mapped':
                # Adds point to representative trajectory
                rep_traj.add_point(Point(round(float(pos[0]), 3), 
                                         round(float(pos[1]), 3), 
                                         time, semantics))
                semantics= {}
        
        self.add_traj(rep_traj)

        header = csv_data[-2][0:-1].split(', ')
        values = csv_data[-1].split(', ')
        for i in range(len(header)):
            self.__settings[header[i]] = round(float(values[i]), 3)
        
        return True

    # Adds trajectory to bank
    def add_traj(self, traj: Trajectory):
        #print(traj.id, " - ", traj)
        self.__trajectories[traj.id] = traj
        self.__num_traj += 1
    
    # Remove trajectories based on ID
    def remove_traj(self, id):
        if id in self.__trajectories.keys():
            self.__trajectories.pop(id)
            self.__num_traj -= 1
    
    @property
    def trajectories(self):
        return self.__trajectories.values()
    
    @property
    def header(self):
        return self.__header
    
    @property
    def settings(self):
        return self.__settings
    
    @property
    def num_traj(self):
        return self.__num_traj