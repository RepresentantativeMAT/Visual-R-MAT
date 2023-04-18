

from abc import ABC, abstractmethod
import PySimpleGUI as sg


class AbstractWindow(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.__window : sg.Window

    @abstractmethod
    def window(self):
        pass