import random
import xml.etree.ElementTree as ET

from MIDIHelper import *
from midiutil.MidiFile import MIDIFile


#https://docs.google.com/spreadsheets/d/1ssmpa4BogK7YGO-Z6effPV2etxjEtAQWHVqYKhlRFmU/edit#gid=0

def ReturnIndianNoteCharacterFrom_Step_Alter_Octave(step, alter, octave):
    if step ==  'C' and alter == '-1' and octave == '3':
        return "..nn"
    elif step ==  'C' and alter == '0' and octave == '3':
            return "..N"
    elif step ==  'C' and alter == '1' and octave == '3':
            return ".S"
    elif step ==  'D' and alter == '-1' and octave == '3':
            return ".S"
    elif step ==  'D' and alter == '0' and octave == '3':
            return ".rr"
    elif step ==  'D' and alter == '1' and octave == '3':
            return ".R"
    elif step ==  'E' and alter == '-1' and octave == '3':
            return ".R"
    elif step ==  'E' and alter == '0' and octave == '3':
            return ".gg"
    elif step ==  'E' and alter == '1' and octave == '3':
            return ".G"
    elif step ==  'F' and alter == '-1' and octave == '3':
            return ".gg"
    elif step ==  'F' and alter == '0' and octave == '3':
            return ".G"
    elif step ==  'F' and alter == '1' and octave == '3':
            return ".M"
    elif step ==  'G' and alter == '-1' and octave == '3':
            return ".M"
    elif step ==  'G' and alter == '0' and octave == '3':
            return ".M'"
    elif step ==  'G' and alter == '1' and octave == '3':
            return ".P"
    elif step ==  'A' and alter == '-1' and octave == '3':
            return ".P"
    elif step ==  'A' and alter == '0' and octave == '3':
            return ".dd"
    elif step ==  'A' and alter == '1' and octave == '3':
            return ".D"
    elif step ==  'B' and alter == '-1' and octave == '3':
            return ".D"
    elif step ==  'B' and alter == '0' and octave == '3':
            return ".nn"
    elif step ==  'B' and alter == '1' and octave == '3':
            return ".N"
    elif step ==  'C' and alter == '-1' and octave == '4':
            return ".nn"
    elif step ==  'C' and alter == '0' and octave == '4':
            return ".N"
    elif step ==  'C' and alter == '1' and octave == '4':
            return "S"
    elif step ==  'D' and alter == '-1' and octave == '4':
            return "S"
    elif step ==  'D' and alter == '0' and octave == '4':
            return "rr"
    elif step ==  'D' and alter == '1' and octave == '4':
            return "R"
    elif step ==  'E' and alter == '-1' and octave == '4':
            return "R"
    elif step ==  'E' and alter == '0' and octave == '4':
            return "gg"
    elif step ==  'E' and alter == '1' and octave == '4':
            return "G"
    elif step ==  'F' and alter == '-1' and octave == '4':
            return "gg"
    elif step ==  'F' and alter == '0' and octave == '4':
            return "G"
    elif step ==  'F' and alter == '1' and octave == '4':
            return "M"
    elif step ==  'G' and alter == '-1' and octave == '4':
            return "M"
    elif step ==  'G' and alter == '0' and octave == '4':
            return "M'"
    elif step ==  'G' and alter == '1' and octave == '4':
            return "P"
    elif step ==  'A' and alter == '-1' and octave == '4':
            return "P"
    elif step ==  'A' and alter == '0' and octave == '4':
            return "dd"
    elif step ==  'A' and alter == '1' and octave == '4':
            return "D"
    elif step ==  'B' and alter == '-1' and octave == '4':
            return "D"
    elif step ==  'B' and alter == '0' and octave == '4':
            return "nn"
    elif step ==  'B' and alter == '1' and octave == '4':
            return "N"
    elif step ==  'C' and alter == '-1' and octave == '5':
            return "nn"
    elif step ==  'C' and alter == '0' and octave == '5':
            return "N"
    elif step ==  'C' and alter == '1' and octave == '5':
            return "S."
    elif step ==  'D' and alter == '-1' and octave == '5':
            return "S."
    elif step ==  'D' and alter == '0' and octave == '5':
            return "rr."
    elif step ==  'D' and alter == '1' and octave == '5':
            return "R."
    elif step ==  'E' and alter == '-1' and octave == '5':
            return "R."
    elif step ==  'E' and alter == '0' and octave == '5':
            return "gg."
    elif step ==  'E' and alter == '1' and octave == '5':
            return "G."
    elif step ==  'F' and alter == '-1' and octave == '5':
            return "gg."
    elif step ==  'F' and alter == '0' and octave == '5':
            return "G."
    elif step ==  'F' and alter == '1' and octave == '5':
            return "M."
    elif step ==  'G' and alter == '-1' and octave == '5':
            return "M."
    elif step ==  'G' and alter == '0' and octave == '5':
            return "M'."
    elif step ==  'G' and alter == '1' and octave == '5':
            return "P."
    elif step ==  'A' and alter == '-1' and octave == '5':
            return "P."
    elif step ==  'A' and alter == '0' and octave == '5':
            return "dd."
    elif step ==  'A' and alter == '1' and octave == '5':
            return "D."
    elif step ==  'B' and alter == '-1' and octave == '5':
            return "D."
    elif step ==  'B' and alter == '0' and octave == '5':
            return "nn."
    elif step ==  'B' and alter == '1' and octave == '5':
            return "N."
    elif step ==  'C' and alter == '-1' and octave == '6':
            return "nn."
    elif step ==  'C' and alter == '0' and octave == '6':
            return "N."
    elif step ==  'C' and alter == '1' and octave == '6':
            return "S.."

