

import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MainInterface:
    def __init__(self) -> None:
        sg.theme('systemdefault')
        sg.set_options(ttk_theme='alt')
        colors = ('red', 'blue', 'yellow', 'orange', 'green')
        line_styles = ('-', '--', '-.', ':')
        marker_styles = ('.', 'o', 'v', '^', 's', 'p')

        op_line_1 = [sg.Input(key='dataset_path', visible=False, enable_events=True), sg.FileBrowse('Dataset', size=(15,1)),
            sg.Checkbox('Dataset', key='plot_dataset', size=(7,1)),
            sg.Checkbox('Points', key='plot_dataset_points', size=(7,1)),
            sg.Checkbox('Text', key='plot_dataset_text'),
            sg.Text("Color", size=(7, 1), justification='r'), sg.Combo(colors, colors[0], key='dataset_color', readonly=True),
            sg.Text("Line", size=(7, 1), justification='r'), sg.Combo(line_styles, line_styles[1], key='dataset_line_style', readonly=True),
            sg.Text("Marker", size=(7, 1), justification='r'), sg.Combo(marker_styles, marker_styles[0], key='dataset_marker_style', readonly=True),
            sg.Combo([], key='displayed_semantic', readonly=True, size=(15, 1))]

        op_line_2 = [sg.Input(key='r-mat_path', visible=False, enable_events=True), sg.FileBrowse('R-MAT', size=(15,1)),
            sg.Checkbox('R-MAT', key='plot_rep_traj', size=(7,1)),
            sg.Checkbox('Points', key='plot_rep_traj_points', size=(7,1)),
            sg.Checkbox('Text', key='plot_rep_traj_text'),
            sg.Text("Color", size=(7, 1), justification='r'), sg.Combo(colors, colors[0], key='rep_traj_color', readonly=True),
            sg.Text("Line", size=(7, 1), justification='r'), sg.Combo(line_styles, line_styles[1], key='rep_traj_line_style', readonly=True),
            sg.Text("Marker", size=(7, 1), justification='r'), sg.Combo(marker_styles, marker_styles[0], key='rep_traj_marker_style', readonly=True)]

        line1 = [op_line_1, op_line_2]

        filter_stack = []
        filter_tab = [[sg.InputText(key="command_line", size=(20,1))], 
                      [sg.Column(filter_stack, scrollable=True, vertical_scroll_only=True, justification='r')]]

        self.__figure_canvas_agg = None
        graph_area = [[sg.Canvas(key='graphCanvas')],
                      [sg.Button('Reset', size=(10,1), key='reset_graph'),
                       sg.Button('Plot', size=(10,1), key="plot_graph"), 
                       sg.Input(key='save_graph', visible=False, enable_events=True), 
                       sg.SaveAs('Save', size=(10,1), file_types=(('JPEG', '.jpeg'), ('PNG', '.png'), ('PDF', '.pdf')))]]
        line2 = [sg.Column(filter_tab, vertical_alignment='top', expand_y=True), sg.Column(graph_area, element_justification='r')]

        layout = [line1, line2]

        self.__window = sg.Window('Data Visualizer', layout, resizable=True, finalize=True)
    
    def update_semantics(self, semantics: list):

        self.__semantic_categories = [semantic[0] for semantic in semantics]#+['interval temporal']
        self.__window['displayed_semantic'].update(values=self.__semantic_categories, value=semantics[4])

    def draw_figure(self, figure):
        if(self.__figure_canvas_agg):
            self.__figure_canvas_agg.get_tk_widget().forget()
        self.__figure_canvas_agg = FigureCanvasTkAgg(figure, self.__window['graphCanvas'].TKCanvas)
        self.__figure_canvas_agg.draw()
        self.__figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=0)
        return self.__figure_canvas_agg

    @property
    def window(self):
        return self.__window
    
    @property
    def semantics_categories(self):
        return self.__semantic_categories