

import matplotlib.pyplot as plt
import numpy as np
import adjustText


class Graph:
    def __init__(self) -> None:
        self.__fig, self.__ax = plt.subplots()
        self.__ax.grid(True)
        self.__lines = []
        self.__points = []
        self.__texts = []

    def plot_lines(self, x, y, name, line_color, line_style = '-', line_width = 1):
        self.__lines = self.__ax.plot(x, y, label=name, color=line_color, linestyle=line_style, linewidth=line_width)

    def plot_points(self, x, y, name, marker_color, marker_style = 'o', marker_size = 10):
        self.__points = self.__ax.scatter(x, y, label=name, color=marker_color, marker=marker_style, s=marker_size)
    
    def plot_text(self, trajectory, key, color):
        for point in trajectory.points:
            if key == 'tid':
                text = trajectory.id
            elif key == 'lat':
                text = point.x
            elif key == 'lon':
                text = point.y
            elif key == 'date_time':
                text = point.time
            else:
                text = point.semantics[key]
            
            text = str(text).split(' ')[0]
            
            self.__texts.append(self.__ax.text(point.x, point.y, text, fontsize=6, c=color))

    def adjust_text(self):
        x = adjustText.adjust_text(self.__texts, autoalign='y', only_move={'points':'y', 'text':'y'}, 
                            force_points=0.15)#, arrowprops=dict(arrowstyle="->", color='black', lw=0.5))
        #print(f"{x} interation needed")

    def show_plot(self):
        plt.show()

    def save_plot(self, filename):
        plt.savefig(filename, dpi=800, bbox_inches='tight')
    
    def settings(self, grid, grid_size : float, n_traj, xlabel = "Latitude", ylabel = "Longitude"):
        if grid:
            #print(self.__ax.xaxis_date())
            xlim = self.__ax.get_xlim()
            x_ticks = np.arange(xlim[0], xlim[1], grid_size)
            #print('xlim: ', xlim, 'grid_size: ', grid_size)
            #print(np.arange(xlim[0], xlim[1], grid_size))
            ylim = self.__ax.get_ylim()
            y_ticks = np.arange(ylim[0], ylim[1], grid_size)
            self.__ax.set_xticks(x_ticks)
            self.__ax.set_yticks(y_ticks)

        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        self.__ax.legend(by_label.values(), by_label.keys(), loc='lower center', ncol = n_traj, bbox_to_anchor = (0.5, 1))
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

    def reset(self, grid_size : float, grid: bool):
        self.__fig, self.__ax = plt.subplots()
        self.__texts.clear()
        if grid: self.__ax.grid(True)
        else: self.__ax.grid(False)
        
    @property
    def fig(self):
        return self.__fig