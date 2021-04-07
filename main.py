import PySimpleGUI as sg
import comportement

test = comportement.moveAnt()

layout = [[sg.Text("Valeur de x : "+ str(test.x) +" . Et valeur de y : "+ str(test.y))], [sg.Button("Close window")]]

window = sg.Window("test", layout, margins=(300,150))

while True:
    event, values = window.read()
    if event == "Close window" or event == sg.WIN_CLOSED:
        break

window.close()