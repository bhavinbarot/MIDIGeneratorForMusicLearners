import random
from MIDIHelper import *
from midiutil.MidiFile import MIDIFile

def GetDurationByType(Note_Duration):
    if Note_Duration == 'Whole':
        return 4
    elif Note_Duration == 'Half':
        return 2
    elif Note_Duration == 'Quarter':
        return 1

def getPitchFromNote(note):
    if note ==  '.g':
        return 52
    if note ==  '.G':
        return 53
    elif note ==  '.M':
        return 54
    elif note ==  ".M'":
        return 55
    elif note ==  '.P':
        return 56
    elif note ==  '.d':
        return 57
    elif note ==  '.D':
        return 58
    elif note ==  '.n':
        return 59
    elif note ==  '.N':
        return 60
    elif note ==  'S':
        return 61
    elif note ==  'r':
        return 62
    elif note ==  'R':
        return 63
    elif note ==  'g':
        return 64
    elif note ==  'G':
        return 65
    elif note ==  'M':
        return 66
    elif note ==  "M'":
        return 67
    elif note ==  'P':
        return 68
    elif note ==  'd':
        return 69
    elif note ==  'D':
        return 70
    elif note ==  'n':
        return 71
    elif note ==  'N':
        return 72
    elif note ==  'S.':
        return 73
    elif note ==  'r.':
        return 74
    elif note ==  'R.':
        return 75
    elif note ==  'g.':
        return 76
    elif note ==  'G.':
        return 77
    elif note ==  'M.':
        return 78
    elif note ==  "M'.":
        return 79
    elif note ==  'P.':
        return 80
    elif note ==  'd.':
        return 81
    elif note ==  'D.':
        return 82
    elif note ==  'n.':
        return 83
    elif note ==  'N.':
        return 84
    elif note ==  'S..':
        return 85

def getNoteFromPitch(pitch):
    if pitch == 52:
        return '.g'
    elif pitch == 53:
        return '.G'
    elif pitch == 54:
        return '.M'
    elif pitch == 55:
        return ".M'"
    elif pitch == 56:
        return '.P'
    elif pitch == 57:
        return '.d'
    elif pitch == 58:
        return '.D'
    elif pitch == 59:
        return '.n'
    elif pitch == 60:
        return '.N'
    elif pitch == 61:
        return 'S'
    elif pitch == 62:
        return 'r'
    elif pitch == 63:
        return 'R'
    elif pitch == 64:
        return 'g'
    elif pitch == 65:
        return 'G'
    elif pitch == 66:
        return 'M'
    elif pitch == 67:
        return "M'"
    elif pitch == 68:
        return 'P'
    elif pitch == 69:
        return 'd'
    elif pitch == 70:
        return 'D'
    elif pitch == 71:
        return 'n'
    elif pitch == 72:
        return 'N'
    elif pitch == 73:
        return 'S.'
    elif pitch == 74:
        return 'r.'
    elif pitch == 75:
        return 'R.'
    elif pitch == 76:
        return 'g.'
    elif pitch == 77:
        return 'G.'
    elif pitch == 78:
        return 'M.'
    elif pitch == 79:
        return "M'."
    elif pitch == 80:
        return 'P.'
    elif pitch == 81:
        return 'd.'
    elif pitch == 82:
        return 'D.'
    elif pitch == 83:
        return 'n.'
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





def GenerateMidiByNotesInput(mf, track, channel, begintime,Note_Duration, tempo,filename, SRGMFiles):
    time = begintime    # start at the beginning
    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, tempo)
    
    volume = 100
    duration= GetDurationByType(Note_Duration)
    for SRGMFileName in SRGMFiles:
        with open(SRGMFileName) as f:
            lines = f.readlines()

        SRGM = ''.join(lines).rsplit()
        print(SRGM)
        
        i=1
        for char in SRGM:
            try:
                pitch = getPitchFromNote(char)
                mf.addNote(track, channel, pitch, time, duration, volume)
                print('success - ', time, ' for char ', char, ' pitch - ' , pitch)
            except:
                print('Error with - ', char)
            
            time = time + 1
        
    # write it to disk
    with open(filename, 'wb') as outf:
        mf.writeFile(outf)


def GetNumberOfNotesFromFile(SRGMFileName):
    with open(SRGMFileName) as f:
        lines = f.readlines()
    return len(''.join(lines).rsplit())