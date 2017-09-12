import sys, random

#introduce a single error
for word in sys.stdin:
	word = word.strip()

	#choose an index
	ind = random.randint(0, len(word) - 1)

	#choose a new value to change it to
	val = random.choice(filter(lambda x: x != word[ind], ['0', '1', '2', '3']))

	print '{}{}{}'.format(word[:ind], val, word[ind+1:])
