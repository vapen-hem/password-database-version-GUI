'''
This function has not been worked in yet
'''
import hashlib
import bcrypt
import PySimpleGUI as sg
from cryptography.fernet import Fernet

layout = [
    [sg.Text('Welcome to the', font=('gill sans', 30), background_color='#b4f4fa', text_color='black')],
    [sg.Text('Database', font=('impact', 45), background_color='#b4f4fa', text_color='black')],
    [sg.Button('Go Back', font=('gill sans', 15), size=(7, 1))],
]

window  = sg.Window("Start Meny", layout, background_color='#b4f4fa', element_justification='c', size=(800, 720))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Go Back':
        break
            
window.close()
