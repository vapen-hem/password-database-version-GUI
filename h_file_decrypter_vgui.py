'''

'''
import PySimpleGUI as sg
from cryptography.fernet import Fernet
import os

#Code Divider -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def file_decrypter():
    #This is where each items of the window is assinged and given parameters, such as color, size, key, font etc
    layout = [
        [sg.Text('Welcome to The file decrypter\n', background_color='#b4f4fa', text_color='black', font=('impact', 45))],
        [sg.Text('What file would you like to decrypt?           ', background_color='#b4f4fa', text_color='black', font=('gill sans', 15)), sg.Input(), sg.FileBrowse(key='-SELECTED_FILE-', size=(7, 1), font=('gill sans', 15))],
        [sg.Text('Select the Encryption Key File                   ', background_color='#b4f4fa', text_color='black', font=('gill sans', 15)), sg.Input(), sg.FileBrowse(key='-KEY_FILE-', size=(7, 1), font=('gill sans', 15))],
        [sg.Text('Where should the decrypted file be saved?', font=('gill sans', 15), text_color='Black', background_color='#b4f4fa'), sg.Input(), sg.FolderBrowse(key='-SAVE_LOCATION-', size=(7, 1), font=('gill sans', 15))],
        [sg.Text('Give the new file a name                          ', font=('gill sans', 15), text_color='Black', background_color='#b4f4fa'), sg.Input(key='-FILE_NAME-', size=(59,1))],
        [sg.Text('', background_color='#b4f4fa')],
        [sg.Text('Create an encrypted copy of the file?', font=('gill sans', 15), text_color='Black', background_color='#b4f4fa'), sg.OptionMenu(values=('Yes', 'No'), key='-DECD_YN-', text_color='White', background_color='#283b5b')],
        [sg.Text('', background_color='#b4f4fa')],
        [sg.Button('Decrypt Selected File', key='-DECT_FILE-', font=('gill sans', 15), size=(17, 1))],
        [sg.Text('', background_color='#b4f4fa')],
        [sg.Button('Go Back', font=('gill sans', 15), size=(7, 1))],
    ]

    #Code Divider -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #Decryption Function
    def decrypter():

        #These take the values guven by the user and assigns a variable to each value
        #What file should be derypted
        choosen_file = values['-SELECTED_FILE-']

        #What key file should be used to decrypt (Must be the same as the one used to encrypt)
        key_file     = values['-KEY_FILE-']

        #This will have one of the three following values 'Yes' 'No' ''.
        #If the value is yes, there WILL be a encrypted copy of the file
        #If the value if No, there will NOT be a encrypted copy of the file
        DECD_copy    = values['-DECD_YN-']

        #This is variable contains the file path to the location the user wants to save the file to
        location     = values['-SAVE_LOCATION-']
        
        #This variable contains the name the user wants the file to have
        name         = values['-FILE_NAME-']

        #Opens the user choosen file and reads it's data
        with open(choosen_file, 'rb') as og_text:
            #It then assings the data to the variable og_var
            og_var = og_text.read()
        
        #Opens the user choosen key file and reads it's data
        with open(key_file, 'rb') as Tkey:
            #It then assings the data to the variable key_var
            key_var = Tkey.read()
        
        #Here Fernet takes the key and reads it, and then it is assinged to the fernet_key variable
        fernet_key = Fernet(key_var)

        #Here the fernet_key variable is used to decrypt the data from the user choosen file
        decrypted = fernet_key.decrypt(og_var)



        #Both of the following options do basically the same task
        #If 'Yes', the program will leave the origional file alone
        if DECD_copy == 'Yes':
            #os.path.splittext is a function from the os librarry that split's the file extension from a file path
            #This C:\user\username\skrivbord\random_file.txt will turn into a list like this ['C:\user\username\skrivbord\random_file', '.txt']
            #As you can see the file extension has been seperated from the file path, allowiing the program to later assing it to the new file
            extension = os.path.splitext(choosen_file)
            #os.path.join is a function that joins directory/folder paths with file names, which alows the program to move files.
            #Here you can also see that the above variable(Tuple) 'extension' is used with the ending [1], this is done beacuse the file name choosen by the user
            #Does not contain a file extension, which is needed, but thanks to the os.path.splittext() function we now know what file extension the old file had
            #And can thus apply it to the new file name [1] is the index(location from start of tuple(basically a list)) of the file extension
            new_path = os.path.join(location, name+extension[1])

            #Here the function opens a file in the user choosen location, but since there is not file with the user choosen name,
            #The function will create one instead
            with open(new_path, 'wb') as asd_text:
                #This code writes the data of the decrypted file to the new file
                asd_text.write(decrypted)

        #If 'No', the program will delete the origional file
        elif DECD_copy == 'No':
            #os.path.splittext is a function from the os librarry that split's the file extension from a file path
            #This C:\user\username\skrivbord\random_file.txt will turn into a list like this ['C:\user\username\skrivbord\random_file', '.txt']
            #As you can see the file extension has been seperated from the file path, allowiing the program to later assing it to the new file
            extension = os.path.splitext(choosen_file)
            #os.path.join is a function that joins directory/folder paths with file names, which alows the program to move files.
            #Here you can also see that the above variable(Tuple) 'extension' is used with the ending [1], this is done beacuse the file name choosen by the user
            #Does not contain a file extension, which is needed, but thanks to the os.path.splittext() function we now know what file extension the old file had
            #And can thus apply it to the new file name [1] is the index(location from start of tuple(basically a list)) of the file extension
            new_path = os.path.join(location, name+extension[1])

            #Here the function opens a file in the user choosen location, but since there is not file with the user choosen name,
            #The function will create one instead
            with open(new_path, 'wb') as asd_text:
                #This code writes the data of the decrypted file to the new file
                asd_text.write(decrypted)

            #Since the user choose to not keep the old file,
            #This code will delete the old file
            os.remove(choosen_file)



    #Code Divider -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



    #Creates a window variable, here you assing layout, background color, any element justification and lastly size
    window  = sg.Window("Start Meny", layout, background_color='#b4f4fa', element_justification='c', size=(1080, 720))

    #This is the event loop
    while True:
        #Reads events such as button presses, or inout entries, and checks for value of items
        event, values = window.read()
        #If the X is hit or the go Back button is pressed the window will close
        if event == sg.WIN_CLOSED or event == 'Go Back':
            #Stops the loop
            break

        #This code will be run if the user clicks the decrypt file button
        if event == '-DECT_FILE-':
            #This calls the decryption function which makes it run
            decrypter()
    #This code kills the window
    window.close()