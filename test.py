import math
import numpy as np
import csv
import matplotlib.pyplot as plot

from DatasetReader import DatasetReader
from RepresentativeTrajectoryGraph import RepresentativeTrajectoryGraph
from RepresentativeTrajectoryReader import RepresentativeTrajectoryReader
from DatasetGraph import DatasetGraph
from ComparisionGraph import ComparisionGraph

dataset_reader = DatasetReader("datasets/Foursquare - user 6 - v2.csv")
dataset_reader.process_data()

dataset_graph = DatasetGraph(dataset_reader.processed_data, 'red', 'red', plot_points= True, line_style='--')

# for trajectory in dataset_reader.processed_data:
#     plot.plot(trajectory[1], trajectory[2], label=trajectory[0], linewidth = 1, )

# plot.xlabel("Latitude")
# plot.ylabel("Longitude")
# plot.legend(loc='lower center', ncol = len(dataset_reader.processed_data))
# plot.grid()
# plot.show()


rep_traj_reader = RepresentativeTrajectoryReader("datasets/Foursquare - user 6 - v2[output] - z1.csv")
rep_traj_reader.process_data()
trajectory = rep_traj_reader.processed_data
#print(f"{trajectory[0]} -> X: {trajectory[1]}, Y: {trajectory[2]}")

rep_traj_graph = RepresentativeTrajectoryGraph(rep_traj_reader.processed_data, 'blue', 'blue', plot_points= True)

# plot.plot(rep_traj_reader.processed_data[1], rep_traj_reader.processed_data[2], label=rep_traj_reader.processed_data[0], color='blue')
 
# plot.xlabel("Latitude")
# plot.ylabel("Longitude")
# plot.legend(loc='lower center', ncol = len(rep_traj_reader.processed_data))
# plot.grid()
#plot.show()

trajectories = dataset_reader.processed_data
trajectories.append(rep_traj_reader.processed_data)

total_graph = ComparisionGraph(trajectories, 'red', 'red', 'blue', 'blue', rep_traj_plot_points=True)

# for i, trajectory in enumerate(trajectories):
#     if i == len(trajectories)-1:
#         plot.plot(trajectory[1], trajectory[2], label=trajectory[0], color='blue')
#         plot.scatter(trajectory[1], trajectory[2], marker='v', color='blue')
#     else:
#         plot.plot(trajectory[1], trajectory[2], label=trajectory[0], color='red')
#         plot.scatter(trajectory[1][1], trajectory[2][1], marker='o', color='red')
#         plot.scatter(trajectory[1][-1], trajectory[2][-1], marker='o', color='red')


# plot.xlabel("Latitude")
# plot.ylabel("Longitude")
# plot.legend(loc='lower center', ncol = len(trajectories))
# plot.grid()
# plot.show()
