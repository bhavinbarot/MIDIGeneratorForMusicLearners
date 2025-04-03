from MIDIHelper import *
from midiutil.MidiFile import MIDIFile
import random

#out_midi_filename = '00MIDI/Alankaar-12-13.mid'
#TestMidiGeneration(out_midi_filename)


'''
This method Supports
1.  Free Form Text
2. Multiple Files
3. Copy from Excel
'''
input_Notes_Files = ['00MIDI/SRGM.txt']
out_midi_filename = '00MIDI/Kehrva.mid'

GenerateMidiByNotesInput(out_midi_filename, input_Notes_Files,enableBeatsFlag = False, convertToAllThaats = False)

#GetMeTheNotes('00MIDI/Untitled.xml', '00MIDI/Untitled_with_notes.xml')



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

#total_beats =  640 #Prefer multiple of 8
#out_midi_filename = '00MIDI/Kalyan - Shabada Madhur Bole.mid'
#GenerateRandomMidiByThaat(mf, track, channel, begintime, 'Quarter', tempo, out_midi_filename,total_beats, thaat_BILAWAL)






