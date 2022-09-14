from tkinter.colorchooser import *


def choice_color(event):
    from view.gui import line_color

    color = askcolor()
    # print(color)
    line_color.config(bg=color[1])
    # print(line_color.cget("bg"))
