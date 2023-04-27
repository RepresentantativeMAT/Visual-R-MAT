

from Filters.Filter import Filter
from Trajectory import Trajectory
from TrajectoryBank import TrajectoryBank

class CategoricalFilter(Filter):
    def __init__(self):
        super().__init__()
        self.__filtered_trajectories = TrajectoryBank()
    @property
    def filtered_trajectories(self):
        return self.__filtered_trajectories

    # Recebe lista de valores aceitos e key da semantica e retorna pontos que satisfazem a condicao
    def filter_trajectories(self, filter_name, trajectories, key, arguments):
        for trajectory in trajectories:
            new_traj = Trajectory(trajectory.id)
            for point in trajectory.points:
                if (point.semantics[key].split(' ')[0] in arguments):
                    new_traj.add_point(point)
            if not(new_traj.is_empty()):
                new_traj.id = filter_name
                self.filtered_trajectories.add_traj(new_traj)