#!/usr/bin/python

import sys, cgi, cgitb

cgitb.enable()

input_data = cgi.FieldStorage()

size = int(input_data['len'].value) - 1

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

H = Matrix([[1]])

print 'Content-Type:text/html'
print

print '''<html>
	<head>
		<title>Barcodes for use</title>
		<style type='text/css'>
			span#out {
				font-family: courier;
			}
		</style>
	</head>
	<body>
		<span id='out'>'''

while size:
	size -= 1

	H = H.append_right(H).append_under(H.append_right(H * -1))

translate = {(0, 0): 'A',
			 (0, 1): 'C',
			 (1, 0): 'G',
			 (1, 1): 'T'}

sys.stdout.write('\t\t\t')

for row in H.append_under(H * -1):
	for i in zip(row[::2], row[1::2]):
		sys.stdout.write(translate[((i[0] + 1) / 2, (i[1] + 1) / 2)])

	sys.stdout.write('<br />\n\t\t\t')

print '''
		</span>
	</body>
</html>'''
