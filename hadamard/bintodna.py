import sys

'''translate binary to DNA'''

#a dictionary containing the different conversions
translate = {('0', '0'): 'A',
			 ('0', '1'): 'C',
			 ('1', '0'): 'G',
			 ('1', '1'): 'T'}

#goes through each pair of binary digits in each line, and translates them
for line in sys.stdin:
	for i in zip(line.strip()[::2], line.strip()[1::2]):
		sys.stdout.write(translate[i])

	sys.stdout.write('\n')
