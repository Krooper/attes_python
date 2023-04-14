import time

from controllers.Note_control import Note_control
from controllers.Notes_control import Notes_control, int_check
from date_input_manager import select_date_range
from models.Note import Note
from models.Notes import Notes


class Notes_view:
    notes = None

    def __init__(self):
        self.notes = Notes()

    def note_choose(self):
        print("Choose a Note from the list below\n")
        time.sleep(1)
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

    def note_input(self, file):
        note = Note()
        note_id = 0
        for note in self.notes.notes:
            note_id = note.id + 1
        note.set_id(note_id)
        note.set_caption()
        note.set_text()
        note.set_date_created()
        note.set_date_edited()

        Notes_control.add(note, self.notes)
        Notes_control.file_save(self.notes, file)

    def note_edit(self, file):
        note_id = self.note_choose()
        edit_note = Notes_control.edit(note_id, self.notes)
        edited_note = Note_control.edit(edit_note)
        Notes_control.add(edited_note, self.notes)
        Notes_control.file_save(self.notes, file)

    def note_delete(self, file):
        note_id = self.note_choose()
        Notes_control.delete(note_id, self.notes)
        Notes_control.file_save(self.notes, file)

    def note_sort(self, file):
        self.notes = Notes_control.date_sort(self.notes)
        self.notes = Notes_control.date_save(self.notes)
        Notes_control.file_save(self.notes, file)

    def file_save(self, file):
        Notes_control.file_save(self.notes, file)

    def file_read(self, file):
        Notes_control.file_read(self.notes, file)
        Notes_control.save_from_file(self.notes)

    def select_date_range(self):
        start_date, end_date = select_date_range()
        out_notes = Notes()
        for note in self.notes.notes:
            if start_date < note.date_created < end_date:
                Notes_control.add(note, out_notes)

        print(out_notes)

