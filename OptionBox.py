

import PySimpleGUI as sg
from AbstractWidget import AbstractWidget


colors = ('red', 'blue', 'yellow', 'orange', 'green')
line_styles = ('-', '--', '-.', ':')
point_styles = ('.', 'o', 'v', '^', 's', 'p')


class OptionBox(AbstractWidget):
    def __init__(self, name : str) -> None:

        self.__name = name

        self.__elements = [[sg.Checkbox(name.capitalize(), key=name, background_color='#7A7A7A', default=True)],
                    [sg.Checkbox('Line', key=name+'_line', size=(7,1), background_color='#7A7A7A'), 
                     sg.Combo(colors, colors[0], key=name+'_color', readonly = True), 
                     sg.Combo(line_styles, line_styles[0], key=name+'_line_style', readonly = True)],
                    [sg.Checkbox('Point', key=name+'_point', size=(7,1), background_color='#7A7A7A'),  
                     sg.Combo(point_styles, point_styles[0], key=name+'_point_style', readonly = True)],
                    [sg.Checkbox('Text', key=name+'_text', size=(7,1), background_color='#7A7A7A'),  
                     sg.Combo([], key=name+'_semantic', size=(15,1), readonly = True)]
                   ]
        self.__layout = sg.Column(self.__elements, background_color='#7A7A7A')
    
    def update_semantic(self, semantics):
        self.__elements[3][1].update(values=semantics, value=semantics[0])
    
    @property
    def layout(self):
        return self.__layout