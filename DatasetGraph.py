

from GraphBuilder import GraphBuilder


class DatasetGraph(GraphBuilder):
    def __init__(self, dataset_data, semantic_key, line_color, point_color, 
                 line_width = 1, line_style = '-', marker_style = 'o', 
                 marker_size = 16, plot_points = False, plot_text = False):
        super().__init__()

        self.__dataset_data = dataset_data
        pos = dataset_data[0].positions()
        axis_limits = [min(pos[0]), max(pos[0]),
                       min(pos[1]), max(pos[1])]

        for trajectory in dataset_data:
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
            self.plot_line(trajectory, line_color, line_width, line_style)

            if plot_points:
                self.plot_points(trajectory, point_color, marker_style, marker_size)
            
        if plot_text:
            self.plot_text(dataset_data, semantic_key, (line_color, line_color))
        
        self.config_graph(axis_limits, len(dataset_data)//2)