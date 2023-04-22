

import PySimpleGUI as sg
from AbstractWidget import AbstractWidget
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphWidget(AbstractWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__canvas = sg.Canvas(key='canvas')
        self.__figure_canvas_agg = None
        self.__layout = self.__canvas
    
    def draw_graph(self, window, fig):
        if(self.__figure_canvas_agg):
            self.__figure_canvas_agg.get_tk_widget().forget()
        self.__figure_canvas_agg = FigureCanvasTkAgg(fig, window['canvas'].TKCanvas)
        self.__figure_canvas_agg.draw()
        self.__figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=0)
        return self.__figure_canvas_agg

    @property
    def layout(self):
        return self.__layout
