"""
Ask user for their username
"""

def main():

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
                 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username = input("Enter username: ")
    if username in usernames:
        print("Welcome back")
    else:
        print("Invalid username")