def ReturnWesternNoteCharacterFrom_Step_Alter_Octave(step, alter, octave):
    if step ==  'C' and alter == '-1' and octave == '3':
            return '.B'
    elif step ==  'C' and alter == '0' and octave == '3':
            return '.C'
    elif step ==  'C' and alter == '1' and octave == '3':
            return '.C#'
    elif step ==  'D' and alter == '-1' and octave == '3':
            return '.C#'
    elif step ==  'D' and alter == '0' and octave == '3':
            return '.D'
    elif step ==  'D' and alter == '1' and octave == '3':
            return '.D#'
    elif step ==  'E' and alter == '-1' and octave == '3':
            return '.D#'
    elif step ==  'E' and alter == '0' and octave == '3':
            return '.E'
    elif step ==  'E' and alter == '1' and octave == '3':
            return '.F'
    elif step ==  'F' and alter == '-1' and octave == '3':
            return '.E'
    elif step ==  'F' and alter == '0' and octave == '3':
            return '.F'
    elif step ==  'F' and alter == '1' and octave == '3':
            return '.F#'
    elif step ==  'G' and alter == '-1' and octave == '3':
            return '.F#'
    elif step ==  'G' and alter == '0' and octave == '3':
            return '.G'
    elif step ==  'G' and alter == '1' and octave == '3':
            return '.G#'
    elif step ==  'A' and alter == '-1' and octave == '3':
            return '.G#'
    elif step ==  'A' and alter == '0' and octave == '3':
            return 'A'
    elif step ==  'A' and alter == '1' and octave == '3':
            return 'A#'
    elif step ==  'B' and alter == '-1' and octave == '3':
            return 'A#'
    elif step ==  'B' and alter == '0' and octave == '3':
            return 'B'
    elif step ==  'B' and alter == '1' and octave == '3':
            return 'C'
    elif step ==  'C' and alter == '-1' and octave == '4':
            return 'B'
    elif step ==  'C' and alter == '0' and octave == '4':
            return 'C'
    elif step ==  'C' and alter == '1' and octave == '4':
            return 'C#'
    elif step ==  'D' and alter == '-1' and octave == '4':
            return 'C#'
    elif step ==  'D' and alter == '0' and octave == '4':
            return 'D'
    elif step ==  'D' and alter == '1' and octave == '4':
            return 'D#'
    elif step ==  'E' and alter == '-1' and octave == '4':
            return 'D#'
    elif step ==  'E' and alter == '0' and octave == '4':
            return 'E'
    elif step ==  'E' and alter == '1' and octave == '4':
            return 'F'
    elif step ==  'F' and alter == '-1' and octave == '4':
            return 'E'
    elif step ==  'F' and alter == '0' and octave == '4':
            return 'F'
    elif step ==  'F' and alter == '1' and octave == '4':
            return 'F#'
    elif step ==  'G' and alter == '-1' and octave == '4':
            return 'F#'
    elif step ==  'G' and alter == '0' and octave == '4':
            return 'G'
    elif step ==  'G' and alter == '1' and octave == '4':
            return 'G#'
    elif step ==  'A' and alter == '-1' and octave == '4':
            return 'G#'
    elif step ==  'A' and alter == '0' and octave == '4':
            return 'A.'
    elif step ==  'A' and alter == '1' and octave == '4':
            return 'A#.'
    elif step ==  'B' and alter == '-1' and octave == '4':
            return 'A#.'
    elif step ==  'B' and alter == '0' and octave == '4':
            return 'B.'
    elif step ==  'B' and alter == '1' and octave == '4':
            return 'C.'
    elif step ==  'C' and alter == '-1' and octave == '5':
            return 'B.'
    elif step ==  'C' and alter == '0' and octave == '5':
            return 'C.'
    elif step ==  'C' and alter == '1' and octave == '5':
            return 'C#.'
    elif step ==  'D' and alter == '-1' and octave == '5':
            return 'C#.'
    elif step ==  'D' and alter == '0' and octave == '5':
            return 'D.'
    elif step ==  'D' and alter == '1' and octave == '5':
            return 'D#.'
    elif step ==  'E' and alter == '-1' and octave == '5':
            return 'D#.'
    elif step ==  'E' and alter == '0' and octave == '5':
            return 'E.'
    elif step ==  'E' and alter == '1' and octave == '5':
            return 'F.'
    elif step ==  'F' and alter == '-1' and octave == '5':
            return 'E.'
    elif step ==  'F' and alter == '0' and octave == '5':
            return 'F.'
    elif step ==  'F' and alter == '1' and octave == '5':
            return 'F#.'
    elif step ==  'G' and alter == '-1' and octave == '5':
            return 'F#.'
    elif step ==  'G' and alter == '0' and octave == '5':
            return 'G.'
    elif step ==  'G' and alter == '1' and octave == '5':
            return 'G#.'
    elif step ==  'A' and alter == '-1' and octave == '5':
            return 'G#.'
    elif step ==  'A' and alter == '0' and octave == '5':
            return 'A.'
    elif step ==  'A' and alter == '1' and octave == '5':
            return 'A#.'
    elif step ==  'B' and alter == '-1' and octave == '5':
            return 'A#.'
    elif step ==  'B' and alter == '0' and octave == '5':
            return 'B.'
    elif step ==  'B' and alter == '1' and octave == '5':
            return 'C.'
    elif step ==  'C' and alter == '-1' and octave == '6':
            return 'A..'
    elif step ==  'C' and alter == '0' and octave == '6':
            return 'A#..'
    elif step ==  'C' and alter == '1' and octave == '6':
            return 'A#..'

