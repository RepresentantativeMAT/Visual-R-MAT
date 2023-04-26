

import PySimpleGUI as sg
from AbstractWindow import AbstractWindow
from TrajectoryWidget import TrajectoryWidget


class TrajectoryWindow(AbstractWindow):
    def __init__(self, trajectories) -> None:
        self.__trajectory_widgets = {}
        for trajectory in trajectories:
            self.__trajectory_widgets[trajectory.id] = TrajectoryWidget(trajectory)

        self.__layout = [[sg.Column(
            [[sg.Button("Delete all", key="delete_all")]] + 
            [[traj_w.layout] for traj_w in self.__trajectory_widgets.values()],
            size=(400,300), scrollable=True, vertical_scroll_only= True, expand_x=True, expand_y=True
        )]]
        self.__window = sg.Window("Load File", self.__layout, modal=True)

    def remove_traj(self, id):
        self.__trajectory_widgets.pop(id)
        self.__window[id].hide_row()

    @property
    def window(self):
        return self.__window
    
    @property
    def trajectory_widgets(self):
        return self.__trajectory_widgets