# Visual-R-MAT: Visual Representation of Multiple Aspect Trajectory
==========================================================================

Overview
Visual R-MAT is a tool for the representation of multiple aspect trajectories (MAT) in 2D graphs with a main focus on the comparison of a set T=<t1, t2, ..., tn> of MATs to a representative trajectory of the set. It offers the following options for creating graphs:
- (i) dataset representation: Represents the dataset with the use of lines and points that can be customized. The input file follows the format proposed by the MAT-SG method. 
- (ii) representative trajectory: Draws the representative trajectories with points and/or lines. The input file follows the format proposed by the MAT-SG method. 
- (iii) text representation: An option to display semantic information related to each point of the set T trajectories and/or the representative trajectory. 

# Not Implemented features
- Filter: Option to filter and display only points that satisfy a semantic condition.
- Save file type and image quality option not implemented.
- ...

# Installation:
 Download the repository and install the following Python libraries (if not already installed):
 - PySimpleGui
 - tkinter
 - adjustText

# How to run:
Launch the program through the app.py file. Click on "Load" and select the file path and its format (filter option not implemented). Click on "Trajectories" to see the loaded trajectories and manually delete them. Select options for dataset and representative trajectory visualization and generate the graph by clicking on "Plot". Other functions include:
- Loading the representative trajectory file sets the grid size automatically. The grid can also be manually set and turned on/off.
- The "Auto reset" option resets the graph every time it's generated. If turned off, it adds lines, points, and texts over the existing graph (even if it's the same information on the graph).
- The "Save" option allows to save the graph as PNG images (other file types not implemented).

