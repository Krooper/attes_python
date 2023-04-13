import json

def int_check(note_id):
    try:
        int(note_id)
        return True
    except ValueError:
        return False


class Notes_control:

    @staticmethod
    def note_check(note, notes):
        if note in notes.notes_dict.keys():
            return True
        return False

    @staticmethod
    def add(note, notes):
        notes.notes.append(note)
        notes.notes_dict[note.id] = {}
        notes.notes_dict[note.id] = {
            "Date of creation": note.date_created,
            "Date of editing": note.date_edited,
            "Caption": note.caption,
            "Text": note.text
        }

    @staticmethod
    def delete(note_id, notes):
        try:
            del notes.notes_dict[note_id]
            for note in notes.notes:
                if note.id == note_id:
                    notes.notes.remove(note)
        except KeyError:
            print("No such note! Try again!")

    @staticmethod
    def edit(note_id, notes):
        try:
            del notes.notes_dict[note_id]
        except KeyError:
            print("No such note! Try again!")

        note_for_editing = None
        for note_i in range(len(notes.notes) - 1):
            if notes.notes[note_i].id == note_id:
                note_for_editing = notes.notes.pop(note_i)
        return note_for_editing

    @staticmethod
    def date_sort(notes):
        for i in range(len(notes.notes) - 1):
            for j in range(len(notes.notes) - 1 - i):
                if notes.notes[j].date_edited > notes.notes[j+1].date_edited:
                    notes.notes[j], notes.notes[j+1] = notes.notes[j+1], notes.notes[j]

        return notes

    @staticmethod
    def date_save(notes):
        notes.notes_dict.clear()
        for note in notes.notes:
            notes.notes_dict[note.id] = {}
            notes.notes_dict[note.id] = {
                "Date of creation": note.date_created,
                "Date of editing": note.date_edited,
                "Caption": note.caption,
                "Text": note.text
            }
        return notes

    @staticmethod
    def file_save(notes, file):
        save_dict = notes.copy()
        for field, note_info in save_dict.items():
            save_dict[field] = str(note_info)

        with open(file, "w", encoding="utf-8") as file:
            json.dump(save_dict, file)
