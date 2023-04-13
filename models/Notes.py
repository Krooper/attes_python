class Notes:
    notes_dict = {}
    notes = []

    def __init__(self):
        self.notes_dict = {}
        self.notes = []

    def __str__(self):
        out_str = ''
        for note_id, note in self.notes_dict.items():
            out_str += f"Note {note_id}:\n"
            for key, value in note.items():
                out_str += f"{key}: {value}\n"
            out_str += "\n"
        return out_str