def findLyricsElementForTheCurrentNote(node, indent):
    step = ""
    alter = "0"
    octave = ""
    try:
        step = node.find('.//pitch//step').text
    except:
        step = '0'
    
    try:
        alter = node.find('.//pitch//alter').text
    except:
        alter = '0'
    
    try:
        octave = node.find('.//pitch//octave').text
    except:
        octave = '0'
    print(indent + step + alter + octave)
    return ReturnWesternNoteCharacterFrom_Step_Alter_Octave(step,alter,octave)


def print_all_nodes_from_root(node, indent=""):
    print(indent + node.tag)
    if node.tag ==  'note':
       noteFlag = findLyricsElementForTheCurrentNote(node,indent)
       
       try:
           # Create the new element
           lyric_element = ET.Element("lyric")
           lyric_element.set("number", "2")

           syllabic_element = ET.Element("syllabic")
           syllabic_element.text = "single"

           text_element = ET.Element("text")
           text_element.text = noteFlag

           lyric_element.append(syllabic_element)
           lyric_element.append(text_element)
           
           # Insert the new element after the target node
           node.append(lyric_element)
           print('Element has been inserted at - ' + node.tag)
       except:
           print('Error adding node')
       
    for child in node:
        print_all_nodes_from_root(child, indent + "  ")

def GetMeTheNotes(xml_file, xml_file_withNotes):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    print_all_nodes_from_root(root)
    # Save the modified XML to a file
    tree.write(xml_file_withNotes)
    

def GetDurationByType(Note_Duration):
    if Note_Duration == 'Whole':
        return 4
    elif Note_Duration == 'Half':
        return 2
    elif Note_Duration == 'Quarter':
        return 1

def getPitchFromNote(note):
    if note ==  '.S':
        return 49
    elif note ==  '.rr' or note ==  '.r':
        return 50
    elif note ==  '.R':
        return 51
    elif note ==  '.gg' or note ==  '.g':
        return 52
    if note ==  '.G':
        return 53
    elif note ==  '.M':
        return 54
    elif note ==  ".M'":
        return 55
    elif note ==  '.P':
        return 56
    elif note ==  '.dd' or note ==  '.d':
        return 57
    elif note ==  '.D':
        return 58
    elif note ==  '.nn' or note ==  '.n':
        return 59
    elif note ==  '.N':
        return 60
    elif note ==  'S':
        return 61
    elif note ==  'rr' or note ==  'r':
        return 62
    elif note ==  'R':
        return 63
    elif note ==  'gg' or note ==  'g':
        return 64
    elif note ==  'G':
        return 65
    elif note ==  'M':
        return 66
    elif note ==  "M'":
        return 67
    elif note ==  'P':
        return 68
    elif note ==  'dd' or note ==  'd':
        return 69
    elif note ==  'D':
        return 70
    elif note ==  'nn' or note ==  'n':
        return 71
    elif note ==  'N':
        return 72
    elif note ==  'S.':
        return 73
    elif note ==  'rr.' or note ==  'r.':
        return 74
    elif note ==  'R.':
        return 75
    elif note ==  'gg.' or note ==  'g.':
        return 76
    elif note ==  'G.':
        return 77
    elif note ==  'M.':
        return 78
    elif note ==  "M'.":
        return 79
    elif note ==  'P.':
        return 80
    elif note ==  'dd.' or note ==  'd.':
        return 81
    elif note ==  'D.':
        return 82
    elif note ==  'nn.' or note ==  'n.':
        return 83
    elif note ==  'N.':
        return 84
    elif note ==  'S..':
        return 85
    elif note ==  '$':
        return 0
    elif note ==  '#':
        return -1
    elif note ==  '-':
        return 0
    elif note ==  'Dha':
        return 60
    elif note ==  'Dhin' or note ==  'Dhi':
        return 61
    elif note ==  'Ge':
        return 62
    elif note ==  'Ka' or note ==  'Ki' or note ==  'Ke':
        return 63
    elif note ==  'Kda':
        return 64
    elif note ==  'Na' or note ==  'Ta' or note ==  'TraKa':
        return 65
    elif note ==  'Re' or note ==  'Ra':
        return 66
    elif note ==  "Te":
        return 67
    elif note ==  'Ti' or note ==  'Tin' or note ==  'Tik':
        return 68
    else:
        print('Bad Note - ' , note)
        return 0

