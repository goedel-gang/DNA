import sys

#minimum distance as a command line argument
diff = int(sys.argv[1])

#it keeps track of comparisons made in the crucial bits of code (not in rep_close, as that counts as extra)
comparisons = 0

#a function to return a nice way to represent the crossover between strings
def rep_close(a, b):
	out = ''
	for i, j in zip(a, b):
		if i == j:
			out += i

		else:
			out += '.'

	return out

#function to determine if two strings are of a certain distance from each other
def is_close(a, b, max_diff):
	global comparisons

	diff_count = 0

	for i, j in zip(a, b):
		comparisons += 1

		if i != j:
			diff_count += 1

	return diff_count <= max_diff

pool = []

#works through each line in stdin, comparing it to all previous lines
for j in sys.stdin:
	i = j.strip()

	for k in pool:
		if is_close(i, k, diff):
			print i, k, '({0})'.format(rep_close(i, k))

	pool.append(i)

print comparisons
