from datetime import datetime


class Note_control:

    @staticmethod
    def edit(note):
        note.date_edited = datetime.now()

        print("Input a Caption:")
        note.caption = input()

        print("Input Notes text:")
        note.text = input()

        return note
