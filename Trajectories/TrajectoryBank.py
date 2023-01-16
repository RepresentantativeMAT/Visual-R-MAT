

from Trajectories.Trajectory import Trajectory


# Group of trajectories
class TrajectoryBank:
    def __init__(self):
        self.__trajectories = {}  # Trajectories dictionary identified by ID
        self.__num_traj = 0         # Number of trajectories
    
    @property
    def trajectories_id(self):
        return list(self.__trajectories.keys())
    
    @property
    def trajectories(self):
        return list(self.__trajectories.values())

    @property
    def num_traj(self):
        return self.__num_traj

    # Return trajectory based on ID
    def id_search(self, id):
        return self.__trajectories[id]
    
    # Adds trajectory to bank
    def add_traj(self, traj: Trajectory):
        self.__trajectories[traj.id] = traj
        self.__num_traj += 1
    
    # Remove trajectories based on ID
    def remove_traj(self, id):
        if id in self.__trajectories.keys():
            self.__trajectories.pop(id)