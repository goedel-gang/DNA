#!/usr/bin/python

'''a CGI script to get Hadamard codes. thinly wraps dna/hadamard/get_hadamard.py'''

import sys, cgi, cgitb
#outputs a nice error traceback in case of an emergency
cgitb.enable()

input_data = cgi.FieldStorage()

in_codes = input_data['codes'].value.split()

size = len(in_codes) / 2

#defines a Matrix class. not really used but nice to have
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

#print a header telling the client this is html
print 'Content-Type:text/html'
print

#print some setup html
print '''<html>
	<head>
		<title>Decoded barcodes</title>
		<style type='text/css'>
			span#out {
				font-family: courier;
			}
			
			span.temp {
				display: none;
			}
		</style>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
		<script>
			var hidden = true;

			$(document).ready(function() {
				$('button#togg').click(function() {
					if (hidden) {
						$('span.temp').show();
						hidden = false;

					} else {
						$('span.temp').hide();
						hidden = true;

					}

				});
			});

		</script
	


	</head>
	<body>
		<button id="togg">Toggle display of distance</button><br />
		<span id='out'>'''

#iterate Sylvester's construction
while size != 1:
	size /= 2

	H = H.append_right(H).append_under(H.append_right(H * -1))

#dictionary to translate a tuple of two consecutive binary digits to DNA
translate = {(0, 0): 'A',
			 (0, 1): 'C',
			 (1, 0): 'G',
			 (1, 1): 'T'}

sys.stdout.write('\t\t\t')

had_codes = []

for row in H.append_under(H * -1):
	had_codes.append('')
	for i in zip(row[::2], row[1::2]):
		had_codes[-1] += translate[((i[0] + 1) / 2, (i[1] + 1) / 2)]

#find hamming distance between a and b
def hamming(a, b):
	return sum(ca != cb for ca, cb in zip(a, b))

for in_code in in_codes:
	best_code = ''
	best_dist = float('inf')
	best_ind = -1

	for ind, had_code in enumerate(had_codes):
		if hamming(in_code, had_code) < best_dist:
			best_ind = ind
			best_code = had_code
			best_dist = hamming(in_code, had_code)

	sys.stdout.write('{} -> {} ({})<span class="temp"> distance of {}</span><br />\n\t\t\t'.format(in_code, best_code, format(best_ind, '0{}'.format(len(str(len(had_codes))))), best_dist))

print '''
		</span>
	</body>
</html>'''
