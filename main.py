from time import sleep

from views.Notes_view import Notes_view
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
            file = create_file()
        elif inp_com == 2:
            file = get_file()
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

    new_view = Notes_view()
    new_view.note_input("notes.json")
    new_view.note_input("notes.json")
    new_view.note_input("notes.json")

    new_view.note_edit("notes.json")

    new_view.note_sort("notes.json")

    new_view.note_edit("notes.json")

    print(new_view.notes)

    new_view.file_save("notes.json")



if __name__ == "__main__":
    main()


