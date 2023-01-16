

from Graphics.GraphBuilder import GraphBuilder


class ComparisionGraph(GraphBuilder):
    def __init__(self):
        super().__init__()

    def plot_trajectories(self, traj_bank, semantic_key, dataset_line_color, dataset_point_color, rep_traj_line_color, rep_traj_point_color,
                 dataset_line_width = 1, rep_traj_line_width = 1, dataset_line_style = '-', rep_traj_line_style = '-',
                 dataset_marker_style = 'o', rep_traj_marker_style = 'o', dataset_marker_size = 16, rep_traj_marker_size = 16,
                 dataset_plot_points = False, rep_traj_plot_points = False, dataset_plot_text = False, rep_traj_plot_text = False):

        self.__traj_bank = traj_bank
        pos = traj_bank.id_search(traj_bank.trajectories_id[0]).positions()
        axis_limits = [min(pos[0]), max(pos[0]),
                       min(pos[1]), max(pos[1])]

        for trajectory in traj_bank.trajectories:
            if trajectory.id == 'Representative Trajectory':
                self.plot_line(trajectory, rep_traj_line_color, rep_traj_line_width, rep_traj_line_style)
                if rep_traj_plot_points:
                    self.plot_points(trajectory, rep_traj_point_color, rep_traj_marker_style, rep_traj_marker_size)
            else :
                n = min(trajectory.positions()[0])
                if n < axis_limits[0]:
                    axis_limits[0] = round(n, 2)
                n = max(trajectory.positions()[0])
                if n > axis_limits[1]:
                    axis_limits[1] = round(n, 2)
                n = min(trajectory.positions()[1])
                if n < axis_limits[2]:
                    axis_limits[2] = round(n, 2)
                n = max(trajectory.positions()[1])
                if n > axis_limits[3]:
                    axis_limits[3] = round(n, 2)
                self.plot_line(trajectory, dataset_line_color, dataset_line_width, dataset_line_style)

                if dataset_plot_points:
                    self.plot_points(trajectory, dataset_point_color, dataset_marker_style, dataset_marker_size)
            
        if dataset_plot_text and rep_traj_plot_text:
            self.plot_text(traj_bank.trajectories, semantic_key, (rep_traj_line_color, dataset_line_color))
        elif dataset_plot_text:
            self.plot_text(traj_bank.trajectories[0:-1], semantic_key, (dataset_line_color, dataset_line_color))
        elif rep_traj_plot_text and traj_bank.trajectories[-1].id == 'Representative Trajectory':
            self.plot_text([traj_bank.trajectories[-1]], semantic_key, (rep_traj_line_color, rep_traj_line_color))

        self.config_graph(axis_limits, traj_bank.num_traj//2)

