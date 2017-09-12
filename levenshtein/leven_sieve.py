import sys
from levenshtein import levenshtein

'''sieves through stdin, outputting items that have more than a certain levenshtein distance form each other'''

#reads minimum difference from command line arguments
diff = int(sys.argv[1])

pool = []

#goes through stdin
for line in sys.stdin:
	line = line.strip()

	#for each previously printed item
	for prev in pool:

		#if the item is too close
		if levenshtein(line, prev) <= diff:
			#break from the for/else structure
			break

	#if the break has not occurred
	else:
		#print the line and add it to the pool of previous lines
		print line
		pool.append(line)
