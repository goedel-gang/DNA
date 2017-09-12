import sys

#find if a number is a power of 2
def is_power(n):
	return (n != 0) and not (n & (n - 1))

for quad_text in sys.stdin:

	quad_text = quad_text.strip()
	code = [int(i) for i in quad_text]

	bad_parity = []
	bad_tallies = []
	badnorm_tallies = []
	desired_tallies = []

	for ind, i in enumerate(code):
		#if it's a parity quad, check parity
		if is_power(ind + 1):

			tally = 0

			#iterate over quads ocurring after parity quad
			for jnd, j in enumerate(code[ind + 1:], ind + 1):

				#if index should be covered
				if (jnd + 1) & (ind + 1):
					tally += j

			if code[ind] != tally % 4:
				bad_parity.append(ind + 1)
				badnorm_tallies.append(tally)
				desired_tallies.append(code[ind])

	#if an error was detected...
	if len(bad_parity) > 0:
		code[sum(bad_parity) - 1] += desired_tallies[0] - badnorm_tallies[0]

		code[sum(bad_parity) - 1] %= 4

	#go backwards through the sequence, removing parity quads
	for ind in range(len(code))[::-1]:
		if is_power(ind + 1):
			del code[ind]

	print ''.join([str(i) for i in code])
