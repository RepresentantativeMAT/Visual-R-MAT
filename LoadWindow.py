

import PySimpleGUI as sg
from AbstractWindow import AbstractWindow


class LoadWindow(AbstractWindow):
    def __init__(self) -> None:
        super().__init__()
        self.__layout = [[sg.FileBrowse(target="file_path", file_types=(("CSV Files", ".csv"), )), 
                             sg.InputText(key="file_path", size=(60,1)), sg.Button("Load", key='load')],
                            [sg.Radio("Dataset", "file_type_pick", key="dataset", default= True),
                             sg.Radio("Representative Trajectory", "file_type_pick", key="rep_traj"),
                             sg.Radio("Filter", "file_type_pick")]]
        self.__window = sg.Window("Load File", self.__layout, modal=True)

    @property
    def window(self):
        return self.__window