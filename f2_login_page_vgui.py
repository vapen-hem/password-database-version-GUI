import bcrypt
import PySimpleGUI as sg
import os
import time
from f1_user_creation_vgui import user_creation_main

def user_verification_main():
    #The layout of the window
    layout = [
        [sg.Text('Welcome to the', font=('gill sans', 30), background_color='#b4f4fa', text_color='black')],
        [sg.Text('User creation', font=('impact', 45), background_color='#b4f4fa', text_color='black')],
        [sg.Text('', background_color='#b4f4fa')],
        [sg.Text('', background_color='#b4f4fa')],
        [sg.Text(
            'Username',
            font=('gill sans', 20),
            background_color='#b4f4fa',
            text_color='black',
        ),
        sg.Input(
            key='usrnm',
            enable_events=True,
        )],
        [sg.Text(
            'Password ',
            font=('gill sans', 20),
            background_color='#b4f4fa',
            text_color='black',
        ),
        sg.Input(
            key='pwd',
            enable_events=True,
            password_char='*',
        )],
        [sg.Button(
            'Login',
            key='login'
        ),
        sg.Button(
            'Create User',
            key='create_user'
        )],
        [sg.Button('Go Back', font=('gill sans', 15), size=(7, 1))],
    ]

    #The function that verifyies the user
    def user_verification():
        #The user entered username
        username_input = values['usrnm']
        username_correct_format = username_input + '.txt'
        #The user enetered password
        password_input = values['pwd']

        #Changes dir to current working
        os.chdir('./')
        #Ignore this, it will be changed
        os.chdir('./users')

        #Get's every file and dir in the current directory into a list
        what_file = os.listdir()
        i = 0
        #Counts how many files and dirs are in the current directory
        list_length = len(what_file)
        #this loop is repeated as many times are there are files and dirs in this directory
        for i in range(list_length):
            #Checks if the username fil is in the curernt dir
            if username_correct_format in what_file[i]:
                #If the username is found, the_file variable get assigned that file name.
                the_file = what_file[i]
                #Leaves loop
                break
            else:
                i += 1

        #Get's the current directory file path
        cwd = os.getcwd()

        #add the file to the file path
        get_this_file = cwd + '\\' + the_file

        #opens file using file path
        with open(get_this_file) as random_var:
            #reads file data and assings it to a variable
            user_info_unfinished = random_var.readlines()
            #Says that the password is the third line
            hashed_password = user_info_unfinished[2]
            #Cleans variabel so that only the password remains
            hashed_password = hashed_password.replace(' ', '')
            #Cleans variabel so that only the password remains
            hashed_password = hashed_password.replace('\n', '')
            #Cleans variabel so that only the password remains
            hashed_password = hashed_password.replace("b'", '')
            #Cleans variabel so that only the password remains
            hashed_password = hashed_password.replace("'", '')

        #encodes the hashed password using utf-8
        hashed_password_bytes = hashed_password.encode('utf-8')

        #encodes the user inputed password uding utf-8
        userBytes = password_input.encode('utf-8')

        #If the user inouted password matches the stored one, this variable will be True.
        result = bcrypt.checkpw(userBytes, hashed_password_bytes)

        if result == True:
            #if passwords match
            sg.popup('User Confirmed')
        else:
            #If they don't match
            sg.popup('Wrong password, wait 3 seconds and try again')

    window  = sg.Window("Start Meny", layout, background_color='#b4f4fa', element_justification='c', size=(800, 720))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Go Back':
            break
        if event == 'login':
            user_verification()
        if event == 'create_user':
            user_creation_main()
                
    window.close()
