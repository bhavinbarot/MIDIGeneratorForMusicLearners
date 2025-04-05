import argparse
from MIDIHelper import *
from midiutil.MidiFile import MIDIFile
import random

def main():
    parser = argparse.ArgumentParser(description='MIDI Generator For Music Learners')

    parser.add_argument(
        '--input',
        nargs='+',
        default=['Resources/FilesInput/input.txt'],
        help='List of input note text files (default: Resources/FilesInput/input.txt)'
    )
    parser.add_argument(
        '--output',
        default='Resources/FilesOutput/output.mid',
        help='Output MIDI filename (default: Resources/FilesOutput/output.mid)'
    )
    parser.add_argument(
        '--random',
        action='store_true',
        help='Generate a random melody instead of using a note file'
    )
    parser.add_argument(
        '--thaat',
        type=str,
        help='Thaat name for random melody (required if --random is set)'
    )
    parser.add_argument(
        '--beats',
        type=int,
        default=40,
        help='Number of beats for random melody generation (default: 40)'
    )
    parser.add_argument(
        '--tempo',
        type=int,
        default=120,
        help='Tempo in BPM (default: 120)'
    )

    args = parser.parse_args()

    if args.random:
        if not args.thaat:
            print("Error: --thaat must be specified when using --random")
            return

        thaat_map = {
            "BILAWAL": thaat_BILAWAL,
            "KALYAN": thaat_KALYAN,
            "KHAMAJ": thaat_KHAMAJ,
            "KAFI": thaat_KAFI,
            "BHAIRAV": thaat_BHAIRAV,
            "MARWA": thaat_MARWA,
            "ASAWARI": thaat_ASAWARI,
            "BHAIRAVI": thaat_BHAIRAVI,
            "POORVI": thaat_POORVI,
            "TODI": thaat_TODI
        }

        selected_thaat = thaat_map.get(args.thaat.upper())

        if not selected_thaat:
            print(f"Error: Invalid Thaat name '{args.thaat}'")
            return

        mf = MIDIFile(1)
        track = 0
        channel = 0
        begintime = 0

        GenerateRandomMidiByThaat(
            mf,
            track,
            channel,
            begintime,
            'Quarter',
            args.tempo,
            args.output,
            args.beats,
            selected_thaat
        )

    else:
        GenerateMidiByNotesInput(
            args.output,
            args.input,
            enableBeatsFlag=False,
            convertToAllThaats=False
        )

if __name__ == '__main__':
    main()
