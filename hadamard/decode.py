import sys
from subprocess import Popen, PIPE

'''for every line in stdin, return the closest hadamard code. couldn't understand the bit on wikipedia about local decodability, so did it this way
https://en.wikipedia.org/wiki/Hadamard_code'''

#get codes
proc = Popen(['python', 'gen_hadamard.py', sys.argv[1]], stdout=PIPE)
codes = proc.communicate()[0].split()
proc.wait()

#find hamming distance between a and b
def hamming(a, b):
	return sum(ca != cb for ca, cb in zip(a, b))

#finds closest code for each line in stdin
for line in sys.stdin:
	best_code = ''
	best_dist = float('inf')

	for code in codes:
		if hamming(line.strip(), code) < best_dist:
			best_code = code
			best_dist = hamming(line.strip(), code)

	print best_code
