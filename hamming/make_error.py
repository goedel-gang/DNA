import sys, random

'''causes an error in binary at a random index, for testing the hamming encoder and decoder'''

for word in sys.stdin:
	word = word.strip()

	#generate a random index
	ind = random.randint(0, len(word) - 1)

	print '{}{}{}'.format(word[:ind],
						  1 - int(word[ind]), #flip the bit
						  word[ind+1:])
