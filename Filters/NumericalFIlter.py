

from Filters.Filter import Filter
from Trajectories.Trajectory import Trajectory


class NumericalFilter(Filter):
    def __init__(self):
        super().__init__()
        self.__filtered_trajectories = []
    
    @property
    def filtered_trajectories(self):
        return self.__filtered_trajectories

    def filter_trajectories(self, trajectories: list[Trajectory], key, arguments):
        for trajectory in trajectories:
            new_traj = Trajectory(trajectory.id)
            for point in trajectory.points:
                if (float(point.semantics[key]) >= arguments[0] and float(point.semantics[key]) <= arguments[1]):
                    new_traj.add_point(point)
            if not(new_traj.is_empty()):
                self.__filtered_trajectories.append(new_traj)
