from file_manager import create_file, get_file
from views.Notes_view import Notes_view


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
    # file = start()

    new_view = Notes_view()
    new_view.note_input("notes.json")
    new_view.note_input("notes.json")
    new_view.note_input("notes.json")

    new_view.note_edit("notes.json")

    new_view.note_sort("notes.json")

    new_view.file_read("notes.json")

    new_view.note_edit("notes.json")

    new_view.note_sort("notes.json")

    new_view.note_input("notes.json")

    new_view.note_edit("notes.json")

    new_view.note_sort("notes.json")


if __name__ == "__main__":
    main()
