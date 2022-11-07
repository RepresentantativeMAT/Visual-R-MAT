

from Readers.DatasetReader import DatasetReader
from Readers.RepresentativeTrajectoryReader import RepresentativeTrajectoryReader
from Graphics.ComparisionGraph import ComparisionGraph
from Filters.Filter import Filter
from MainInterface import MainInterface
import PySimpleGUI as sg

class Controller:
    def __init__(self) -> None:
        self.__gui = MainInterface()
        self.__dataset_reader = None
        self.__rep_traj_reader = None
        self.__filters : list[Filter] = []
        self.__graph = ComparisionGraph()
        self.__gui.draw_figure(self.__graph.fig)

    def run(self):
        running = True
        while running:
            event, values = self.__gui.window.read()
            if event == sg.WIN_CLOSED:
                running = False
            elif event == 'dataset_path':
                if values['dataset_path'] != '':
                    self.__dataset_reader = DatasetReader(values['dataset_path'])
                    self.__dataset_reader.process_data()
                    self.__gui.update_semantics(self.__dataset_reader.header)
                    #print(self.__dataset_reader.processed_data)
                    #print(self.__dataset_reader.header)
            elif event == 'r-mat_path':
                if values['r-mat_path'] != '':
                    self.__rep_traj_reader = RepresentativeTrajectoryReader(values['r-mat_path'])
                    self.__rep_traj_reader.process_data()
                    #print(self.__rep_traj_reader.processed_data)
            elif event == 'plot_graph':
                if values['plot_dataset'] or values['plot_rep_traj']:
                    self.plot_graph(values)
                    self.__gui.draw_figure(self.__graph.fig)
            elif event == 'Save Figure':
                self.__graph.save_plot('image.png')
        quit()

    def plot_graph(self, values):
        if values['plot_dataset'] and values['plot_rep_traj']:
            trajectories = self.__dataset_reader.processed_data
            trajectories.append(self.__rep_traj_reader.processed_data)
            self.__graph.plot_trajectories(trajectories, values['displayed_semantic'], values['dataset_color'], values['dataset_color'], 
                                            values['rep_traj_color'], values['rep_traj_color'], 
                                            dataset_line_style=values['dataset_line_style'], rep_traj_line_style=values['rep_traj_line_style'],
                                            dataset_marker_style=values['dataset_marker_style'], rep_traj_marker_style=values['rep_traj_marker_style'],
                                            dataset_plot_points=values['plot_dataset_points'], rep_traj_plot_points=values['plot_rep_traj_points'],
                                            dataset_plot_text=values['plot_dataset_text'], rep_traj_plot_text=values['plot_rep_traj_text'])
            trajectories.pop()
        elif values['plot_dataset'] and not values['plot_rep_traj']:
            self.__graph.plot_trajectories(self.__dataset_reader.processed_data, values['displayed_semantic'], values['dataset_color'], values['dataset_color'], 
                                            values['rep_traj_color'], values['rep_traj_color'], 
                                            dataset_line_style=values['dataset_line_style'], rep_traj_line_style=values['rep_traj_line_style'],
                                            dataset_marker_style=values['dataset_marker_style'], rep_traj_marker_style=values['rep_traj_marker_style'],
                                            dataset_plot_points=values['plot_dataset_points'], rep_traj_plot_points=values['plot_rep_traj_points'],
                                            dataset_plot_text=values['plot_dataset_text'], rep_traj_plot_text=values['plot_rep_traj_text'])
        elif values['plot_rep_traj'] and not values['plot_dataset']:
            self.__graph.plot_trajectories([self.__rep_traj_reader.processed_data], values['displayed_semantic'], values['dataset_color'], values['dataset_color'], 
                                            values['rep_traj_color'], values['rep_traj_color'], 
                                            dataset_line_style=values['dataset_line_style'], rep_traj_line_style=values['rep_traj_line_style'],
                                            dataset_marker_style=values['dataset_marker_style'], rep_traj_marker_style=values['rep_traj_marker_style'],
                                            dataset_plot_points=values['plot_dataset_points'], rep_traj_plot_points=values['plot_rep_traj_points'],
                                            dataset_plot_text=values['plot_dataset_text'], rep_traj_plot_text=values['plot_rep_traj_text'])

#    print(f"{event} : {values}")