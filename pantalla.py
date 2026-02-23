import PySimpleGUI as sg

layout = [[sg.Button('Ejecutar')]]

window = sg.Window('Mi Aplicación', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()