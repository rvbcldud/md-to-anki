import mdtoanki
import sys

def main():
    print('running md-to-anki script')
    mdtoanki.export_deck(sys.argv[1], sys.argv[2])
