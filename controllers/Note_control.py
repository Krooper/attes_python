from datetime import datetime

from controllers.Notes_control import Notes_control


class Note_control:

    @staticmethod
    def edit(note):
        note.date_edited = datetime.now()

        print("Input a Caption:")
        note.caption = input()

        print("Input Notes text:")
        note.text = input()

        return note

    @staticmethod
    def date_sort(notes):
        # notes.notes_dict.clear()
        # notes.notes.sort()
        # for note in notes.notes:
        # Notes_control.add(note, notes)
