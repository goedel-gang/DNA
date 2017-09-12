import sys

#minimum distance is read from command line arguments
diff = int(sys.argv[1])

#functioning to determine closeness
def is_close(a, b, max_close):
    diff_count = 0

    for i, j in zip(a, b):
        if i != j:
            diff_count += 1

    return diff_count <= max_close

pool = []

#works through each line in stdin. if it is close to no previous line, it prints and adds to the pool of previous lines to check against
for j in sys.stdin:
	i = j.strip()

	for k in pool:
		if is_close(i, k, diff):
			break

	#is reached if there is no break
	else:
		pool.append(i)
		print i
