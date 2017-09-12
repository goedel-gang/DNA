import sys
from levenshtein import levenshtein

'''writes each pair of items that are too close in levenshtein edit distance'''

#reads minimum difference from command line arguments
diff = int(sys.argv[1])

pool = []

#goes through stdin
for line in sys.stdin:
	line = line.strip()

	#for every previous item
	for prev in pool:
		#if they are too close, alert the user
		if levenshtein(line, prev) <= diff:
			print line, prev, levenshtein(line, prev)

	#add item to pool of previous items
	pool.append(line)
