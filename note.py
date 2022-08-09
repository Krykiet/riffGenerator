validNotes = {"C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"}
validValues = {1, 2, 4, 8, 16, 32, 64, "2*", "4*", "8*", "16*", "32*", "64*"}

class Note:
    #TODO position system
    def __init__(self, value, position, name="r", octave=None):
        # name of the note, default is the rest
        self.name = name
        if name not in validNotes:
            raise ValueError(f"Notes name must be one of {validNotes}")
        # default octave as 2 or 3
        self.octave = octave
        # position in the bar
        self.position = position
        # TODO not so sure how to do this yet, probably tuple x with precision of (1/4^n) where n is len(x)
        if octave is None:
            if name in {"C", "C#", "D", "D#"}:
                self.octave = 3
            else:
                self.octave = 2
        # value = duration of the note, no default
        self.value = value
        if value not in validValues:
            raise ValueError(f"Invalid value for {name} note")


