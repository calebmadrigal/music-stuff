starting_freq = 27.5 #A0
freqs = []
current_note = starting_freq
interval_ratio = 2**(1./12)

for i in range(88):
	freqs.append(current_note)
	current_note = current_note * interval_ratio

print "Piano note frequencies:"
for i in range(88):
	print "Note", i+1, "=", freqs[i]

