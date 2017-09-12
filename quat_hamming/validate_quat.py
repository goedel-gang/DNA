import sys

'''checks if the input consists of quaternary numbers with an increment of 1 each time'''

#grabs the first line
last = int(next(sys.stdin).strip(), 4)

for line in sys.stdin:
	line = int(line.strip(), 4)

	#if the increment is not one
	if line - last != 1:
		print False
		#break from the for/else structure
		break

	last = line

#if no break has happened
else:
	print True