def getNoteFromPitch(pitch):
    if pitch == 49:
        return '.S'
    elif pitch == 50:
        return '.rr'
    elif pitch == 51:
        return '.R'
    elif pitch == 52:
        return '.gg'
    elif pitch == 53:
        return '.G'
    elif pitch == 54:
        return '.M'
    elif pitch == 55:
        return ".M'"
    elif pitch == 56:
        return '.P'
    elif pitch == 57:
        return '.dd'
    elif pitch == 58:
        return '.D'
    elif pitch == 59:
        return '.nn'
    elif pitch == 60:
        return '.N'
    elif pitch == 61:
        return 'S'
    elif pitch == 62:
        return 'rr'
    elif pitch == 63:
        return 'R'
    elif pitch == 64:
        return 'gg'
    elif pitch == 65:
        return 'G'
    elif pitch == 66:
        return 'M'
    elif pitch == 67:
        return "M'"
    elif pitch == 68:
        return 'P'
    elif pitch == 69:
        return 'dd'
    elif pitch == 70:
        return 'D'
    elif pitch == 71:
        return 'nn'
    elif pitch == 72:
        return 'N'
    elif pitch == 73:
        return 'S.'
    elif pitch == 74:
        return 'rr.'
    elif pitch == 75:
        return 'R.'
    elif pitch == 76:
        return 'gg.'
    elif pitch == 77:
        return 'G.'
    elif pitch == 78:
        return 'M.'
    elif pitch == 79:
        return "M'."
    elif pitch == 80:
        return 'P.'
    elif pitch == 81:
        return 'dd.'
    elif pitch == 82:
        return 'D.'
    elif pitch == 83:
        return 'nn.'
    elif pitch == 84:
        return 'N.'
    elif pitch == 85:
        return 'S..'

thaat_BILAWAL = [getPitchFromNote('S'), getPitchFromNote('R'),getPitchFromNote('G'),getPitchFromNote('M'),getPitchFromNote('P'),getPitchFromNote('D'),getPitchFromNote('N'),getPitchFromNote('S')]
thaat_KALYAN = [getPitchFromNote('S'), getPitchFromNote('R'),getPitchFromNote('G'),getPitchFromNote('M'''),getPitchFromNote('P'),getPitchFromNote('D'),getPitchFromNote('N'),getPitchFromNote('S')]
thaat_KHAMAJ = [getPitchFromNote('S'), getPitchFromNote('R'),getPitchFromNote('G'),getPitchFromNote('M'),getPitchFromNote('P'),getPitchFromNote('D'),getPitchFromNote('n'),getPitchFromNote('S')]
thaat_KAFI = [getPitchFromNote('S'), getPitchFromNote('R'),getPitchFromNote('g'),getPitchFromNote('M'),getPitchFromNote('P'),getPitchFromNote('D'),getPitchFromNote('n'),getPitchFromNote('S')]
thaat_BHAIRAV = [getPitchFromNote('S'), getPitchFromNote('r'),getPitchFromNote('G'),getPitchFromNote('M'),getPitchFromNote('P'),getPitchFromNote('d'),getPitchFromNote('N'),getPitchFromNote('S')]
thaat_MARWA = [getPitchFromNote('S'), getPitchFromNote('r'),getPitchFromNote('G'),getPitchFromNote('M'''),getPitchFromNote('P'),getPitchFromNote('D'),getPitchFromNote('N'),getPitchFromNote('S')]
thaat_ASAWARI = [getPitchFromNote('S'), getPitchFromNote('R'),getPitchFromNote('g'),getPitchFromNote('M'),getPitchFromNote('P'),getPitchFromNote('d'),getPitchFromNote('n'),getPitchFromNote('S')]
thaat_BHAIRAVI = [getPitchFromNote('S'), getPitchFromNote('r'),getPitchFromNote('g'),getPitchFromNote('M'),getPitchFromNote('P'),getPitchFromNote('d'),getPitchFromNote('n'),getPitchFromNote('S')]
thaat_POORVI = [getPitchFromNote('S'), getPitchFromNote('r'),getPitchFromNote('G'),getPitchFromNote('M'''),getPitchFromNote('P'),getPitchFromNote('d'),getPitchFromNote('N'),getPitchFromNote('S')]
thaat_TODI = [getPitchFromNote('S'), getPitchFromNote('r'),getPitchFromNote('g'),getPitchFromNote('M'''),getPitchFromNote('P'),getPitchFromNote('d'),getPitchFromNote('N'),getPitchFromNote('S')]



def isFirstNote(i):
    if i==1:
        #print('isFirstNote')
        return True

