'''defines a class for a matrix, which basically just wraps a two-dimensional list'''

#function to recursively apply a callable to every item in a two-dimensional list - not needed anymore
def list_op(func, l):
	if type(l) == list:
		return [list_op(func, i) for i in l]

	else:
		return func(l)

class Matrix(object):
	def __init__(self, l=[[]]):
		self.contents = l

	def __mul__(self, other):
		if isinstance(other, Matrix):
			self_rows = [row for row in self]
			other_cols = [[row[i] for row in other] for i in range(len(other[0]))]

			return Matrix([[sum([a * b for a, b in zip(row, col)]) for col in other_cols] for row in self_rows])

		else:
			return Matrix([[i * other for i in row] for row in self])

	def __add__(self, other):
		return Matrix([[a + b for a, b in zip(ra, rb)] for ra, rb in zip(self, other)])
		
	def __str__(self):
		max_width = 0

		out = ''
		
		for row in self:
			for i in row:
				if len(str(i)) > max_width:
					max_width = len(str(i))

		for row in self:
			out += '|'
			for i in row:
				out += format(i, ' {}'.format(max_width + 1))

			out += ' |\n'

		return out

	def __iter__(self):
		return iter(self.contents)

	def __getitem__(self, ind):
		return self.contents[ind]

	def __len__(self):
		return len(self.contents)

	def append_right(self, other):
		return Matrix([rowa + rowb for rowa, rowb in zip(self, other)])

	def append_under(self, other):
		return Matrix(self.contents + other.contents)

if __name__ == '__main__':

	a = Matrix([[1, 2, 3],
				[4, 5, 6],
				[7, 8, 9]])

	b = Matrix([[1, 0, 1],
				[2, 1, 2],
				[2, 1, 3]])

	c = Matrix([[2, 3, 4],
				[1, 0, 0]])

	d = Matrix([[0, 1000],
				[1, 100],
				[0, 10]])

	print 'a:'
	print a
	print 'b:'
	print b
	print 'a * 2:'
	print a * 2
	print 'a + b:'
	print a + b
	print 'a * b:'
	print a * b
	print 'c:'
	print c
	print 'd:'
	print d
	print 'c * d:'
	print c * d
