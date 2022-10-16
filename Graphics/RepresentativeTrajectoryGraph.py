

from Graphics.GraphBuilder import GraphBuilder


class RepresentativeTrajectoryGraph(GraphBuilder):
    def __init__(self, trajectory, semantic_key, line_color, point_color, 
                 line_width = 1, line_style = '-', marker_style = 'o', 
                 marker_size = 16, plot_points = False, plot_text = False):
        super().__init__()

        self.__dataset_data = trajectory
        pos = trajectory.positions()

        axis_limits = [min(pos[0]), max(pos[0]),
                       min(pos[1]), max(pos[1])]

    
        self.plot_line(trajectory, line_color, line_width, line_style)

        if plot_points:
            self.plot_points(trajectory, point_color, marker_style, marker_size)

        if plot_text:
            self.plot_text([trajectory], semantic_key, (line_color, line_color))

        self.config_graph(axis_limits, 1)