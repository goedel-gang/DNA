import sys

'''converts ascii to binary. used in testing hamming encoder and decoder, for quickly legible strings such as abcdefg'''

for word in sys.stdin:
	for i in word.strip():

		#uses the format spec to convert to binary string of seven, padded with zeroes
		sys.stdout.write(format(ord(i), '07b'))

	sys.stdout.write('\n')
