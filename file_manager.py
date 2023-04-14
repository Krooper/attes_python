import os

from views.Notes_view import Notes_view


def get_file():
    new_view = Notes_view()
    if not os.path.exists("notes.json"):
        print("The file does not exists!\nCreating empty file...")
        open("notes.json", "x")
        return "notes.json", new_view
    else:
        print("File exists! Reading...")
        try:
            new_view.file_read("notes.json")
        except ValueError:
            print("The file is empty!")
        return "notes.json", new_view
