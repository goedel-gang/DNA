import sys, random

'''introduces a specified number of errors randomly into binary'''

for line in sys.stdin:
	#uses a set comprehension to generate indices of bits to flip
	error_indices = {random.randint(0, len(line) - 2) for _ in xrange(int(sys.argv[1]))}

	for ind, i in enumerate(line):
		if ind in error_indices:
			sys.stdout.write(str(1 - int(i)))

		else:
			sys.stdout.write(i)