def is7thNote(i):
    if (i+1)%8 == 0 and i!=0:
        #print('7th Note')
        return True

def is8thNote(i):
    if (i%8) == 0 and i!=0:
        #print('8th Note')
        return True

def is15thNote(i):
    if (i+1)%16 == 0 and i!=0:
        #print('15th Note')
        return True

def isFirstPause(i):
    if (i+1)%8 == 0 and i!=0:
        print('isFirstPause')
        return True

def isSecondPause(i):
    if (i+1)%16 == 0:
        print('isMidPause')
        return True

def isLastPause(i,total_beats):
    if i == total_beats:
        print('isLastPause')
        return True


def get1stNotePitch():
    return getPitchFromNote('S')

def get7thNotePitch():
    return getPitchFromNote('.P')

def get15thNotePitch():
    return getPitchFromNote('P')

def get31stNotePitch():
    return getPitchFromNote('S.')






def getPitchFromNotePosition_test(i):
    if i==1:
        return getPitchFromNote('S')
    elif i==7:
        return getPitchFromNote('.P')
    elif i==15:
        return getPitchFromNote('P')
    elif i==23:
        return getPitchFromNote('S')
    elif i==31:
        return getPitchFromNote('S.')
    else:
        return random.choice(thaat_BILAWAL)

def getPitchFromNotePosition(i, thaat):
    j = i+1
    if i==1:
        return getPitchFromNote('S')
    elif j%32==0:
        return getPitchFromNote('S.')
    elif j%24==0:
        return getPitchFromNote('S')
    elif j%16==0:
        return getPitchFromNote('P')
    elif j%8==0:
        return getPitchFromNote('.P')
    else:
        return random.choice(thaat)

def GenerateRandomMidiByThaat(mf, track, channel, begintime, Note_Duration, tempo, filename, total_beats, thaat):
    time = begintime    # start at the beginning
    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, tempo)

    
    # add some notes
    channel = 0
    volume = 100
    duration= GetDurationByType(Note_Duration)
    doubleDuration = GetDurationByType(Note_Duration) * 2

    duration_total = 0
    
    i=1
    while i <= total_beats:
        pitch = getPitchFromNotePosition(i, thaat)
        
        duration = GetDurationByType(Note_Duration) # Other notes are 1 beat long
        if is7thNote(i):
            duration = doubleDuration    # 2 beats long on 7th Beat
    

        time = i-1
        print('i - ',i,' , pitch-',getNoteFromPitch(pitch), ', duration-',duration, ', time-',(time + 1), ', volume-',volume,'duration_total-',duration_total)
      

        if is8thNote(i):
            print('8th Note..Skipped..')
            test = 0
        else:    
            #mf.addNote(track, channel, pitch, time, duration, volume)
            mf.addNote(track, channel, pitch, duration_total, duration, volume)

        duration_total = duration_total + duration
        i = i + duration

    # write it to disk
    with open(filename, 'wb') as outf:
        mf.writeFile(outf)


    
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def createMIDIFromTempSRGMLyrics(TempoArray,SRGMArray,LyricsArray,enableBeatsFlag,out_midi_filename):
        # create your MIDI object
        mf = MIDIFile(1)     # only 1 track
        track = 0   # the only track
        program = 42 # A Cello
        begintime = 0
        tempo = 120
        channel1 = 0 #Main Channel e.g. Piano
        channel2 = 1 #Secondary Channel e.g. Beats
        channel3 = 2 #Secondary Channel e.g. Beats

        time = 0.0    # start at the beginning 0
        mf.addTrackName(track, time, "Main Track")
        mf.addTempo(track, time, tempo)
        volume = 100
        default_duration = 0.5
        i=0
        try:
            for char in SRGMArray:
                try:
                    if len(TempoArray) > 0:
                        duration = float(TempoArray[i])
                        if "-" in TempoArray[i]:
                            print('0.5 note found')
                    else:
                        duration = default_duration

                    if char == '#':
                        time = time + 1
                    elif char == '$':
                        time = time + (4-time%4) #Put a measure gap
                    else:                           
                        try:
                                pitch = getPitchFromNote(char)
                                LyricsChar = LyricsArray[i] if len(LyricsArray) > 0 else char
                                print( ') i - ',i,'Timeline - ',time, 'Duration - ', duration,' Note - ', char, ' (pitch - ' , pitch, ')',  ' - ', ' Lyrics - ' , LyricsChar)
                                
                                if char == '-':
                                    #This is for the REST
                                    mf.addNote(track, channel1, pitch, time, duration, 0)
                                else:
                                    mf.addNote(track, channel1, pitch, time, duration, volume)
                                
                                mf.addText(track,time,LyricsChar)
                                
                                
                                if enableBeatsFlag == True:
                                    if (time%16) == 0:
                                        mf = EnableTaal(mf,track,channel2,time,duration,volume)
                                        mf.addNote(track, channel2, getPitchFromNote('S'), time, duration, volume)
                                        mf.addNote(track, channel2, getPitchFromNote('G'), time, duration, volume)
                                        mf.addNote(track, channel2, getPitchFromNote('P'), time, duration, volume)
                                    if (time%4) == 0:
                                        mf = EnableTaal(mf,track,channel2,time,duration,volume)
                                        mf.addNote(track, channel2, getPitchFromNote('S'), time, duration, volume)
                                        

                                if SumNoteFlag(LyricsChar):
                                    mf.addNote(track, channel2, getPitchFromNote('S'), time, duration, volume)
                                    mf.addNote(track, channel2, getPitchFromNote('G'), time, duration, volume)
                                    mf.addNote(track, channel2, getPitchFromNote('P'), time, duration, volume)
                                if NinthNoteFlag(LyricsChar):
                                    mf.addNote(track, channel2, getPitchFromNote('S'), time, duration, volume)
                                #else:
                                #    mf.addNote(track, channel2, getPitchFromNote('S'), time, 1, volume)
                                #mf.addNote(track, channel3, getPitchFromNote('S'), time, duration, volume)
                                time = time + duration

                                i = i+1
                                if i == len(TempoArray):
                                    i = 0       
                        except:
                            duration = 1 #Set default duration to a quarter note
                except:
                    print('Error with - ', char)
        except:
                print('Error with for Loop')
                    
        # write it to disk
        with open(out_midi_filename, 'wb') as outf:
            mf.writeFile(outf)
            print(out_midi_filename)


