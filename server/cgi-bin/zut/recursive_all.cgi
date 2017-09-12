#!/usr/bin/python

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

import cgi
import cgitb
cgitb.enable()

input_data=cgi.FieldStorage()

print 'AKLSDJHFALSKDJFH'

#potential characters to use
chrs = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

#reads base from command line arguments
base = 4

alpha = '0123'

#reads desired length of strings
length = int(input_data['len'].value)

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

print '{',
for ind, i in enumerate(get_all(alpha, length)):
	print ind, ':', i,
	print ',',
print '}'
