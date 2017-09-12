import sys

for line in sys.stdin:
	for i in line.strip():
		if i == '1':
			#sys.stdout.write('\x1b[0;33;44m \x1b[0m')
			sys.stdout.write('/')
		else:
			sys.stdout.write(' ')

	sys.stdout.write('\n')
