'''
This function generates a 128 bit AES key
'''
import os
from cryptography.fernet import Fernet
import PySimpleGUI as sg

#This function get imported and called in the action_selection_menu_vGUI file
def encryption_key_generator():
    '''
    This function allows this program to be imported and used in another program
    '''
    recommended_folder = os.getcwd()

    #This is where each items of the window is assinged and given parameters,
    #such as color, size, key, font etc
    layout = [
        [sg.Text(
            'Welcome to the',
            font=('gill sans', 30),
            background_color='#b4f4fa',
            text_color='black')
        ],
        [sg.Text(
            'Pincode Generator',
            font=('impact', 45),
            background_color='#b4f4fa',
            text_color='black')
        ],
        [sg.Text(
            'What folder should the Key File be saved in?',
            background_color='#b4f4fa',
            text_color='black',
            font=('gill sans', 15)
        ),
        sg.FolderBrowse(
            key='where_to_save',
            initial_folder=recommended_folder,
            size=(7, 1),
            font=('gill sans', 15))
        ],
        [sg.Text(
            'What should the File be called?',
            background_color='#b4f4fa',
            text_color='black',
            font=('gill sans', 15))
        ],
        [sg.Input(
            key='-file_name-',
            enable_events=True,
            size=(55, 1)
        ),
        sg.Button(
            'Generate',
            font=('gill sans', 15),
            size=(8, 1))
        ],
        [sg.Button(
            'Go Back',
            font=('gill sans', 15),
            size=(7, 1))
        ],
    ]

    #Encryption key generation function
    def enc_key_gen():
        '''
        This function generates an encryption key using the Fernet.generate_key(),
        function from the cryptography.fernet library.
        It checks if the user has choosen a new folder to save the key file in,
        by checking if the new folder variable ''what_folder'' is an empty string,
        if it is not empty, it's value gets passed into the os.chdir() funtion,
        which then changes the output directory to the users choice.
        If it is empty the output directory will remain the same,
        which in this case is the working folder.

        Using the ''file_name'' variable the function creates a file with the .key extension,
        and then it writes the ''key'' variable into that file.
        The function then saves the file completing it's task.

        The file has the .key extension since it is reqiuerd by the cryptography.fernet library
        '''
        #This code generates a encryption key using the generate_key()
        #function from the cryptography.fernet libarary
        #And then assings the key to the key variable
        key = Fernet.generate_key()

        #This is variable contains the file path to the location
        #the user wants to save the key file to
        location = values['where_to_save']

        #This variable contains the name the user wants the key file to have
        name = values['-file_name-']

        #If this variable has the value '' the user has not
        #choosen a new location to save the file to,
        #the variable recommended_location will remain as the default location
        if location == '':
            #Skips without doing anything
            pass
        #If the user has choosen a new location to save the file to, this will be run
        else:
            #Changes the directory to the user choosen one
            os.chdir(location)

        #Here the function opens a key file in the user choosen location,
        #but since there is not key file with the user choosen name,
        #The function will create one instead
        #This code also assings the .key extension the the file name
        with open(name + '.key', 'wb') as mykey:
            #This code writes the data of the key variable to the new key file
            mykey.write(key)

    #this gives the window a name, layout, background color,
    #it decides how elemts should be alinged and lastly it sets a size.
    window  = sg.Window(
        "Start Meny",
        layout,
        background_color='#b4f4fa',
        element_justification='c',
        size=(800, 720)
    )
    #Event loop
    while True:
        #Gets events and value from the window
        event, values = window.read()
        #The first if checks if the winow is getting closed
        if event == sg.WIN_CLOSED or event == 'Go Back':
            break
        #If the generate button is pressed, this code will run
        if event == 'Generate':
            #If they user has not choosen a file name, they will be prompted with
            #a popup telling them to assign a name to the file
            if (values['-file_name-']) == '':
                #The popup
                sg.popup('You need to enter a name for the file!')
            #If the user has choosen a file name, the program will continue
            else:
                #This calls the encryption key generator function, which forces it to be run
                enc_key_gen()
                window['-file_name-'].update('')
                stored_locaion = values['where_to_save']
                #Gives the user a popup telling them where they stored the file
                sg.popup(f'The key file has been created and is stored here: {stored_locaion}')
    #Closes the window
    window.close()
