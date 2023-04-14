import json
from datetime import datetime
from models.Note import Note


def int_check(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


class encode_date_time(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()


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
                if notes.notes[j].date_edited > notes.notes[j + 1].date_edited:
                    notes.notes[j], notes.notes[j + 1] = notes.notes[j + 1], notes.notes[j]

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
        save_dict = {}
        for note_id, note in notes.notes_dict.items():
            save_dict[note_id] = note
            for field, info in note.items():
                save_dict[note_id][field] = info

        with open(file, "w", encoding="utf-8") as file:
            file.write(json.dumps(save_dict, indent=4, cls=encode_date_time))

    @staticmethod
    def file_read(notes, file):
        with open(file) as file:
            notes_dict = json.load(file)

        for key in notes_dict.keys():
            notes.notes_dict[int(key)] = notes_dict[key]

    @staticmethod
    def save_from_file(notes):
        notes.notes = []
        for note_id, note in notes.notes_dict.items():
            new_note = Note()
            new_note.id = int(note_id)
            new_note.date_created = datetime.fromisoformat(note["Date of creation"])
            new_note.date_edited = datetime.fromisoformat(note["Date of editing"])
            new_note.caption = note["Caption"]
            new_note.text = note["Text"]
            notes.notes.append(new_note)
