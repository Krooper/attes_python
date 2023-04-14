from file_manager import get_file


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
            file, new_view = get_file()
        elif inp_com == 2:
            file, new_view = get_file()
        elif inp_com == 0:
            new_view = None
            quit()
        else:
            raise ValueError
    except ValueError:
        print('There is no such command! Try again!')
        return start()
    return file, new_view


def main_menu(file, new_view):
    while True:

        print('-' * 75)
        print('Main menu')
        print('-' * 75)
        inp_com = input(f'Choose an action:\n"1" - Print notes\n'
                        f'"2" - Add note\n"3" - Edit note\n'
                        f'"4" - Delete note\n"5" - Choose notes by date\n'
                        f'"0" - Exit\n')
        print('-' * 75)
        try:
            inp_com = int(inp_com)
            if inp_com == 1:
                print(new_view.notes)
            elif inp_com == 2:
                new_view.note_input(file)
            elif inp_com == 3:
                new_view.note_edit(file)
            elif inp_com == 4:
                new_view.note_delete(file)
            elif inp_com == 5:
                new_view.select_date_range()
            elif inp_com == 0:
                quit()
            else:
                raise ValueError
        except ValueError:
            print('No such command! Try again!')
            return main_menu()


def main():
    file, new_view = start()
    main_menu(file, new_view)


if __name__ == "__main__":
    main()
