'''
This is main menu of the Password database GUI

This program has a encrypted database for storing passwords,
a password generator,
a pincode generator,
a AES 128 bit key generator,
a file encrypter
and a file decrypter2

The login system is not yet finished, it can currently create news users, verify passwords, and store passwords in "safely"?
The different users are stored in the users folder
The current goals for the login system is
    * Make each user file have a more informtion about their account

The how to use function is not yet finished,
it will show with pictures and text how the program works and how to use it

The Database is not yet completed in the GUI version, but is completed in the Terminal version
    
From this window the user will be able to interact with all other parts of the program
'''
#The GUI library
import PySimpleGUI as sg
#Future how to use import
""" #from b_how_to_use_vgui import * """
#Imports the password generator function
from c_password_generator_vgui import password_generator
#Imports the pincode generator function
from d_pincode_generator_vgui import pincode_generator
#Imports the encryption key function
from e_encryption_key_generator_vgui import encryption_key_generator
#Imports the user verification function
from f2_login_page_vgui import user_verification_main
#Imports the file encrypter function
from g_file_encrypter_vgui import file_encrypter
#Imports the file decryption function
from h_file_decrypter_vgui import file_decrypter

#I have put these here because it makes the code alot cleaner
button1 = 'How to Use'
button2 = 'Create Password'
button3 = 'Create Pincode'
button4 = 'Create Encryption Key'
button5 = 'See Database'
button6 = 'Encrypt a File'
button7 = 'Decrypt a File'
button8 = 'Exit'

#The window layout
layout = [
    [sg.Text('Welcome to Winther Storage\n', background_color='#b4f4fa', text_color='black', font=('impact', 45))],
    [sg.Button(button1, font=('gill sans', 20), key='B1', size=(20, 1))],
    [sg.Button(button2, font=('gill sans', 20), key='B2', size=(20, 1))],
    [sg.Button(button3, font=('gill sans', 20), key='B3', size=(20, 1))],
    [sg.Button(button4, font=('gill sans', 20), key='B4', size=(20, 1))],
    [sg.Button(button5, font=('gill sans', 20), key='B5', size=(20, 1))],
    [sg.Button(button6, font=('gill sans', 20), key='B6', size=(20, 1))],
    [sg.Button(button7, font=('gill sans', 20), key='B7', size=(20, 1))],
    [sg.Button(button8, font=('gill sans', 20), key='B8', size=(20, 1))],
]

#The window variable
window  = sg.Window("Start Meny", layout, background_color='#b4f4fa', element_justification='c', size=(800, 720))

#Event loop
while True:
    event, values = window.read()
    #If the cancel(Exit) button is pressed, the window will terminate itself
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'B1':
        #Does not exist yet
        #If button 1 is pressed, the how to use window will be started
        pass
    elif event == 'B2':
        #If button 2 is pressed, the password generator is started
        password_generator()
    elif event == 'B3':
        #If button 3 is pressed, the pincode generator is started
        pincode_generator()
    elif event == 'B4':
        #If button 4 is pressed, the encryption key generator is started
        encryption_key_generator()
    elif event == 'B5':
        #Not yet complete
        #If button 5 is pressed, user verification is started
        user_verification_main()
    elif event == 'B6':
        #If button 6 is pressed, the file encrypter is started
        file_encrypter()
    elif event == 'B7':
        #If button 7 is pressed, the file decrypter is started
        file_decrypter()
    elif event == 'B8':
        #If button 8 is pressed, the program will terminate itself
        break

#Closes the window
window.close()
