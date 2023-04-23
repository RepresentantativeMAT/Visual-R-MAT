

import PySimpleGUI as sg
from tkinter import filedialog
from Gui import Gui
from TrajectoryBank import TrajectoryBank
from Graph import Graph


# Manages program elements


class Controller:
    def __init__(self) -> None:
        self.__trajectory_bank = TrajectoryBank()   # Store trajectories data
        self.__graph = Graph()                      # Displayed graph
        self.__interface = Gui(self.__graph.fig)    # Graphical interface

    # Program main loop
    def run(self):
        running = True
        while running:
            event, values = self.__interface.window.read()  # Read for event

            if event == sg.WIN_CLOSED:
                running = False
            elif event == "load":
                self.load_file_loop()       # Calls loop for load file window
            elif event == "trajectories":
                self.trajectory_list_loop() # Calls loop for tajectories window
            elif event == "reset":
                self.reset(values)          # Reset graph
            elif event == "plot":
                self.plot(values)           # Plot graph
                #self.__graph.show_plot()
                self.__interface.draw_graph(self.__graph.fig)   # Update gui graph
            elif event == "save":
                filename = filedialog.asksaveasfilename(filetypes=[('PNG', '*.png')])   # Calls save window
                self.__graph.save_plot(filename)                                        # Save graph
        self.__interface.window.close()

    # Load file window loop
    def load_file_loop(self):
        self.__interface.load_file_window()     # Creates load file window
        while True:
            event, values = self.__interface.load_window.window.read()  # Read for event
            if event == sg.WIN_CLOSED:
                break
            if event == "load":
                if values["file_path"] == '':
                    self.error_message("No file path!")                 # No file path given
                else:
                    # Set file type
                    if values["rep_traj"]:
                        file_type = "rep_traj"
                    else:
                        file_type = "dataset"
                    # Call function to load file. If successful return True
                    if self.__trajectory_bank.add_from_file(values["file_path"], file_type=file_type):
                        semantics = [semantic[0] for semantic in self.__trajectory_bank.header]     # Collects semantic category types
                        self.__interface.update_semantics(semantics)                                # Updates semantic category types on gui
                        self.__interface.window['grid_size'].update(self.__trajectory_bank.settings.get('CellSize', 1)) # Updates grid size (default=1)
                        break
        self.__interface.load_window.window.close()

    # Trajectories window loop
    def trajectory_list_loop(self):
        self.__interface.load_trajectory_window(self.__trajectory_bank.trajectories)    # Creates trajectories window
        while True:
            event, values = self.__interface.trajectory_window.window.read()    # Read for event
            if event == sg.WIN_CLOSED:
                break
            if event.split('-')[0] == 'delete':
                # Deletes trajectory from trajectory bank
                id = event.split('-')[1]
                self.__interface.trajectory_window.remove_traj(id)
                self.__trajectory_bank.remove_traj(id)

    # Plot graph
    def plot(self, values):
        # If auto reset on resets graph before plotting
        if values["auto-reset"]:
            self.reset(values)

        trajectories = self.__trajectory_bank.trajectories

        # For every trajectory
        for trajectory in trajectories:
            # If trajectory type is active
            if values[trajectory.type]:
                # Get x and y positions as tuple(list[float], list[float])
                pos = trajectory.positions()
                # If line active plot lines
                if values[trajectory.type+'_line']:
                    self.__graph.plot_lines(pos[0], pos[1], trajectory.type, values[trajectory.type+'_color'], 
                                            values[trajectory.type+'_line_style'])
                # If point active plot points
                if values[trajectory.type+'_point']:
                    self.__graph.plot_points(pos[0], pos[1], trajectory.type, values[trajectory.type+'_color'], 
                                            values[trajectory.type+'_point_style'])
                # If text active plot texts
                if values[trajectory.type+'_text']:
                    self.__graph.plot_text(trajectory, values[trajectory.type+'_semantic'], values[trajectory.type+'_color'])
        
        # Adjust text if it exists
        self.__graph.adjust_text()  
        
        # Configure graph settings
        self.__graph.settings(values['grid'], float(values['grid_size']), self.__trajectory_bank.num_traj)

    def reset(self, values):
        self.__graph.reset(float(values['grid_size']), values['grid'])  # Reset graph
        self.__interface.draw_graph(self.__graph.fig)                   # Update gui

        # Calls error message
    def error_message(self, text):
        sg.PopupOK(text, title="Error", modal=True)
        