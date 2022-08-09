class Riff:
    def __init__(self, notes, rhythm, length=0, *args):
        self.length = length
        # Rhythm - places in bar when individual notes can start
        self.rhythm = rhythm
        # Duaaration and note symbol -
        self.notes = notes

        def set_time_signature(*metre):
            time_signature = []
            if len(metre) % 2 != 0:
                raise ValueError(f"Invalid time signature {metre}")
            # elif {metre[::2] not in {1, 2, 4, 8, 16, 32, 64}}:
            #     pass
            else:
                for x in zip(metre[::2], metre[1::2]):
                    time_signature.append(x)
                return time_signature

        self.timeSignature = set_time_signature(*args)



