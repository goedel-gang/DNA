import sys
from matrices import Matrix

'''generates hadamard codes, using the hadamard matrix constructin, which are made using the sylvester construction
https://en.wikipedia.org/wiki/Hadamard_matrix
https://en.wikipedia.org/wiki/Hadamard_code'''

#the length of the codes will be 2 ** size
size = int(sys.argv[1])

H = Matrix([[1]])

while size:
	size -= 1

	H = H.append_right(H).append_under(H.append_right(H * -1))

for row in H.append_under(H * -1):
	for i in row:
		sys.stdout.write(str((i + 1) / 2))

	sys.stdout.write('\n')
