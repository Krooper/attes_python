import time

from controllers.Note_control import Note_control
from controllers.Notes_control import Notes_control, int_check
from models.Note import Note
from models.Notes import Notes


class Notes_view:
    notes = None

    def __init__(self):
        self.notes = Notes()

    def note_choose(self):
        print("Choose a Note from the list below\n")
        time.sleep(2)
        print(self.notes)
        note_id = input("Input a note id: ")

        check = False
        while not check:
            if not int_check(note_id):
                note_id = input("Input a number!\nInput a note id: ")
            else:
                note_id = int(note_id)
                if not Notes_control.note_check(note_id, self.notes):
                    note_id = input("No such note!\nInput a note id: ")
                else:
                    check = True

        return note_id

    def note_input(self):
        note = Note()
        Notes_control.add(note, self.notes)

    def note_edit(self):
        note_id = self.note_choose()
        edit_note = Notes_control.edit(note_id, self.notes)
        edited_note = Note_control.edit(edit_note)
        Notes_control.add(edited_note, self.notes)

    def note_delete(self):
        note_id = self.note_choose()
        Notes_control.delete(note_id, self.notes)





