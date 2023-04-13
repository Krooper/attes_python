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
        notes.notes_dict[note.id] = []
        notes.notes_dict[note.id].append({
            "Date of creation": note.date_created,
            "Date of editing": note.date_edited,
            "Caption": note.caption,
            "Text": note.text
        })

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
        for note_i in range(len(notes.notes)):
            if notes.notes[note_i].id == note_id:
                note_for_editing = notes.notes.pop(note_i)
        return note_for_editing
