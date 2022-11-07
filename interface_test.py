import PySimpleGUI as sg
from MainInterface import MainInterface
import matplotlib.pyplot as plt
import numpy as np
from Readers.DatasetReader import DatasetReader
from Readers.RepresentativeTrajectoryReader import RepresentativeTrajectoryReader
from Graphics.ComparisionGraph import ComparisionGraph
from Filters.Filter import Filter

dataset = DatasetReader("D:/Tiago/UFSC/PET/Pesquisa/Visual-R-MAT/datasets/Foursquare - user 6 - v2.csv")
dataset.process_data()
graph = ComparisionGraph(dataset.processed_data, "rating", "red", "red", "blue", "blue")


gui = MainInterface()

running = True
while running:
    event, values = gui.window.read(timeout=200)
    gui.draw_figure(graph.fig)
    if event == sg.WIN_CLOSED:
        running = False
    print(values['dataset_path'])

gui.window.close()
quit()