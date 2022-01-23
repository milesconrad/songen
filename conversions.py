notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

# given a diatonic chord, finds what chords can be played after it
chord_list = { 
    1 : [*range(1, 8)],
    2 : [5, 7],
    3 : [2, 4, 6],
    4 : [2, 5, 7],
    5 : [1, 6, 7],
    6 : [2, 4],
    7 : [1, 5, 6]
}

# converts a spot on a scale to the number of semitones away it is from the root note
note_to_semitones = {
    1 : 0,
    2 : 2,
    3 : 4,
    4 : 5,
    5 : 7,
    6 : 9,
    7 : 11
}

# given a diatonic chord (in the major scale), finds the quality of the chord
chord_qualities = {
    1 : '',
    2 : 'm',
    3 : 'm',
    4 : '',
    5 : '',
    6 : 'm',
    7 : 'dim'
}

note_to_int = {}

for i in range(len(notes)):
    note_to_int[notes[i]] = (i + 9) % 12

# making dictionary keys for enharmonic notes
for i in range(len(notes)):
    if '#' in notes[i]:
        note_to_int[f'{notes[(i + 1) % 12]}b'] = note_to_int[notes[i]]