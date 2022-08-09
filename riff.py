from note import *

valid_time_signatures = {1,2,4,8,16,32,64,128}
class Riff:
    notes = []
    def __init__(self, notes, *args):

        # Duration and note symbol -
        self.notes = notes

        def set_time_signature(*metre):
            time_signature = []
            if len(metre) % 2 != 0:
                raise ValueError(f"Odd time signature values {metre}.") # Only even metre acceptable
            if set(metre[1::2]).issubset(valid_time_signatures):
                for x in zip(metre[::2], metre[1::2]):
                        time_signature.append(x)
                return time_signature
            else:
                raise ValueError(f"Invalid time signature values {metre}.") # Wrong number in time signature

        self.timeSignature = set_time_signature(*args)

        # bar - places in bar when individual notes can start.
        # TODO need to create bar structure, dependent on time signature
        self.bar = None
        # TODO length to be calculated from total bar length
        self.length = None



