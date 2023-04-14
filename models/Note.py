from datetime import datetime
counter = 0


class Note:
    id = int
    date_created = None
    date_edited = None
    caption = str
    text = str

    def set_caption(self):
        print("Input a Caption:")
        self.caption = input()

    def set_text(self):
        print("Input Notes text:")
        self.text = input()

    def set_id(self, note_id=counter):
        global counter
        self.id = note_id
        counter += 1

    def set_date_created(self):
        self.date_created = datetime.now()

    def set_date_edited(self):
        self.date_edited = datetime.now()

    def __init__(self):
        pass


