import os


def get_file():
    if not os.path.exists("notes.json"):
        print("The file does not exists!\nCreating empty file...")
        open("notes.json", "x")
        return "notes.json"
    else:
        return "notes.json"


def create_file():
    file_name = "notes.json"
    if not os.path.exists(file_name):
        open(file_name, "x")
    else:
        print("The file exists!\nAre you sure you want to remove it? (input y or n)")
        action = input()
        if action == 'y' or action == "Y":
            os.remove(file_name)
            open(file_name, "x")
        elif action == 'n' or action == "N":
            print("Input a new name for a new file:")
            file_name = input()
            open(file_name, "x")
        else:
            print("No such command! Try again!")
            return create_file()
    file = file_name
    return file