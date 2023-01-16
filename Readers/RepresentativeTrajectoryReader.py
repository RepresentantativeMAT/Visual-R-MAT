

from Readers.CSVReader import CSVReader
from Trajectories.Trajectory import Trajectory
from Trajectories.Point import Point

def isfloat(n):
    try: 
        float(n)
        return True
    except ValueError:
        return False

# Process R-MAT files
class RepresentativeTrajectoryReader(CSVReader):
    def __init__(self, csv_path):
        super().__init__(csv_path)
        self.set_csv_data(csv_path) # Sets file

    @property
    def processed_data(self):
        return self.__processed_data

    def set_csv_data(self, csv_path):
        self.__csv_data = open(csv_path, "r").readlines() # Open file and saves lines

    def process_data(self, traj_bank):
        rep_traj = Trajectory(id='Representative Trajectory')
        semantics, info = {}, []
        for row in self.__csv_data: # For each line in the file
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
                # Adiciona ponto a trajetória representativa
                rep_traj.add_point(Point(round(float(pos[0]), 3), 
                                         round(float(pos[1]), 3), 
                                         time, semantics))
                semantics, info = {}, []

        traj_bank.add_traj(rep_traj)
