from functions import fetch_todos, write_todos
import FreeSimpleGUI as sg

layout = [[sg.Text("What's your name?")],     # Part 2 - The Layout
            [sg.Input()],
            [sg.Button('Ok')] ]
window = sg.Window("My todo App", layout)
event, values = window.read()
try:
    if len(values[0]) > 0:
        print(values)
        window.close()
except ValueError:
    print("Add a value")
    window.close()