def SumNoteFlag(LyricsChar):
    if '(1)' in LyricsChar:
        return True
    else:
        return False

def NinthNoteFlag(LyricsChar):
    if '(9)' in LyricsChar:
        return True
    else:
        return False
    
def EnableTaal(mf,track,channel2,time,duration,volume):
    print('track-', track, 'channel2-', channel2, 'time-' , time, 'duration-', 1, 'volume-', volume)
    
      
    return mf  
             
def GenerateMidiByNotesInput(out_midi_filename, input_Notes_Files,enableBeatsFlag, convertToAllThaats):
    #Read SRGM files
    lines = []
    SRGMArray = []
    TempoArray = []
    LyricsArray = []
    
    for SRGMFileName in input_Notes_Files:
        with open(SRGMFileName) as f:
            lines = lines + f.readlines()

    linecount = 1
    for line in lines:
        linecount = linecount + 1
        if len(line.replace('\t','')) > 0:
            Tempoline = replaceTempolineWithBlank(line)
            line = line.replace(Tempoline,'')
            line = line.replace('//Tempo','')
            Noteline = replaceNotelineWithBlank(line)
            line = line.replace(Noteline,'')  
            line = line.replace('//Notes//','')    
            try:
                if '//Lyrics' in line:
                    Lyricline = replaceLyriclineWithBlank(line)
                    line = line.replace(Lyricline,'')
                    line = line.replace('//Lyrics','')
                    LyricsArray = LyricsArray + line.replace('\n','').replace('\t',' ').rsplit()
                    continue

                if line.replace('\t','') != '\n' and line.replace('\t','')[0] != '/': #Ignore comments and new lines
                    if isfloat(line.replace('\n','').replace('\t',' ').rsplit()[0]): #If first character is a float number, then it's a tempo, or else it is a SRGM
                        TempoArray = TempoArray + line.replace('\n','').replace('\t',' ').rsplit()
                    else:
                        SRGMArray = SRGMArray + line.replace('\n','').replace('\t',' ').rsplit()
            except:
                print('Error parsing this line no - ' , linecount)
                print(line)
                return

    TempoArray_temp = TempoArray
    SRGMArray_temp = SRGMArray
    LyricsArray_temp = LyricsArray

    print('TempoArray - ',len(TempoArray) , ' - ', TempoArray)
    print('SRGMArray - ',len(SRGMArray)-SRGMArray.count('$'),' - ', SRGMArray)
    print('LyricsArray - ' , len(LyricsArray) , ' - ', LyricsArray)
    
    createMIDIFromTempSRGMLyrics(TempoArray,SRGMArray,LyricsArray,enableBeatsFlag,out_midi_filename)
    
    print('TempoArray - ',len(TempoArray))
    print('SRGMArray - ',len(SRGMArray)-SRGMArray.count('$'))
    print('LyricsArray - ' , len(LyricsArray))
    
    
    if convertToAllThaats == True:
        print('### Convert to BILAWAL')
        print('TempoArray - ',len(TempoArray) , ' - ', TempoArray)
        print('SRGMArray - ',len(SRGMArray) , ' - ', SRGMArray)
        print('LyricsArray - ' , len(LyricsArray) , ' - ', LyricsArray)
        createMIDIFromTempSRGMLyrics(TempoArray,SRGMArray,LyricsArray,enableBeatsFlag,out_midi_filename.replace('.mid','-01BILAWAL.mid'))
        TempoArray = TempoArray_temp
        SRGMArray = SRGMArray_temp
        LyricsArray = LyricsArray_temp
        
        
        print('### Convert to Kalyan - M'' Tivra')
        SRGMArray = list(map(lambda x: x.replace('M', 'M\''), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('M', 'M\''), LyricsArray))
        print('TempoArray - ',len(TempoArray) , ' - ', TempoArray)
        print('SRGMArray - ',len(SRGMArray) , ' - ', SRGMArray)
        print('LyricsArray - ' , len(LyricsArray) , ' - ', LyricsArray)
        createMIDIFromTempSRGMLyrics(TempoArray,SRGMArray,LyricsArray,enableBeatsFlag,out_midi_filename.replace('.mid','-02KALYAN.mid'))
        TempoArray = TempoArray_temp
        SRGMArray = SRGMArray_temp
        LyricsArray = LyricsArray_temp



        print('### Convert to Khamaj - n komal')
        SRGMArray = list(map(lambda x: x.replace('N', 'n'), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('N', 'n'), LyricsArray))
        print('TempoArray - ',len(TempoArray) , ' - ', TempoArray)
        print('SRGMArray - ',len(SRGMArray) , ' - ', SRGMArray)
        print('LyricsArray - ' , len(LyricsArray) , ' - ', LyricsArray)
        createMIDIFromTempSRGMLyrics(TempoArray,SRGMArray,LyricsArray,enableBeatsFlag, out_midi_filename.replace('.mid','-03KHAMAJ.mid'))
        TempoArray = TempoArray_temp
        SRGMArray = SRGMArray_temp
        LyricsArray = LyricsArray_temp
    
        print('### Convert to KAFI - g n Komal')
        SRGMArray = list(map(lambda x: x.replace('G', 'g'), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('G', 'g'), LyricsArray))
        
        SRGMArray = list(map(lambda x: x.replace('N', 'n'), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('N', 'n'), LyricsArray))
        print('TempoArray - ',len(TempoArray) , ' - ', TempoArray)
        print('SRGMArray - ',len(SRGMArray) , ' - ', SRGMArray)
        print('LyricsArray - ' , len(LyricsArray) , ' - ', LyricsArray)
        createMIDIFromTempSRGMLyrics(TempoArray,SRGMArray,LyricsArray,enableBeatsFlag, out_midi_filename.replace('.mid','-04KAFI.mid'))
        TempoArray = TempoArray_temp
        SRGMArray = SRGMArray_temp
        LyricsArray = LyricsArray_temp
    
        print('### Convert to BHAIRAV - r d Komal')
        SRGMArray = list(map(lambda x: x.replace('R', 'r'), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('R', 'r'), LyricsArray))
        
        SRGMArray = list(map(lambda x: x.replace('D', 'd'), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('D', 'd'), LyricsArray))
        print('TempoArray - ',len(TempoArray) , ' - ', TempoArray)
        print('SRGMArray - ',len(SRGMArray) , ' - ', SRGMArray)
        print('LyricsArray - ' , len(LyricsArray) , ' - ', LyricsArray)
        createMIDIFromTempSRGMLyrics(TempoArray,SRGMArray,LyricsArray,enableBeatsFlag, out_midi_filename.replace('.mid','-05BHAIRAV.mid'))
        TempoArray = TempoArray_temp
        SRGMArray = SRGMArray_temp
        LyricsArray = LyricsArray_temp
    
        print('### Convert to MARWA - M tivra r Komal')
        SRGMArray = list(map(lambda x: x.replace('M', 'M\''), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('M', 'M\''), LyricsArray))
        
        SRGMArray = list(map(lambda x: x.replace('R', 'r'), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('R', 'r'), LyricsArray))
        print('TempoArray - ',len(TempoArray) , ' - ', TempoArray)
        print('SRGMArray - ',len(SRGMArray) , ' - ', SRGMArray)
        print('LyricsArray - ' , len(LyricsArray) , ' - ', LyricsArray)
        createMIDIFromTempSRGMLyrics(TempoArray,SRGMArray,LyricsArray,enableBeatsFlag, out_midi_filename.replace('.mid','-06MARWA.mid'))
        TempoArray = TempoArray_temp
        SRGMArray = SRGMArray_temp
        LyricsArray = LyricsArray_temp

        print('### Convert to ASAWARI - g d n Komal')
        SRGMArray = list(map(lambda x: x.replace('G', 'g'), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('G', 'g'), LyricsArray))
        
        SRGMArray = list(map(lambda x: x.replace('D', 'd'), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('D', 'd'), LyricsArray))

        SRGMArray = list(map(lambda x: x.replace('N', 'n'), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('N', 'n'), LyricsArray))

        print('TempoArray - ',len(TempoArray) , ' - ', TempoArray)
        print('SRGMArray - ',len(SRGMArray) , ' - ', SRGMArray)
        print('LyricsArray - ' , len(LyricsArray) , ' - ', LyricsArray)
        createMIDIFromTempSRGMLyrics(TempoArray,SRGMArray,LyricsArray,enableBeatsFlag, out_midi_filename.replace('.mid','-07ASAWARI.mid'))
        TempoArray = TempoArray_temp
        SRGMArray = SRGMArray_temp
        LyricsArray = LyricsArray_temp

        print('### Convert to BHAIRAVI - r g d n Komal')
        SRGMArray = list(map(lambda x: x.replace('R', 'r'), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('R', 'r'), LyricsArray))

        SRGMArray = list(map(lambda x: x.replace('G', 'g'), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('G', 'g'), LyricsArray))
        
        SRGMArray = list(map(lambda x: x.replace('D', 'd'), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('D', 'd'), LyricsArray))

        SRGMArray = list(map(lambda x: x.replace('N', 'n'), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('N', 'n'), LyricsArray))

        print('TempoArray - ',len(TempoArray) , ' - ', TempoArray)
        print('SRGMArray - ',len(SRGMArray) , ' - ', SRGMArray)
        print('LyricsArray - ' , len(LyricsArray) , ' - ', LyricsArray)
        createMIDIFromTempSRGMLyrics(TempoArray,SRGMArray,LyricsArray,enableBeatsFlag, out_midi_filename.replace('.mid','-08BHAIRAVI.mid'))
        TempoArray = TempoArray_temp
        SRGMArray = SRGMArray_temp
        LyricsArray = LyricsArray_temp

        print('### Convert to POORVI - r d Komal M Tivra')
        SRGMArray = list(map(lambda x: x.replace('R', 'r'), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('R', 'r'), LyricsArray))

        SRGMArray = list(map(lambda x: x.replace('D', 'd'), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('D', 'd'), LyricsArray))

        SRGMArray = list(map(lambda x: x.replace('M', 'M\''), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('M', 'M\''), LyricsArray))

        print('TempoArray - ',len(TempoArray) , ' - ', TempoArray)
        print('SRGMArray - ',len(SRGMArray) , ' - ', SRGMArray)
        print('LyricsArray - ' , len(LyricsArray) , ' - ', LyricsArray)
        createMIDIFromTempSRGMLyrics(TempoArray,SRGMArray,LyricsArray,enableBeatsFlag, out_midi_filename.replace('.mid','-09POORVI.mid'))
        TempoArray = TempoArray_temp
        SRGMArray = SRGMArray_temp
        LyricsArray = LyricsArray_temp

        print('### Convert to TODI - r g d Komal M Tivra')
        SRGMArray = list(map(lambda x: x.replace('R', 'r'), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('R', 'r'), LyricsArray))

        SRGMArray = list(map(lambda x: x.replace('G', 'g'), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('G', 'g'), LyricsArray))

        SRGMArray = list(map(lambda x: x.replace('D', 'd'), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('D', 'd'), LyricsArray))

        SRGMArray = list(map(lambda x: x.replace('M', 'M\''), SRGMArray))
        LyricsArray = list(map(lambda x: x.replace('M', 'M\''), LyricsArray))

        print('TempoArray - ',len(TempoArray) , ' - ', TempoArray)
        print('SRGMArray - ',len(SRGMArray) , ' - ', SRGMArray)
        print('LyricsArray - ' , len(LyricsArray) , ' - ', LyricsArray)
        createMIDIFromTempSRGMLyrics(TempoArray,SRGMArray,LyricsArray,enableBeatsFlag, out_midi_filename.replace('.mid','-10TODI.mid'))
        TempoArray = TempoArray_temp
        SRGMArray = SRGMArray_temp
        LyricsArray = LyricsArray_temp


