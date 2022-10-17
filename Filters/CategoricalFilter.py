

from Filters.Filter import Filter
from Trajectories.Trajectory import Trajectory


class CategoricalFilter(Filter):
    def __init__(self):
        super().__init__()
        self.__filtered_trajectories = []
    
    @property
    def filtered_trajectories(self):
        return self.__filtered_trajectories

    def filter_trajectories(self, trajectories, key, arguments):
        for trajectory in trajectories:
            new_traj = Trajectory(trajectory.id)
            for point in trajectory.points:
                if (point.semantics[key] in arguments):
                    new_traj.add_point(point)
            if not(new_traj.is_empty()):
                self.filtered_trajectories.append(new_traj)