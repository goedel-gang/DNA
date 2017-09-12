import sys, bisect
from levenshtein import levenshtein
from BK_trees import BK_tree

'''a sieve that uses a BK-tree for checking. It appears to be murderously inefficient'''

#get top word, print it and use it to initialise the tree
w = next(sys.stdin).strip()

print w

tree = BK_tree([w])

#for each following word
for line in sys.stdin:
	line = line.strip()

	#if it doesn't match anything in the tree, print it and add it to the tree
	if not tree.match(line, 2):
		print line
		tree.add(line)
