'''
This module allows the user to create a pincode through a GUI

The librarys used are: PySimpleGui, secrets, sklearn.utils

secrets is used for it's .choice function, Unlike the built in random.choice function
the .choice is cryptographically safe.

skleanr.utils is used for it's .shuffle function, Unlike the built in shuffle function
the .shuffle is cryptographically safe.

PySimpleGui is used to make the GUI
'''
#Replacement for the random module, Random is not crytpographically safe, since it uses sudeorandom
import secrets
#Cruptographically safe list shuffler
import sklearn.utils
#GUI Library
import PySimpleGUI as sg

#Alows the code to be called in another file
def pincode_generator():
    '''
    This module allows the user to create a pincode, via a GUI
    '''
    #The window layout
    layout = [
        [sg.Text('Welcome to the',
        font=('gill sans', 30),
        background_color='#b4f4fa',
        text_color='black')
        ],
        [sg.Text('Pincode Generator',
        font=('impact', 45),
        background_color='#b4f4fa',
        text_color='black')
        ],
        [sg.Text('How long should the pincode be?',
        background_color='#b4f4fa',
        text_color='black')
        ],
        [sg.Multiline(key='-IN-',
        enable_events=True,
        size=(34, 1),
        no_scrollbar=True
        ),
        sg.Button('Enter',
        key='ENTER',
        font=('gill sans', 15))
        ],
        [sg.Text('This is your pincode',
        font=('gill sans', 12),
        background_color='#b4f4fa',
        text_color='grey')
        ],
        [sg.Input(key='-OUT-',
        enable_events=True)
        ],
        [sg.Button('Go Back',
        font=('gill sans', 15),
        size=(7, 1))
        ],
    ]

    #The pincode generation function
    def pingen():
        '''
        This is the pincode generation function.

        During the pincodes creation all the numbers are astored in the "pincode" list.

        The function gets the user choosen length from the input with the key "-IN-",
        and stores it in the length variable.

        the available numbers are stored in the "list_123" list

        The reason for "_" being used instead of "i" in the for loops is becasue,
        pylint complains that,the "i" is an unused variable.

        The length variable is used to run a for loop as many times as the pincode length.
        Each time the loop is ran the it picks a number from the "litst_123" randomly,
        using the .choice function from the secrets library
        the loop then appends the choosen number to the list.

        After the for loop has completed all of it's runs, the function shuffles the pincode list,
        using the sklearn.utils librarys .shuffle function.
        The function then removes all ' and , in the list, which leave it with a single value,
        Which is the full and completed pincode

        It then returns the pincode as the functions value
        '''
        pincode = []
        length = int(values['-IN-'])
        list_123 = ['0','1','2','3','4','5','6','7','8','9']
        for _ in range(length):
            number = ''.join(secrets.choice(list_123))
            pincode.append(number)
        pincode = sklearn.utils.shuffle(pincode)
        pincode = ''.join(pincode)
        return pincode

    window  = sg.Window("Start Meny", layout, background_color='#b4f4fa', element_justification='c', size=(800, 720))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Go Back':
            break
        if event == 'ENTER':
            if str(values['-IN-']).isdigit():
                window['-OUT-'].update(pingen())
                window['-IN-'].update('')
            else:
                window['-IN-'].update('')
                sg.popup('You can only enter numbers')

    window.close()
