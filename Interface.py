

import PySimpleGUI as sg


class Interface:
    def __init__(self) -> None:
        sg.theme('darkblue13')
        sg.set_options(ttk_theme='alt')
        colors = ('red', 'blue', 'yellow', 'orange', 'green')
        line_styles = ('-', '--', '-.', ':')
        marker_styles = ('.', 'o', 'v', '^', 's', 'p')

        line1 = [sg.Text('Data Visualizer', justification= 'center', size=(80,1))]
        
        line2 = [sg.FileBrowse(target= 'file_location', size = (15,1), file_types=(("CSV files", ".csv"),)), 
                 sg.InputText(size=(60,1), key='file_location'), sg.Button("Load Dataset"), 
                 sg.Button("Load Representative Trajectory")]
        
        column1 = sg.Column([
            [sg.Text("Plot Dataset", size=(15,1)), sg.Checkbox('', key='plot_dataset')],
            [sg.Text("Color", size=(15, 1)), sg.Combo(colors, colors[0], key='dataset_color', readonly=True)],
            [sg.Text("Line Style", size=(15, 1)), sg.Combo(line_styles, line_styles[1], key='dataset_line_style', readonly=True)],
            [sg.Text("Plot Points", size=(15,1)), sg.Checkbox('', key='plot_dataset_points')],
            [sg.Text("Plot Text", size=(15,1)), sg.Checkbox('', key='plot_dataset_text')],
            [sg.Text("Marker Style", size=(15, 1)), sg.Combo(marker_styles, marker_styles[0], key='dataset_marker_style', readonly=True)],
        ])

        column2 = sg.Column([
            [sg.Text("Plot Representative Trajectory", size=(30,1)), sg.Checkbox('', key='plot_rep_traj')],
            [sg.Text("Color", size=(30, 1)), sg.Combo(colors, colors[1], key='rep_traj_color', readonly=True)],
            [sg.Text("Line Style", size=(30, 1)), sg.Combo(line_styles, line_styles[0], key='rep_traj_line_style', readonly=True)],
            [sg.Text("Plot Points", size=(30,1)), sg.Checkbox('', key='plot_rep_traj_points')],
            [sg.Text("Plot Text", size=(30,1)), sg.Checkbox('', key='plot_rep_traj_text')],
            [sg.Text("Marker Style", size=(30, 1)), sg.Combo(marker_styles, marker_styles[0], key='rep_traj_marker_style', readonly=True)],
        ])

        line3 = [column1, column2]
        
        line4 = [sg.Text("Displayed Semantic", size=(15, 1)), 
                 sg.Combo([], key='displayed_semantic', readonly=True, size=(15, 1)),
                 sg.Button("Plot Graphic"), sg.Button('Save Figure')]
        
        layout = [line1, line2, line3, line4]


        self.__window = sg.Window('Data Visualizer', layout)
    
    def update_semantics(self, semantics: list):

        self.__semantic_categories = [semantic[0] for semantic in semantics]#+['interval temporal']
        self.__window['displayed_semantic'].update(values=self.__semantic_categories, value=semantics[4])

    @property
    def window(self):
        return self.__window
    
    @property
    def semantics_categories(self):
        return self.__semantic_categories