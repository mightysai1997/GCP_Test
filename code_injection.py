import os

def list_directory(directory):
    # Unsafely concatenate user input into a system command
    command = f"ls {directory}"
    os.system(command)

directory = input("Enter directory to list: ")
list_directory(directory)
