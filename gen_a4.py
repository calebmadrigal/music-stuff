from pyknon.genmidi import Midi
from pyknon.music import NoteSeq, Note, Rest
 
C_major = NoteSeq("A")
 
midi = Midi(1, tempo=80)
midi.seq_notes(C_major)
midi.write("A4.mid")
 
