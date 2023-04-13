from time import sleep

from views.Notes_view import Notes_view
import os


def file_reader():
    if not os.path.exists("notes.json"):
        print("The file does not exists!\nCreating empty file...")
        open("notes.json", "x")
        return "notes.json"
    else:
        return "notes.json"


def file_creator():
    file_name = "notes.json"
    if not os.path.exists(f'{file_name}.json'):
        open(f"{file_name}.json", "x")
    else:
        print("The file exists!\nAre you sure you want to remove it? (input y or n)")
        action = input()
        if action == 'y' or action == "Y":
            os.remove(f"{file_name}.json")
            open(f"{file_name}.json", "x")
        elif action == 'n' or action == "N":
            print("Input a new name for a new file:")
            file_name = input()
            open(f"{file_name}.json", "x")
        else:
            print("No such command! Try again!")
            return file_creator()
    file = f"{file_name}.json"
    return file


def start():
    print("Choose an action:")
    print("1 - Create a new Notes list.")
    print("2 - Read Notes list from .json file.")
    print("0 - Exit.")
    inp_com = input()
    file = "notes.json"

    try:
        inp_com = int(inp_com)
        if inp_com == 1:
            file = file_creator()
        elif inp_com == 2:
            file = file_reader()
        elif inp_com == 0:
            quit()
        else:
            raise ValueError
    except ValueError:
        print('There is no such command! Try again!')
        return start()
    return file


def main():
    #file = start()



if __name__ == "__main__":
    main()


