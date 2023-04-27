

from Filter import Filter
from Trajectory import Trajectory
from TrajectoryBank import TrajectoryBank

class NumericalFilter(Filter):
    def __init__(self):
        super().__init__()
        self.__filtered_trajectories = TrajectoryBank()
    
    @property
    def filtered_trajectories(self):
        return self.__filtered_trajectories

    # Recebe parametros de intervalo e key da semantica e retorna pontos que satisfazem a condicao
    def filter_trajectories(self, trajectories: list[Trajectory], key, arguments):
        arguments[0] = float(arguments[0])
        arguments[1] = float(arguments[1])

        for trajectory in trajectories:
            new_traj = Trajectory(trajectory.id)
            for point in trajectory.points:
                if (float(point.semantics[key]) >= arguments[0] and float(point.semantics[key]) <= arguments[1]):
                    new_traj.add_point(point)
            if not(new_traj.is_empty()):
                self.__filtered_trajectories.add_traj(new_traj)
