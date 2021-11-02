# HashCalc version 0.2

#   importing main functionality
import PySimpleGUI as sg
import hashlib
import os.path


#   calculating MD5
def calculate_checksummd5(filename):
    with open(filename, 'rb') as file:
        return hashlib.md5(file.read()).hexdigest()
        
#   calculating SHA-1
def calculate_checksum1(filename):
    with open(filename, 'rb') as file:
        return hashlib.sha1(file.read()).hexdigest()

#   calculating SHA-256
def calculate_checksum256(filename):
    with open(filename, 'rb') as file:
        return hashlib.sha256(file.read()).hexdigest()


#   defining window colour
sg.theme('BrownBlue')
#   Content of the GUI
layout = [  [sg.Text('HashCalc')],
            [sg.Text('Enter full file-path'), sg.InputText()],
            [sg.Button('Calculate'), sg.Button('Close')] ]

#   Creating GUI Window
window = sg.Window('HashCalc v0.2', layout)

#   Loop to process events and get input value
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close': 
        #   if user closes window or clicks cancel
        break
#   Calculation
    if event == 'Calculate':
        
        #   splitting Filepath down to just the filename
        target = values[0]
        tcut = target.split("/", -1)[-1]
        print('\nCalculating hashsums for ', tcut)
        path = str(values[0])
        try:
            calculate_checksum1(path)
        #   error-handling if path to file incorrect or not found
        except (FileNotFoundError, SyntaxError, NameError):
            print('File not found! Please check the path!')
        #   printing output
        else:
            print('\nMD5 Checksum:')
            md5 = (calculate_checksummd5(path))
            print(md5)
            print('\nSHA-1 Checksum:')
            sha1 = (calculate_checksum1(path))
            print(sha1)
            print('\nSHA-256 Checksum:')
            sha256 = (calculate_checksum256(path))
            print(sha256)
window.close()
