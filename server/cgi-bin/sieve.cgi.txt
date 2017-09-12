#!/usr/bin/python

import sys, cgi, cgitb
from subprocess import Popen, PIPE

cgitb.enable()

input_data = cgi.FieldStorage()

diff = int(input_data['diff'].value)

codes = input_data['codes'].value.split()

try:
	head = input_data['head'].value
except KeyError:
	head = ''

min_val = float(input_data['min'].value)
max_val = float(input_data['max'].value)

def bad_temp(head, code, min_temp, max_temp):
	proc = Popen(['cgi-bin/oligotm', head + code], stdout=PIPE)
	temp = float(proc.communicate()[0])
	proc.wait()

	return not min_temp < temp < max_temp, temp

def is_close(a, b, max_close):
    diff_count = 0

    for i, j in zip(a, b):
        if i != j:
            diff_count += 1

    return diff_count < max_close

pool = []

print 'Content-Type:text/html'
print

print '''<html>
	<head>
		<title>Sieved barcodes</title>
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
		<button id='togg'>Toggle display temperatures</button><br/>
		<span id='out'>'''



for i in codes:
	
	t = bad_temp(head, i, min_val, max_val)

	if t[0]:
		continue

	for k in pool:
		if is_close(i, k, diff):
			break

	else:
		pool.append(i)
		print '\t\t\t{0}<span class="temp"> <strong>{1}</strong>{0} {2}</span><br />'.format(i, head, t[1])

print '''
		</span>
	</body>
</html>'''
