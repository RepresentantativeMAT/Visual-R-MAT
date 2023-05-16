

import matplotlib.pyplot as plt
import numpy as np
import adjustText


# Create, store and save graph


class Graph:
    def __init__(self) -> None:
        self.__fig, self.__ax = plt.subplots()  # Graph
        self.__ax.grid(True)                    # Set grid
        self.__lines = []                       # Keep lines stored (No use)
        self.__points = None                     # Keep points stored (No use)
        self.__texts = []                       # Keep texts stores (Used for adjusting text)

    # Receives points coordinates in lists x and y and plots lines connecting them on the order received
    def plot_lines(self, x, y, name, line_color, line_style = '-', line_width = 1):
        self.__lines += self.__ax.plot(x, y, label=name, color=line_color, linestyle=line_style, linewidth=line_width)

    # Receives points coordinates in lists x and y and plots them on the order received
    def plot_points(self, x, y, name, marker_color, marker_style = 'o', marker_size = 10):
        self.__points = self.__ax.scatter(x, y, label=name, color=marker_color, marker=marker_style, s=marker_size)
    
    # Receives trajectory and semantic category and prints texts on graph
    def plot_text(self, trajectory, key, color):
        # For each point of the category
        for point in trajectory.points:
            # Checks if is lat, lon, time or generic semantic
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
            
            # Creates text
            self.__texts.append(self.__ax.text(point.x, point.y, text, fontsize=6, c=color))

    # Adjust texts on graph so they dont overlay eachother (Very inefficient)
    def adjust_text(self):
        if self.__texts != []:
            x = adjustText.adjust_text(self.__texts, autoalign='y', only_move={'points':'y', 'text':'y'}, 
                                force_points=0.15)#, arrowprops=dict(arrowstyle="->", color='black', lw=0.5))
            #print(f"{x} interation needed")

    # Open native plot window (Not used)
    def show_plot(self):
        plt.show()

    # Save plot as png image
    def save_plot(self, filename):
        plt.savefig(filename, dpi=800, bbox_inches='tight')

    # Gets Axes boundaries based on the cell_size and the higher and lower limiters
    def get_ax_boundaries(self, lim: list, cell_size):
        lower_bound = np.floor(min(lim)/cell_size)*cell_size
        higher_bound = np.ceil(max(lim)/cell_size)*cell_size

        return lower_bound, higher_bound
    
    # Configure settings for graph
    def settings(self, grid, grid_size : float, n_traj, xlabel = "Latitude", ylabel = "Longitude"):
        # If grid on
        if grid:
            #print(self.__ax.xaxis_date())
            xlim = self.__ax.get_xlim()                         # x limits
            #x_ticks = np.arange(xlim[0], xlim[1], grid_size)    # Find grid intervals on x
            #print('xlim: ', xlim, 'grid_size: ', grid_size)
            #print(np.arange(xlim[0], xlim[1], grid_size))
            ylim = self.__ax.get_ylim()                         # y limits
            #y_ticks = np.arange(ylim[0], ylim[1], grid_size)    # Find grid intervals on y

            lower_bound_x, higher_bound_x = self.get_ax_boundaries(xlim, grid_size)
            lower_bound_y, higher_bound_y = self.get_ax_boundaries(ylim, grid_size)

            x_ticks = np.arange(lower_bound_x, higher_bound_x + grid_size, grid_size)
            y_ticks = np.arange(lower_bound_y, higher_bound_y + grid_size, grid_size)

            self.__ax.set_xticks(x_ticks)                       # Set grid intervals on x
            self.__ax.set_yticks(y_ticks)                       # Set grid intervals on y
        else:
            self.__ax.grid(False)

        # Set graph subtitles
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        self.__ax.legend(by_label.values(), by_label.keys(), loc='lower center', ncol = n_traj, bbox_to_anchor = (0.5, 1))
        
        # Set axis names
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

    # Resets graphs
    def reset(self, grid_size : float, grid: bool):
        self.__fig, self.__ax = plt.subplots()  # Create new empy graph
        self.__lines.clear()                    # Clean lines
        self.__texts.clear()                    # Clean texts

        # Set grid on or off
        if grid: self.__ax.grid(True)
        else: self.__ax.grid(False)
        
    @property
    def fig(self):
        return self.__fig