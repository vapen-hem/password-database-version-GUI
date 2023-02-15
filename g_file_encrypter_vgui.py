'''
This module allows the user to encrypt a file through a GUI

The librarys used are: os, cryptography.fernet, PySimpleGUI
The module used is: e_encryption_key_generator_vgui

os is used for the file path maniplultaion

cryptography.fernet is used for it's .encrypt function

PySimpleGUI is used to make the GUI

e_encryption_key_generator_vgui is used for it's encryption key generator.
'''
import os
from cryptography.fernet import Fernet
from e_encryption_key_generator_vgui import encryption_key_generator
import PySimpleGUI as sg

def file_encrypter():
    '''
    This module allows thw user to encrypt files using a GUI
    '''
    #The window
    layout = [
        [sg.Text(
            'Welcome to The file encrypter\n',
            background_color='#b4f4fa',
            text_color='black',
            font=('impact', 45))
        ],
        [sg.Text(
            'What file would you like to encrypt?           ',
            background_color='#b4f4fa', text_color='black',
            font=('gill sans', 15)
        ),
        sg.Input(

        ),
        sg.FileBrowse(
            key='-SELECTED_FILE-',
            size=(7, 1),
            font=('gill sans', 15))
        ],
        [sg.Text(
            'Select the Encryption Key File                   ',
            background_color='#b4f4fa',
            text_color='black',
            font=('gill sans', 15)
        ),
        sg.Input(

        ),
        sg.FileBrowse(
            key='-KEY_FILE-',
            size=(7, 1),
            font=('gill sans', 15))
        ],
        [sg.Text(
            'Where should the encrypted file be saved?',
            font=('gill sans', 15), text_color='Black',
            background_color='#b4f4fa'
        ),
        sg.Input(

        ),
        sg.FolderBrowse(
            key='-SAVE_LOCATION-',
            size=(7, 1),
            font=('gill sans', 15))
        ],
        [sg.Text(
            'Give the new file a name                          ',
            font=('gill sans', 15), text_color='Black',
            background_color='#b4f4fa'
        ),
        sg.Input(
            key='-FILE_NAME-',
            size=(59,1))
        ],
        [sg.Text(
            '',
            background_color='#b4f4fa')
        ],
        [sg.Text(
            "Don't have a key? Click here",
            font=('gill sans', 15),
            text_color='Black',
            background_color='#b4f4fa'
        ),
        sg.Button(
            'Create Encryption Key',
            font=('gill sans', 15))
        ],
        [sg.Text(
            'Create an unencrypted copy of the file?         ',
            font=('gill sans', 15), text_color='Black',
            background_color='#b4f4fa'
        ),
        sg.OptionMenu(
            values=('Yes', 'No'),
            key='-UNENCD_YN-',
            text_color='White',
            background_color='#283b5b')
        ],
        [sg.Text(
            '',
            background_color='#b4f4fa')
            ],
        [sg.Button(
            'Encrypt Selected File',
            key='-ENCT_FILE-',
            font=('gill sans', 15),
            size=(17, 1))
            ],
        [sg.Text(
            '',
            background_color='#b4f4fa')
        ],
        [sg.Button(
            'Go Back',
            font=('gill sans', 15),
            size=(7, 1))
        ],
    ]

    def encrypter():
        '''
        This is the encryption function

        The function get's the user choosen file from the filebrowse,
        with the key "-SELECTED_FILE-" and then stores it in the choosen_file variable

        The function get's the user choosen key file from the filebrowse,
        with the key "-KEY_FILE-" and then stores it in the key_file variable

        In the gui there is a option menu where the user can choose between wheater,
        they want an unecrypted copy of the file or not.
        Yes = they want an unecrypted copy
        No = they don't want an unecrypted copy
        If the user has not choosen an option a popup will apear,
        promting the user to choose one.
        The code that checks if the user has choosen yes or no,
        is in the event handler.
        The function then takes the value of the options menu with the key,
        "-UNENCD_YN-" This stand for UNENCrypteD_YesNo

        The function get's the user choosen file save location from the filebrowse,
        with the key "-SAVE_LOCATION-" and then stores it in the location variable

        The function get's the user choosen file name from the input,
        with the key "-FILE_NAME-" and then stores it in the name variable

        Using the built open() function the encrypter() function opens the,
        user choosen file in "rb" mode (Read in Binary mode) with the variable name og_text
        it then reads the og_text variable using the built in .read() function
        and then assings it to the og_var variable

        Using the open() function the encrypter() function opens the,
        user key file in "rb" mode (Read in Binary mode) with the variable name the_key
        it then reads the the_key variable using the built in .read() function
        and then assings it to the key_var variable

        Using the cryptography.fernet library's Fernet() function the encrypter(),
        function does stuff?(I don't what it actually does, but it has to be done),
        and assings it to the fernet_key variable

        Then using the cryptography.fernet library's .encrypt() function the encrypter(),
        function encrypts the files data and stores it in the encrypted variable.

        Read green comments for the IF/ELIF part
        '''

        choosen_file = values['-SELECTED_FILE-']

        key_file = values['-KEY_FILE-']

        UNENCD_copy  = values['-UNENCD_YN-']

        location = values['-SAVE_LOCATION-']

        name  = values['-FILE_NAME-']

        #Opens the user choosen file and reads it's data
        with open(choosen_file, 'rb') as og_text:
            #It then assings the data to the variable og_var
            og_var = og_text.read()

        #Opens the user choosen key file and reads it's data
        with open(key_file, 'rb') as the_key:
            #It then assings the data to the variable key_var
            key_var = the_key.read()

        #Here Fernet takes the key and reads it,
        #and then it is assinged to the fernet_key variable
        fernet_key = Fernet(key_var)

        #Here the fernet_key variable is used to decrypt,
        #the data from the user choosen file
        encrypted = fernet_key.encrypt(og_var)


        #Both of the following options do basically the same task
        #If 'Yes', the program will leave the origional file alone
        if UNENCD_copy == 'Yes':
            extension = os.path.splitext(choosen_file)
            new_path = os.path.join(location, name+extension[1])

            with open(new_path, 'wb') as asd_text:
                asd_text.write(encrypted)

        #If 'No', the program will delete the origional file
        elif UNENCD_copy == 'No':
            #os.path.splittext is a function from the os library,
            #that split's the file extension from a file path
            #This C:\user\username\skrivbord\random_file.txt will turn into,
            # a list like this ['C:\user\username\skrivbord\random_file', '.txt']
            #As you can see the file extension has been seperated from the,
            #file path, allowing the program to later assing it to the new file
            extension = os.path.splitext(choosen_file)
            #os.path.join is a function that joins directory/folder paths with file names,
            #which alows the program to move files.
            #Here you can also see that the above variable(Tuple) 'extension' is used with the ending [1],
            # this is done beacuse the file name choosen by the user
            #Does not contain a file extension, which is needed, but thanks to the os.path.splittext(),
            #function we now know what file extension the old file had
            #And can thus apply it to the new file name [1] is the,
            #index(location from start of tuple(basically a list)) of the file extension
            new_path = os.path.join(location, name+extension[1])

            #Here the function opens a file in the user choosen location,
            # but since there is not file with the user choosen name,
            #The function will create one instead
            with open(new_path, 'wb') as asd_text:
                #This code writes the data of the decrypted file to the new file
                asd_text.write(encrypted)

            #Since the user choose to not keep the old file,
            #This code will delete the old file
            os.remove(choosen_file)

    #Creates a window variable, here you assing layout,
    #background color, any element justification and lastly size
    window  = sg.Window(
        "Start Meny",
        layout,
        background_color='#b4f4fa',
        element_justification='c',
        size=(1080, 720)
    )

    #This is the event loop
    while True:
        #Reads events such as button presses,
        #or inout entries, and checks for value of items
        event, values = window.read()
        #If the X is hit or the go Back button is pressed the window will close
        if event == sg.WIN_CLOSED or event == 'Go Back':
            #Stops the loop
            break
        #This code will be run if the user clicks the encrypt file button
        if event == '-ENCT_FILE-':
            #Checks if the user has deicded if they want to keep os delete the origional file
            #If the value is blank('') the user will be shown a popup which prompts them to make a decision
            #The program will not continue unless Yes or No is choosen
            if (values['-UNENCD_YN-']) == '':
                sg.popup('''
                    You have to select if you want an unecrypted version of the file!
                    Yes means that an unencrypted copy WILL be made
                    No means that an unecrypted copy will NOT be made
                ''')
            #If the user had decided, the encryption function will be run
            else:
                #This calls the encryption function which makes it run
                encrypter()
        #If the user does not have an encryption key, they can create one using this button
        #Pressing the button will launch the encryption_key_generator(),
        #function from the E_encryption_key_generator_vGUI.py file
        if event == 'Create Encryption Key':
            #Alows the user to create an encryption key
            encryption_key_generator()
    #This code kills the window
    window.close()
