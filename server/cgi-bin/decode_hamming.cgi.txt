#!/usr/bin/python

import cgi, sys, cgitb
cgitb.enable()

input_data=cgi.FieldStorage()

translate = {'A': '0',
			 'C': '1',
			 'G': '2',
			 'T': '3'}

def is_power(n):
	return (n != 0) and not (n & (n - 1))

def toquat(dna):
	return ''.join([translate[i.upper()] for i in dna])

codes = input_data['codes'].value.split()

print 'Content-Type:text/html'
print

print '''<html>
	<head>
		<title>Decoded barcodes</title>
		<style type='text/css'>
			span#out {
				font-family: courier;
			}
		</style>
	</head>
	<body>
		<span id='out'>'''

for dna_text in codes:

	quad_text = toquat(dna_text)

	quad_text = quad_text.strip()
	code = [int(i) for i in quad_text]

	bad_parity = []
	bad_tallies = []
	badnorm_tallies = []
	desired_tallies = []

	for ind, i in enumerate(code):
		#if it's a parity quad, check parity
		if is_power(ind + 1):

			tally = 0

			#iterate over quads ocurring after parity quad
			for jnd, j in enumerate(code[ind + 1:], ind + 1):

				#if index should be covered
				if (jnd + 1) & (ind + 1):
					tally += j

			if code[ind] != tally % 4:
				bad_parity.append(ind + 1)
				badnorm_tallies.append(tally)
				desired_tallies.append(code[ind])

	#if an error was detected...
	if len(bad_parity) > 0:

		code[sum(bad_parity) - 1] += desired_tallies[0] - badnorm_tallies[0]

		code[sum(bad_parity) - 1] %= 4

	#go backwards through the sequence, removing parity quads
	for ind in range(len(code))[::-1]:
		if is_power(ind + 1):
			del code[ind]

	print '\t\t\t' + dna_text, '->', str(int(''.join([str(i) for i in code]), 4)) + '<br />'

print '''
		</span>
	</body>
</html>'''
