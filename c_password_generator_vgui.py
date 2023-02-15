'''
This module allows the user to create a password that is bruteforce safe
through a GUI.

There is a Advanced and Simple option.

The librarys used are: string, secrets, sklean.utils, PySimpleGui

string is used for it's ascii modules

secrets are used for it's .choice function, Unlike the built in random.choice function
the .choice is cryptographically safe.

skleanr.utils is used for it's .shuffle function, Unlike the built in shuffle function
the .shuffle is cryptographically safe.

PySimpleGui is used to make the GUI
'''
#Import for ascii modules
import string
#Replacement for the random module, Random is not crytpographically safe, since it uses sudeorandom
import secrets
#Cruptographically safe list shuffler
import sklearn.utils
#GUI Library
import PySimpleGUI as sg

#Alows the code to be called in another file
def password_generator():
    '''
    This module allows the user to create a password that should be bruteforce safe, via a GUI
    '''
    #The Main window function
    def make_win_1():
        '''
        This is the Main window, here the user can choose between,
        Simple and Advanced Generation
        '''
        #The Main window layout
        layout = [
            [sg.Text('Welcome to the',
            font=('gill sans', 30),
            background_color='#b4f4fa',
            text_color='black')
            ],
            [sg.Text('Password Generator',
            font=('impact', 45),
            background_color='#b4f4fa',
            text_color='black')
            ],
            [sg.Button('Simple Generation',
            font=('gill sans', 25)
            ),
            sg.Button('Advanced Generation',
            font=('gill sans', 25))
            ],
            [sg.Text('''
            They are equaly safe, Advanced just gives 
                    you more customizability
            ''',
            font=('gill sans', 20),
            background_color='#b4f4fa',
            text_color='grey')
            ],
            [sg.Button('Go Back',
            font=('gill sans', 15),
            size=(7, 1))
            ],
        ]
        return sg.Window("Start Meny",
        layout, background_color='#b4f4fa',
        element_justification='c',
        size=(800, 720),
        finalize=True
        )

    #The Simple generation window function
    def make_win_2():
        '''
        This is the Simple generation window, here the user only chooses the length of the password,
        And then the program does the rest.
        '''
        #The Simple generation window layout
        layout = [
            [sg.Text('Simple Generation',
            font=('gill sans', 30),
            background_color='#b4f4fa',
            text_color='black')
            ],
            [sg.Button('Go Back',
            font=('gill sans', 15),
            size=(7, 1))
            ],
            [sg.Input(key='-IN-',
            enable_events=True)
            ],
            [sg.Button('Enter',
            key='enter_simple',
            font=('gill sans', 15))
            ],
            [sg.Text('This is your password',
            font=('gill sans', 15),
            background_color='#b4f4fa',
            text_color='grey')
            ],
            [sg.Input(key='-OUT-',
            enable_events=True)
            ],
        ]
        return sg.Window("Start Meny",
        layout, background_color='#b4f4fa',
        element_justification='c',
        size=(800, 720),
        finalize=True
        )

    #The Advanced generation window function
    def make_win_3():
        '''
        This is the Advanced generation window, here the user can choose how many,
        uppercase letters, lowercase letters, numbers and special chars,
        the password should contain.
        '''
        #The Advanced generation window layout
        layout = [
            [sg.Text('Advanced Generation',
            font=('gill sans', 30),
            background_color='#b4f4fa',
            text_color='black')
            ],
            [sg.Button('Go Back',
            font=('gill sans', 15),
            size=(7, 1))
            ],
            [sg.Text('I recommend using atleast 5 of each option',
            font=('gill sans', 15),
            background_color='#b4f4fa',
            text_color='grey')
            ],
            [sg.Text('Uppercase',
            background_color='#b4f4fa',
            text_color='black'
            ),
            sg.Input(key='-IN1-',
            enable_events=True)
            ],
            [sg.Text('Lowercase',
            background_color='#b4f4fa',
            text_color='black'
            ),
            sg.Input(key='-IN2-',
            enable_events=True)
            ],
            [sg.Text('Number    ',
            background_color='#b4f4fa',
            text_color='black'
            ),
            sg.Input(key='-IN3-',
            enable_events=True)
            ],
            [sg.Text('Special    ',
            background_color='#b4f4fa',
            text_color='black'
            ),
            sg.Input(key='-IN4-',
            enable_events=True)
            ],
            [sg.Text('This is your password                ',
            font=('gill sans', 12),
            background_color='#b4f4fa',
            text_color='grey')
            ],
            [sg.Input(key='-OUT-',
            enable_events=True
            ),
            sg.Button('Enter',
            key='enter_advanced',
            font=('gill sans', 15))
            ],
        ]
        return sg.Window("Start Meny",
        layout, background_color='#b4f4fa',
        element_justification='c',
        size=(800, 720), finalize=True
        )

    #The Simple generation function
    def passgen_simple():
        '''
        This is the Simple generation function

        During the passwords creation all it's,
        letters, number and special chars are stored in a list named "password"

        The function gets the user choosen length from the input with the key "-IN-",
        and stores it in the "length" variable.

        The available numbers and special chars are specified in the,
        "numbers" and "special_chars" respectively

        The reason for "_" being used instead of "i" in the for loops is becasue,
        pylint complains that,the "i" is an unused variable.

        The "length" variable is used to run a for loop for as many times as the passwords length.
        Each time it is ran, it picks a a number between 1 and 3, if the number is
        1: The "bokstav" function is ran
        2: The "nummer" function is ran
        3: The "special" function is ran

        The "bokstav" function chooses a big or small letter,
        and then appends it to the "password" list,
        every time it is ran. Bokstav is letter in swedish

        The "nummer" function chooses a number between 0 - 9,
        and then appends it to the "password" list,
        every time it is ran. Nummer is number in swedish

        The "special" function chooses one of the special chars in the special chars list,
        and then appends it to the "password" list, every timme it is ran.
        Special is spelled the same in English and Swedish

        After the for loop has completed all of it's runs, the function shuffles the password list,
        using the sklearn.utils librarys .shuffle function.
        The function then removes all ' and , in the list, which leave it with a single value,
        Which is the full and completed pasword

        It then returns the password as the functions value
        '''
        #The password is stored here trough out the generation process
        password = []
        #Length of password
        length = int(values['-IN-'])
        #Available numbers
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        #Available special chars
        special_chars = ['!', '#', '%', '&', '/', '(', ')', '{', '}', '[', ']', '$', '£', '@']

        def bokstav():
            '''
            Chooses random letters, big or small
            bokstäver = letters in swedish
            '''
            bokstäver = ''.join(secrets.choice(string.ascii_letters))
            password.append(bokstäver)
        def nummer():
            '''
            Chooses random numbers
            flera_nummer = multiple numbers in swedish
            '''
            flera_nummer = ''.join(secrets.choice(numbers))
            password.append(flera_nummer)
        def special():
            '''
            Chooses random special chars
            special_tecken = special chars in swedish
            '''
            special_tecken = ''.join(secrets.choice(special_chars))
            password.append(special_tecken)

        for _ in range(length):
            specials_numbers_letters_int = [1,2,3]
            specials_numbers_letters_var = secrets.choice(specials_numbers_letters_int)
            if specials_numbers_letters_var == 1:
                bokstav()
            elif specials_numbers_letters_var == 2:
                nummer()
            elif specials_numbers_letters_var == 3:
                special()

        password = sklearn.utils.shuffle(password)
        password = ''.join(password)
        return password


    def passgen_advanced():
        '''
        This is the Advanced generation function.

        During the passwords creation all it's,
        letters, number and special chars are stored in a list named "password"

        The function get the user choosen amount of uppercase letters from the input with the key.
        "-IN1-" and stores it in the "stora_bokstäver"- variable.

        The function get the user choosen amount of lowercase letters from the input with the key,
        "-IN2-" and stores it in the "små_bokstäver"- variable.

        The function get the user choosen amount of numbers from the input with the key,
        "-IN3-" and stores it in the "siffror"- variable.

        The function get the user choosen amount of special chars from the input with the key,
        "-IN4-" and stores it in the "tecken"- variable.

        The available numbers and special chars are specified in the,
        "numbers" and "special_chars" respectively

        Using the value of each of these variables the function has a for loop for each variable,
        where it is run as per the users choice.

        The "stora_bokstäver" for loop adds the uppercase letter(s)

        The "små_bokstäver" for loop adds the lowercase letter(s)

        The "nummer" for loop adds the number(s)

        The "tecken" for loop adds the special char(s)

        After the for loops has completed all of their runs,
        the function shuffles the password list,
        using the sklearn.utils librarys .shuffle function.
        The function then removes all ' and , in the list, which leave it with a single value,
        Which is the full and completed pasword

        It then returns the password as the functions value
        '''
        password = []
        #stora_bokstäver = capital letters in swedish
        stora_bokstäver = int(values['-IN1-'])
        #små_bokstäver = lowercase letters in swedish
        små_bokstäver = int(values['-IN2-'])
        #siffror = numbers in swedish
        siffror = int(values['-IN3-'])
        #tecken = chars in swedish
        tecken = int(values['-IN4-'])
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        special_chars = ['!', '#', '%', '&', '/', '(', ')', '{', '}', '[', ']', '$', '£', '@']

        for _ in range(stora_bokstäver):
            temp_var = ''.join(secrets.choice(string.ascii_uppercase))
            password.append(temp_var)

        for _ in range(små_bokstäver):
            temp_var = ''.join(secrets.choice(string.ascii_lowercase))
            password.append(temp_var)

        for _ in range(siffror):
            temp_var = ''.join(secrets.choice(numbers))
            password.append(temp_var)

        for _ in range(tecken):
            temp_var = ''.join(secrets.choice(special_chars))
            password.append(temp_var)

        password = sklearn.utils.shuffle(password)
        password = ''.join(password)
        return password

    #No idead how this works, but it is necesary for multi-window purposes
    window1, window2, window3 = make_win_1(), None, None

    #This is the event loop
    while True:
        window, event, values = sg.read_all_windows()

        #Checks if certain events has occured
        if event == sg.WIN_CLOSED or event == 'Go Back':
            window.close()
            #Also necesary for multi-window purposes
            if window == window3:
                window3 = None
            elif window == window2:
                window2 = None
            elif window == window1:
                break

        #Checks if certain events has occured
        elif event == 'Simple Generation':
            window2 = make_win_2()

        elif event == 'Advanced Generation':
            window3 = make_win_3()

        elif event == 'enter_simple':
            if str(values['-IN-']).isdigit():
                window['-OUT-'].update(passgen_simple())
                window['-IN-'].update('')
            else:
                window['-IN-'].update('')
                sg.popup('You can only enter numbers')

        elif event == 'enter_advanced':
            if str(values['-IN1-']).isdigit() and str(values['-IN2-']).isdigit() and str(values['-IN3-']).isdigit():
                passgen_advanced()
                #These clears all the input fields
                window['-OUT-'].update(passgen_advanced())
                window['-IN1-'].update('')
                window['-IN2-'].update('')
                window['-IN3-'].update('')
                window['-IN4-'].update('')
            else:
                #These clears all the input fields
                window['-IN1-'].update('')
                window['-IN2-'].update('')
                window['-IN3-'].update('')
                window['-IN4-'].update('')
                #This popup is shown if the inputfields does not cintain numbers
                sg.popup('You can only enter numbers')
    #Terminates the window
    window.close()
