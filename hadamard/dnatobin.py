import sys

'''translate DNA to binary'''

#dictionary containing the different conversions
translate = {'A': '00',
			 'C': '01',
			 'G': '10',
			 'T': '11'}

#goes through each line writing the equivalent binary
for line in sys.stdin:
	for i in line.strip():
		sys.stdout.write(translate[i])

	sys.stdout.write('\n')
