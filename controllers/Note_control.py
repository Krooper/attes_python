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


