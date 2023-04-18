

import PySimpleGUI as sg
from OptionBox import OptionBox
from GraphWidget import GraphWidget
from LoadWindow import LoadWindow
from TrajectoryWindow import TrajectoryWindow


class Gui:
    def __init__(self, fig) -> None:

        self.config_theme()

        self.__opt_box1 = OptionBox('dataset')
        self.__opt_box2 = OptionBox('rep_traj')
        self.__row1 = [sg.Button('Load', key='load', size=(10,1)), sg.Button('Trajectory List', key='trajectories'),
                       self.__opt_box1.layout, self.__opt_box2.layout]

        self.__graph_widget = GraphWidget()
        self.__graph_tab = sg.Column([[sg.Checkbox("Grid", key="grid", default=True), sg.Text("Grid Size:"), sg.InputText('1', key='grid_size', size=(5,1))],
                                     [self.__graph_widget.layout],
                                     [sg.Checkbox("Auto reset", key="auto-reset"), sg.Button("Reset", key="reset"), 
                                      sg.Button("Plot", key="plot"), sg.Button("Save", key="save")]],
                                     element_justification='r')
        self.__filter_tab = sg.Column([[sg.Text('filter-tab')]])
        self.__row2 = [self.__filter_tab, self.__graph_tab]

        self.__layout = [sg.Column([self.__row1, self.__row2])]
        self.__window = sg.Window("Visual R-MAT", layout=[self.__layout], finalize=True, resizable=True)
        self.__graph_widget.draw_graph(self.__window, fig)

    def config_theme(self):
        sg.theme('DefaultNoMoreNagging')
        #sg.theme_background_color('#1F1F1F')
        #sg.theme_element_background_color('#3C3C3C')
        #sg.theme_button_color_background()

    def load_file_window(self):
        self.__load_window = LoadWindow()
    
    def load_trajectory_window(self, trajectories):
        self.__trajectory_window = TrajectoryWindow(trajectories)

    def update_semantics(self, semantics):
        self.__opt_box1.update_semantic(semantics)
        self.__opt_box2.update_semantic(semantics)
    
    def draw_graph(self, fig):
        self.__graph_widget.draw_graph(self.__window, fig)
    
    def save_graph(self, filename):
        self.__graph_widget.save(filename)

    @property
    def window(self):
        return self.__window

    @property
    def load_window(self):
        return self.__load_window
    
    @property
    def trajectory_window(self):
        return self.__trajectory_window