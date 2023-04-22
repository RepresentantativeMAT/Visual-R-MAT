

import PySimpleGUI as sg
from tkinter import filedialog
from Gui import Gui
from TrajectoryBank import TrajectoryBank
from Graph import Graph

class Controller:
    def __init__(self) -> None:
        self.__trajectory_bank = TrajectoryBank()
        self.__graph = Graph()
        self.__interface = Gui(self.__graph.fig)

    def run(self):
        running = True
        while running:
            event, values = self.__interface.window.read()

            if event == sg.WIN_CLOSED:
                running = False
            elif event == "load":
                self.load_file_loop()
            elif event == "trajectories":
                self.trajectory_list_loop()
            elif event == "reset":
                self.reset(values)
            elif event == "plot":
                self.plot(values)
                #self.__graph.show_plot()
                self.__interface.draw_graph(self.__graph.fig)
            elif event == "save":
                filename = filedialog.asksaveasfilename(filetypes=[('PNG', '*.png')])
                self.__graph.save_plot(filename)
        self.__interface.window.close()

    def load_file_loop(self):
        self.__interface.load_file_window()
        while True:
            event, values = self.__interface.load_window.window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == "load":
                if values["file_path"] == '':
                    self.error_message("No file path!")
                else:
                    file_type = "dataset"
                    if values["rep_traj"]:
                        file_type = "rep_traj"
                    if self.__trajectory_bank.add_from_file(values["file_path"], file_type=file_type):
                        semantics = [semantic[0] for semantic in self.__trajectory_bank.header]
                        self.__interface.update_semantics(semantics)
                        self.__interface.window['grid_size'].update(self.__trajectory_bank.settings.get('CellSize', 1))
                        break
        self.__interface.load_window.window.close()

    def trajectory_list_loop(self):
        self.__interface.load_trajectory_window(self.__trajectory_bank.trajectories)
        while True:
            event, values = self.__interface.trajectory_window.window.read()
            if event == sg.WIN_CLOSED:
                break
            if event.split('-')[0] == 'delete':
                id = event.split('-')[1]
                self.__interface.trajectory_window.remove_traj(id)
                self.__trajectory_bank.remove_traj(id)

    def plot(self, values):
        if values["auto-reset"]:
            self.reset(values)
        trajectories = self.__trajectory_bank.trajectories
        for trajectory in trajectories:
            if values[trajectory.type]:
                pos = trajectory.positions()
                if values[trajectory.type+'_line']:
                    self.__graph.plot_lines(pos[0], pos[1], trajectory.type, values[trajectory.type+'_color'], 
                                            values[trajectory.type+'_line_style'])
                if values[trajectory.type+'_point']:
                    self.__graph.plot_points(pos[0], pos[1], trajectory.type, values[trajectory.type+'_color'], 
                                            values[trajectory.type+'_point_style'])
                if values[trajectory.type+'_text']:
                    self.__graph.plot_text(trajectory, values[trajectory.type+'_semantic'], values[trajectory.type+'_color'])
        self.__graph.adjust_text()        
        self.__graph.settings(values['grid'], float(values['grid_size']), self.__trajectory_bank.num_traj)

    def reset(self, values):
                self.__graph.reset(float(values['grid_size']), values['grid'])
                self.__interface.draw_graph(self.__graph.fig)

    def error_message(self, text):
        sg.PopupOK(text, title="Error", modal=True)
        