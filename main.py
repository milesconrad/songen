from random import randint, choice
from time import sleep
from pysinewave import SineWave
from threading import Thread
from pychord import Chord
import conversions

# generates chord progression using chords I-VII
def generate_progression():
    counter = 0
    progression = [randint(1, 7)]
    # while the chord progression is unresolved, and there is more than 1 chord in the progression
    while 1 not in conversions.chord_list[progression[-1]] or counter == 0:
        progression.append(choice(conversions.chord_list[progression[-1]]))
        counter += 1
    # if the last chord isn't a I chord, then the progression will be unresolved
    if progression[-1] != 1:
        progression.append(1)
    
    return progression

# takes relative chord progression 
def transpose_progression(progression: list, key: str):
    transposed_progression = []
    root = conversions.notes.index(key)
    for chord in progression:
        note = conversions.notes[(root + conversions.note_to_semitones[chord]) % 12]
        transposed_progression.append(note + conversions.chord_qualities[chord])

    return transposed_progression

# takes in a list of notes, grabs the first and last notes in the list (pysinewave is overwhelmed by more
# than 2 notes at a time), and plays sine tones of those notes
def play_progression(progression: list):
    for chord in progression:
        chord = Chord(chord)
        components = chord.components()
        components = [components[0], components[-1]]
        for note in components:
            Thread(target = play_note, args = (note,)).start()
        sleep(1.25)

def play_note(note: str):
    note_player = SineWave(pitch = conversions.note_to_int[note])
    note_player.play()
    sleep(1)
    note_player.stop()

def main():
    relative_progression = generate_progression()
    key = ''
    print('What key do you want the chord progression to be in?')
    while key not in conversions.notes:
        key = input('Enter the key as a letter such as A, A#, C, D, G# etc. ').upper()
    final_progression = transpose_progression(relative_progression, key)

    print()
    output = 'Your chord progression is: '
    for chord in final_progression:
        output += f'{str(chord)} '
    print(f'{output}\n')

    choice = ''
    while 'y' not in choice and 'n' not in choice:
        choice = input('Would you like to hear your chord progression? If yes, turn your volume\ndown a bit before proceeding (y or n) ').lower()
    
    if 'y' in choice:        
        play_progression(final_progression)

if __name__ == '__main__':
    main()