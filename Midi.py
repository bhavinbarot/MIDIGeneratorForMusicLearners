from MIDIHelper import *
from midiutil.MidiFile import MIDIFile
import random

filename = '00MIDI/AllThaatScales.mid'


# create your MIDI object
mf = MIDIFile(1)     # only 1 track
track = 0   # the only track
program = 42 # A Cello
begintime = 0
tempo = 30
channel = 0

'''
This method Supports
1.  Free Form Text
2. Multiple Files
3. Copy from Excel
'''
SRGMFiles = ['00MIDI/SRGM.txt']
#Note_Duration:
#Whole
#Half
#Quarter

GenerateMidiByNotesInput(mf, track, channel, begintime, 'Quarter', tempo, filename, SRGMFiles)



'''
This method Supports melody Generation using N number of notes in a specific Thaat
'''
#thaat_BILAWAL
#thaat_KALYAN
#thaat_KHAMAJ
#thaat_KAFI
#thaat_BHAIRAV
#thaat_MARWA
#thaat_ASAWARI
#thaat_BHAIRAVI
#thaat_POORVI
#thaat_TODI
total_beats =  640 #Prefer multiple of 8
filename = '00MIDI/Ear Training - Asawari.mid'
#GenerateRandomMidiByThaat(mf, track, channel, begintime, 'Quarter', tempo, filename,total_beats, thaat_ASAWARI)






