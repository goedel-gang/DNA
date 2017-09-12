import sys

'''prints possible words to make given an alphabet or base number and a length: eg
$ python recursive_all.py 2 3
001
010
011
100
etc
$ python recursive_all.py ab 3
aab
aba
abb
baa
etc

used for generating every possible string to sieve, or to do an encoding on'''

#potential characters to use
chrs = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

#reads base from command line arguments
base = sys.argv[1]

#checks if base either is a number less than the size of chrs, otherwise use as an alphabet in itself
if base.isdigit():
	if int(base) < len(chrs):
		base = int(base)
		alpha = chrs[:base]

	else:
		alpha = base
		base = len(alpha)

else:
	alpha = base
	base = len(alpha)

#reads desired length of strings
length = int(sys.argv[2])

#recursively generate strings
def get_all(alph, length, word=''):
	#base case
	if len(word) == length:
		yield word

	else:
		#branch off with recursion
		for i in alph:
			#iterate through generator to flatten yields
			for j in get_all(alph, length, word + i):
				yield j

for i in get_all(alpha, length):
	print i