def GetNumberOfNotesFromFile(SRGMFileName):
    with open(SRGMFileName) as f:
        lines = f.readlines()
    return len(''.join(lines).rsplit())

def replaceTempolineWithBlank(line):
    Tempoline = ''
    try:
        Tempoline = line[line.index('//Tempo'):line.rindex('//')+2]
    except:
        Tempoline = ''
    return Tempoline

def replaceNotelineWithBlank(line):
    Tempoline = ''
    try:
        Tempoline = line[line.index('//Note'):line.rindex('//')+2]
    except:
        Tempoline = ''
    return Tempoline

def replaceLyriclineWithBlank(line):
    Tempoline = ''
    try:
        Tempoline = line[line.index('//Lyric'):line.rindex('//')+2]
    except:
        Tempoline = ''
    return Tempoline

def TestMidiGeneration(out_midi_filename):
    # create your MIDI object
    mf = MIDIFile(1)     # only 1 track
    track = 0   # the only track
    program = 42 # A Cello
    begintime = 0
    tempo = 120
    channel = 0

    #self.pitch = pitch
     #   self.duration = duration
      #  self.volume = volume
       # self.channel = channel
        #self.annotation = annotation
    

    time = 0.0    # start at the beginning 0
    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, tempo)
    volume = 100
    pitch = getPitchFromNote('S')

    mf.addNote(track, channel, pitch, time, 4, volume, 'ABC')
    mf.addTrackName(track,0,"MyTrackName")
    mf.addText(track,0,'A')

    mf.addNote(0, 1, getPitchFromNote('R'), time, 4, volume, 'ABC')
    mf.addNote(0, 2, getPitchFromNote('G'), time, 4, volume, 'ABC')

    # write it to disk
    with open(out_midi_filename, 'wb') as outf:
        mf.writeFile(outf)


