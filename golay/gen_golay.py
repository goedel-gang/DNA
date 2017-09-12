import sys

gen_mat = file(sys.argv[1], 'r')

for ind, line in enumerate(gen_mat):
	sys.stdout.write('0' * ind)
	sys.stdout.write('1')
	sys.stdout.write('0' * (11 - ind))
	sys.stdout.write(line)
