'''
Here the user will be able to create a new user,
after creation the users data will be stored in the users folder,
with their username as the file name.
'''
import bcrypt
import PySimpleGUI as sg
import os

#This is the character that replaces the symbols in the Password inputs
pass_char_rep = '*'

def user_creation_main():
    '''
    The main function
    '''
    #This is the window layout
    layout = [
        [sg.Text('Welcome to the', font=('gill sans', 30), background_color='#b4f4fa', text_color='black')],
        [sg.Text('User creation', font=('impact', 45), background_color='#b4f4fa', text_color='black')],
        [sg.Text('', background_color='#b4f4fa')],
        [sg.Text('', background_color='#b4f4fa')],
        [sg.Text(
            '           Username',
            font=('gill sans', 20),
            background_color='#b4f4fa',
            text_color='black',
        ),
        sg.Input(
            key='usrnm',
            enable_events=True,
        )],
        [sg.Text(
            '            Password',
            font=('gill sans', 20),
            background_color='#b4f4fa',
            text_color='black',
        ),
        sg.Input(
            key='pwd',
            enable_events=True,
            password_char=(pass_char_rep),
        )],
        [sg.Text(
            'Repeat Password',
            font=('gill sans', 20),
            background_color='#b4f4fa',
            text_color='black',
        ),
        sg.Input(
            key='re-pwd',
            enable_events=True,
            password_char=(pass_char_rep),
        )],
        [sg.Checkbox('', key='show_pwd', enable_events=True)],
        [sg.Button(
            'Create',
            key='create'
        )],
        [sg.Button('Go Back', font=('gill sans', 15), size=(7, 1))],
    ]

    #This is the function that creates the user
    def usr_create():
        '''
        This function creates the user
        '''
        #chages the variable so that it is addable to the file path
        file_name = '\\' + values['usrnm'] + '.txt'
        #Where the files will be stores, this will change ignore this
        os.chdir('.\\')
        file_path_finder = os.getcwd()
        location = file_path_finder + "\\users" + file_name
        #Assings the user input password to the password variable
        password = values['pwd']
        #Encodes the password
        bytes_pwd = password.encode('utf-8')
        #The salt used
        salt = bcrypt.gensalt()
        #Hashes the password using the salt
        hashedpwd = bcrypt.hashpw(bytes_pwd, salt)
        #Adds the username and variable to the user_info varible which will be written to the file
        user_info = f'''
        {values['usrnm']}
        {hashedpwd}
        '''
        #Encodes the user info
        user_info_bytes = bytes(user_info, 'utf-8')
        with open(location, 'wb') as b_location:
            b_location.write(user_info_bytes)
        sg.popup('User has been created')
        window.close()

    window  = sg.Window("Start Meny", layout, background_color='#b4f4fa', element_justification='c', size=(800, 720))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Go Back':
            break
        if event == 'create':
            if values['pwd'] == values['re-pwd']:
                usr_create()
            else:
                sg.popup('Passwords do not match')

    window.close()
