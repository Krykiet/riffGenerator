validNotes = {"C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"}

class Note:

    def __init__(self, value, name="r", octave=None):
        # name of the note, default is the rest
        self.name = name
        # default octave as 2 or 3
        self.octave = octave
        if octave is None:
            if name in {"C", "C#", "D", "D#"}:
                self.octave = 3
            else:
                self.octave = 2
        # value = duration of the note, no default
        self.value = value
        if name not in validNotes:
            raise ValueError(f"Notes name must be one of {validNotes}")

