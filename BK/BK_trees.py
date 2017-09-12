import sys, bisect
from levenshtein import levenshtein

'''not yet done. would like to use bisect again to access the children more quickly.'''

class BK_tree(object):
	'''A class for a BK-tree:
	http://blog.notdot.net/2007/4/Damn-Cool-Algorithms-Part-1-BK-Trees
	https://nullwords.wordpress.com/2013/03/13/the-bk-tree-a-data-structure-for-spell-checking/
	It is done recursively, as each subnode (?) of a node is the top node of a smaller tree'''

	def __init__(self, words=[], dist='', depth=0):
		#distance from parent
		self.dist = dist

		#children
		self.children = []

		#set of children distances, for quick access
		self.dists = set()

		#knows its own depth, used for string output
		self.depth = depth

		#__init__ needs to be given at least one word, to be the top node, 
		if len(words) > 0:
			#gets top node
			self.word = words.pop(0)

			#adds the rest, using self.add
			for i in words:
				self.add(i)
		
		else:
			raise ValueError('You can\'t have a tree with no branches!')
			

	#add a word to a tree
	def add(self, word):
		dist = levenshtein(self.word, word)

		#if there already exists a child with this distance, add the word to this child
		if dist in self.dists:
			for i in self.children:
				if i.dist == dist:
					i.add(word)
					break

		#otherwise, add it as a new child and add the distance to the set of distances
		else:
			self.dists.add(dist)
			self.children.append(BK_tree([word], dist, self.depth + 1))

	#see if a word is within a distance of any words in the tree
	def match(self, word, n):
		d = levenshtein(self.word, word)

		if d <= n:
			return True

		if not self.children:
			return False

		else:
			return any(i.match(word, n) for i in filter(lambda x: d - n <= x.dist <= d + n, self.children))

	#return words in the tree within a distance of a given word
	def query(self, word, n):
		d = levenshtein(self.word, word)

		if d <= n:
			yield self.word

		if self.children:

			for y in [i.query(word, n) for i in filter(lambda x: d - n <= x.dist <= d + n, self.children)]:
				for yy in y:
					yield yy

	#an indented representation - the bits it prints are more readable than it itself
	def __str__(self):
		return '{0}{1}:{2}(\n{3}\n{0})\n'.format('\t' * self.depth, self.dist, self.word, str(self.children)[1:-1].replace(',', ''))

	def __repr__(self):
		return str(self)

#if the file is run, show some examples
if __name__ == '__main__':
	tree = BK_tree(['cat', 'cut', 'man', 'hat'])
	tree.add('hit')
	print tree

	tree = BK_tree(['book', 'books', 'cake', 'boo', 'cape', 'cart', 'boon', 'cook'])
	print tree

	print list(tree.query('bood', 1))

	tree = BK_tree(['leeds', 'bristol', 'york', 'leicester', 'hull'])

	print tree

	print tree.match('holi', 2)

	print list(tree.query('leeda', 2))
