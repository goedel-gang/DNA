import sys

'''Hamming decoder. It can correct a single error, and then prints the data bits. Encoding works by adding a parity bit at each position which is apower of 2, which then covers each data bit which also contains that position's 1 bit (if parity_ind & data_ind). Then the error must be at the position obtained by adding the indexes of the erroneous parity bits.''' 

#is a power of 2
def is_power(n):
	return (n != 0) and not (n & (n - 1))

for bin_text in sys.stdin:

	bin_text = bin_text.strip()
	code = [int(i) for i in bin_text]

	bad_parity = []

	#go over parity bits, checking if they correspond
	for ind, i in enumerate(code):
		if is_power(ind + 1):

			#tally up parity
			tally = 0

			#go through bits after the parity bit
			for jnd, j in enumerate(code[ind + 1], ind + 1):
				#if the bit is covered, increment the tally
				if (jnd + 1) & (ind + 1):
					tally += j

			#if it doesn't correspond, flag up that bit's index
			if code[ind] != tally & 1:
				bad_parity.append(ind + 1)

	#if errors were detected
	if len(bad_parity) > 0:

		#correct the erroneous bit
		code[sum(bad_parity) - 1] = 1 - code[sum(bad_parity) - 1]

	#go backwards through the code, removing parity bits
	for ind in range(len(code))[::-1]:
		if is_power(ind + 1):
			del code[ind]

	print ''.join([str(i) for i in code])
