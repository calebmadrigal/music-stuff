import wave
import numpy
from itertools import cycle

starting_freq = 27.5 #A0
piano_freqs = []
current_note = starting_freq
interval_ratio = 2**(1./12)

for i in range(88):
	piano_freqs.append(current_note)
	current_note = current_note * interval_ratio

note_names_gen = cycle(['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'])
note_names = [note_names_gen.next() for i in range(88)]

wav_data = wave.open("A4.wav")
#wav_data = wave.open("MiddleC.wav")
framerate = wav_data.getframerate()
nframes = wav_data.getnframes()
sound_info = wav_data.readframes(nframes/10)
sound_info_array = numpy.fromstring(sound_info, "Int16")

w = [abs(x.real) for x in numpy.fft.fft(sound_info_array)]
max_index = numpy.argmax(numpy.abs(w)**2)

freqs = numpy.fft.fftfreq(len(w))
freq = freqs[max_index]
freq_in_hz = abs(freq*framerate * 4)

print "Frequency:", freq_in_hz

closest_note_match = numpy.argmin(map(lambda note: abs(freq_in_hz - note), piano_freqs))
print "The note is", note_names[closest_note_match]


