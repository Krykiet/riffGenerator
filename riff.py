class Riff:
    def __init__(self, notes, rhythm, length=0):
        self.length = length
        # Rhythm - places in bar when individual notes can start
        self.rhythm = rhythm
        # Duration of each note
        self.notes = notes
