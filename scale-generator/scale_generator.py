class Scale:

    sharp_notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    flat_notes = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

    sharp_major = ['C', 'G', 'D', 'A', 'E', 'B', 'F#']
    sharp_minor = ['a', 'e', 'b', 'f#', 'c#', 'g#', 'd#']
    # flat_major = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb']
    # flat_minor = ['d', 'g', 'c', 'f', 'bb', 'eb']

    def __init__(self, tonic):

        # Use sharps or flats based on the tonic (starting note).
        if tonic in self.sharp_major or tonic in self.sharp_minor:
            self.notes = self.sharp_notes
        else:
            self.notes = self.flat_notes

        # Convert the note to capital; don't modify sharp (#) or flat(b).
        if len(tonic) == 2:
            self.tonic = tonic[0].upper() + tonic[1]
        else:
            self.tonic = tonic.upper()


    def chromatic(self):
        # Return all the notes from the tonic note.
        i = self.notes.index(self.tonic)
        return self.notes[i:] + self.notes[:i]


    def interval(self, intervals):
        
        self.chord = [self.tonic]

        i = self.notes.index(self.tonic)
        for x in intervals[0 : len(intervals) - 1]:
            if x == 'M':
                i = (i + 2) % 12
            elif x == 'm':
                i = (i + 1) % 12
            elif x == 'A':
                i = (i + 3) % 12
                
            self.chord.append(self.notes[i])

        return self.chord


    def __str__(self):
        return self.tonic


