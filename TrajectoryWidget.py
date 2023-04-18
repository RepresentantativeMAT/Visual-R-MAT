

import PySimpleGUI as sg
from AbstractWidget import AbstractWidget


class TrajectoryWidget(AbstractWidget):
    def __init__(self, trajectory) -> None:
        super().__init__()

        self.__layout = sg.Column([[sg.Text(trajectory.id, size=(10,1)), sg.Text(trajectory.type, size=(10,1)), 
                                   sg.Button("Delete", key='delete'+'-'+trajectory.id, size=(10,1))]], 
                                  key=trajectory.id)
    
    @property
    def layout(self):
        return self.__layout