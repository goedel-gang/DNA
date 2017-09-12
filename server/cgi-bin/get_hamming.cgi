#!/usr/bin/python

import cgi, sys, cgitb
cgitb.enable()

input_data=cgi.FieldStorage()

translate = {'0': 'A',
			 '1': 'C',
			 '2': 'G',
			 '3': 'T'}

alpha = '0123'

length = int(input_data['len'].value)

def todna(quat):
	return ''.join([translate[i] for i in quat])

def get_all(alph, length, word=''):
	if len(word) == length:
		yield word

	else:
		for i in alph:
			for j in get_all(alph, length, word + i):
				yield j

def is_power(n):
	return (n != 0) and not (n & (n - 1))

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


for quad_text in get_all(alpha, length):
	code = []

	it = iter(quad_text)

	try:
		while True:
			if is_power(len(code) + 1):
				code.append(-1)
			else:
				code.append(int(next(it)))

	except StopIteration:
		if code[-1] == -1:
			del code[-1]

	for ind, i in enumerate(code):
		if i == -1:
			tally = 0

			for jnd, j in enumerate(code[ind + 1:], ind + 1):

				if (ind + 1) & (jnd + 1):
					tally += j

			code[ind] = tally % 4

	print '\t\t\t' +  todna(''.join([str(i) for i in code])) + '<br />'
	

print '''
		</span>
	</body>
</html>'''
