import sys

'''Hamming encoder. A single error can later be corrected. Encoding works by adding a parity bit at each position which is apower of 2, which then covers each data bit which also contains that position's 1 bit (if parity_ind & data_ind). Then the error must be at the position obtained by adding the indexes of the erroneous parity bits.''' 

#is a power of 2
def is_power(n):
	return (n != 0) and not (n & (n - 1))

for bin_text in sys.stdin:
	bin_text = bin_text.strip()
	code = []

	it = iter(bin_text)

	#fill in the code, reserving space for parity bits at each index which is a power of 2
	try:
		while True:
			if is_power(len(code) + 1):
				code.append(-1)
			else:
				code.append(int(next(it)))

	except StopIteration:
		#if the last item was a parity bit, remove it, as it would have no useful coverage.
		if code[-1] == -1:
			del code[-1]

	#go through the parity bits, filling in the parity
	for ind, i in enumerate(code):
		if i == -1:
			#tally corresponding bits

			tally = 0

			#go through bits ocurring after the parity bit
			for jnd, j in enumerate(code[ind + 1:], ind + 1):
				#if the bit is covered, increment the tally
				if (ind + 1) & (jnd + 1):
					tally += j

			#set the parity bit
			code[ind] = tally & 1

	print ''.join([str(i) for i in code])

