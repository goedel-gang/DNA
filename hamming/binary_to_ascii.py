import sys

'''converts binary to ascii. used in testing hamming encoder and decoder, for quickly legible strings such as abcdefg'''

#generate the 'chunks' of an iterable
def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

for word in sys.stdin:
	#iterate over the chunks of the binary input

	for i in chunks(word.strip(), 7):
		#convert each chunk to an integer from base 2, and then output the corresponding ascii character
		sys.stdout.write(chr(int(i, 2)))

	sys.stdout.write('\n')
