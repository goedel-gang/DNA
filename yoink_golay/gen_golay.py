import yoink

for j in xrange(2**12):
	print yoink.encode([int(i) for i in format(j, '012b')])
