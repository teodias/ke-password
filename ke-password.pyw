#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
    TODO:
    add window.bind for ESCAPE to clear all input fields
    
"""

# modules
import PySimpleGUI as sg
import random
import re
import pathlib as pl
from pathlib import Path
import sys

APP_NAME = "Password Generator"
APP_THEME = 'Default1'

WORD_LIST_FILE = r'wordlist.txt'
PASSWORD_FILE = r'passwords.txt'

SG_TIMEOUT = 50   # timeout in millisecond

DATATYPE_INTEGER = r"[0-9]+"

PASSWORD_LENGTH_MIN = 12
PASSWORD_LENGTH_MAX = 25
PASSWORD_LENGTH = r"1[2-9]|2[0-5]"

PASSWORD_AMOUNT_MIN = 1
PASSWORD_AMOUNT_MAX = 100
PASSWORD_AMOUNT = r"[1-9]|[1-9][0-9]|100"

LOWERCASE_CHARS = [
    # removed some letters to avoid ambiguity with digits
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def generate_passwords(
        password_length,
        use_lowercase_char,
        number_of_passwords):

    def read_word_list():
        with open(WORD_LIST_FILE) as file:
            words = file.read().split("\n")

        # some trivia
        # print('Shortest word in word list has', len(min(words, key=len)), 'chars')
        # print('Longest word in word list has', len(max(words, key=len)), 'chars')
        words = sorted(words, key=len)
        return words

    # local veriables
    word_list = []
    password_list = []

    # read words from word list file
    word_list = read_word_list()

    # starting from 1
    generated_passwords = 1
    while True:
        password = ''
        password += random.choice(word_list)
        password += '-'
        password += str(random.randint(0, 9))
        password += str(random.randint(0, 9))
        if use_lowercase_char:
            password += random.choice(LOWERCASE_CHARS)
        password += '-'
        password += random.choice(word_list)
        if len(password) >= int(password_length):
            password_list.append(password)
            generated_passwords += 1
        if generated_passwords > int(number_of_passwords):
            break
    password_list = sorted(password_list, key=len)
    return password_list


def gui(theme):

    sg.theme(theme)
    menu_right_click = ['', ['Copy selected password']]

    settings_layout = [
        [
            sg.Text(f'Enter password length ({PASSWORD_LENGTH_MIN}-{PASSWORD_LENGTH_MAX})'),
            sg.Push(),
            sg.Input(key='-PASSWORD_LENGTH-', enable_events=True, size=(5, 1), focus=True)
        ],
        [
            sg.Text('Use lowercase char'),
            sg.Push(),
            sg.Checkbox('', key='-USE_LOWERCASE_CHARS-', size=(2, 1), default=False),
        ],
        [
            sg.Text(f'Amount of passwords to generate ({PASSWORD_AMOUNT_MIN}-{PASSWORD_AMOUNT_MAX})'),
            sg.Push(),
            sg.Input(key='-PASSWORD_AMOUNT-', enable_events=True, size=(5, 1)),
        ]
    ]

    layout = [
        [
            sg.Push(),
            sg.Frame('Settings', settings_layout, element_justification="center"),
            sg.Push()
        ],
        [
            sg.MLine(key='-PASSWORDS-', expand_x=True, expand_y=True,
                     disabled=True, rstrip=True,
                     right_click_menu=menu_right_click,
                     font=("Courier New", 12)    # use a monotype font: Courier New, Consolas
                     )
        ],
        [
            sg.Push(),
            sg.Button('Start', disabled=True, expand_x=True, bind_return_key=True),
            sg.Button('Clear', disabled=True, expand_x=True),
            sg.Button('Copy', disabled=True, expand_x=True),
            sg.Button('Save', disabled=True, expand_x=True),
            sg.Button('Exit', expand_x=True),
            sg.Push()
        ]
    ]

    window = sg.Window(
        APP_NAME,
        layout,
        size=(400, 600),
        grab_anywhere=True
    )

    while True:

        event, values = window.read(timeout_key="-TIMEOUT-", timeout=SG_TIMEOUT)
        print("\n", event, values)

        # app closed
        if event in (sg.WIN_CLOSED, None, 'Exit'):
            break

        # input validation: allow users only to enter data suiting to the DATATYPE_INTEGER regex pattern
        if event == '-PASSWORD_LENGTH-' and values['-PASSWORD_LENGTH-'] and not re.fullmatch(DATATYPE_INTEGER, values['-PASSWORD_LENGTH-']):
            window['-PASSWORD_LENGTH-'].update('')
        if event == '-PASSWORD_AMOUNT-' and values['-PASSWORD_AMOUNT-'] and not re.fullmatch(DATATYPE_INTEGER, values['-PASSWORD_AMOUNT-']):
            window['-PASSWORD_AMOUNT-'].update('')

        # if user has entered allowed settings, enable Start buttom
        if re.fullmatch(PASSWORD_LENGTH, values['-PASSWORD_LENGTH-']) and re.fullmatch(PASSWORD_AMOUNT, values['-PASSWORD_AMOUNT-']):
            window['Start'].update(disabled=False)

        # if user has entered unallowed settings, disnable Start buttom
        if not re.fullmatch(PASSWORD_LENGTH, values['-PASSWORD_LENGTH-']) or not re.fullmatch(PASSWORD_AMOUNT, values['-PASSWORD_AMOUNT-']):
            window['Start'].update(disabled=True)

        if values['-PASSWORDS-']:
            """ enable the buttons clear/copy/save only if output area has data"""
            window['Clear'].update(disabled=False)
            window['Copy'].update(disabled=False)
            window['Save'].update(disabled=False)

        if not values['-PASSWORDS-']:
            """disable the buttons clear/copy/save is there is no data in output area"""
            window['Clear'].update(disabled=True)
            window['Copy'].update(disabled=True)
            window['Save'].update(disabled=True)

        if event == 'Copy selected password':
            """ on right click upon a selection of passwords copy them to the clipboard """
            try:
                password = window['-PASSWORDS-'].Widget.selection_get()
            except sg.tk.TclError:
                password = None
            if password:
                sg.clipboard_set(password)
                sg.popup(f"The selected password(s)\n\n{password}\n\nhas been copied\nto the clipboard.\n")

        if event == 'Start':
            """ on click on start button, generate passwords and print them to the output area"""
            passwords = generate_passwords(
                values['-PASSWORD_LENGTH-'],
                values['-USE_LOWERCASE_CHARS-'],
                values['-PASSWORD_AMOUNT-'])
            for password in passwords:
                window['-PASSWORDS-'].print(password)

        if event == 'Clear':
            """ clear the password list """
            window['-PASSWORDS-'].Update('')

        if event == 'Copy' and values['-PASSWORDS-']:
            sg.clipboard_set(values['-PASSWORDS-'])
            sg.popup(f"The listed password(s)\nhas been copied\nto the clipboard.\n")

        if event == 'Save':
            initial_folder = pl.Path.home().joinpath('Documents')
            selected_file_and_path = sg.popup_get_file(
                'Save Passwords',
                save_as=True,
                no_window=True,
                initial_folder=initial_folder,
                default_path=PASSWORD_FILE,
                file_types=(
                    ("Text Files", "*.txt"),
                    ("All Files", "*.*")
                )
            )
            if selected_file_and_path:
                file = pl.Path(selected_file_and_path)
                with open(file, mode='w') as writeable_file:
                    writeable_file.write(values['-PASSWORDS-'])

    window.close()


if __name__ == "__main__":
    script_file_path = Path(__file__).resolve().parent
    if not pl.Path(script_file_path).joinpath(WORD_LIST_FILE).exists():
        sg.Window('File not Found!',
                  [[sg.Text(f"No word list file '{WORD_LIST_FILE}' found!\n\nCannot continue without!")],
                   [sg.VPush()],
                   [sg.Push(), sg.Button("Cancel", size=10, bind_return_key=True)]],
                  size=(350, 170),
                  font="Any 16",
                  grab_anywhere=True,
                  modal=True,
                  keep_on_top=True
                  ).read(close=True)
        sys.exit(1)
    else:
        gui(APP_THEME)
