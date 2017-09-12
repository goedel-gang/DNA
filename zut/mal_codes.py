import random, sys

ran_mal = int(sys.argv[1])

codes = [['a'] * 6]

def malform(code, ext):
	out = code[:]

	for _ in range(ext):
		i = random.randint(0, len(code) - 1)

		out[i] = 'actg'[random.randint(0, 3)]

	return out

for _ in range(100):
	codes.append(malform(codes[-1], ran_mal))

print '\n'.join([''.join(i) for i in codes])

#for i in {1..30}; do echo $i: $(python generate_codes.py $i | python validity_check.py | wc -l); done
