from datetime import datetime
counter = 0


class Note:
    id = int
    date_created = None
    date_edited = None
    caption = str
    text = str

    def __init__(self):
        global counter
        self.id = counter
        counter += 1

        self.date_created = datetime.now()
        self.date_edited = datetime.now()

        print("Input a Caption:")
        self.caption = input()

        print("Input Notes text:")
        self.text = input()


