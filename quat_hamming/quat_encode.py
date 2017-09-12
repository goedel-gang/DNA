import sys

#python ../brute/recursive_all.py 4 3 | python quat_encode.py |  python quat_error.py | python quat_decode.py | python validate_quat.py

#is a power of 2
def is_power(n):
	return (n != 0) and not (n & (n - 1))

for quad_text in sys.stdin:
	quad_text = quad_text.strip()
	code = []

	it = iter(quad_text)

	try:
		#fill in the code to output, reserving space for a parity quad when needed
		while True:
			if is_power(len(code) + 1):
				code.append(-1)
			else:
				code.append(int(next(it)))

	except StopIteration:
		#if the last one was a parity quad, remove it, as it would have had no coverage
		if code[-1] == -1:
			del code[-1]

	#go through the parity quads
	for ind, i in enumerate(code):
		if i == -1:
			#tally up data quads covered
			tally = 0

			#go through quads ocurring after parity quad
			for jnd, j in enumerate(code[ind + 1:], ind + 1):

				#if quad is covered, increment tally
				if (ind + 1) & (jnd + 1):
					tally += j

			#set parity quad to tally modulo 4
			code[ind] = tally % 4

	print ''.join([str(i) for i in code])

